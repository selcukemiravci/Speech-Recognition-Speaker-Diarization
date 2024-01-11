import os
import subprocess
import datetime
import pvfalcon
import json

def record_audio():
    # Records audio using FFmpeg and saves it as a WAV file
    today = datetime.datetime.now().strftime('%Y%m%d')
    audio_file = f"./{today}.wav"
    subprocess.run([
        "ffmpeg", "-f", "avfoundation", "-i", ":YOUR_INPUT_SOURCE",
        "-ar", "16000",  # Set sample rate to 16 kHz
        "-ac", "1",      # Set audio to mono
        "-t", "15",      # Record for 15 seconds
        audio_file
    ])
    return audio_file

def transcribe_audio(audio_file):
    # Transcribes the audio using Whisper
    subprocess.run(["whisper", audio_file, "--model", "medium", "--language", "English"], check=True)
    json_output = f"{audio_file.rsplit('.', 1)[0]}.json"
    # Display macOS notification when transcription is complete
    subprocess.run(["osascript", "-e", 'display notification "Whisper Transcription Complete!" with title "Whisper AI"'])
    if not os.path.exists(json_output):
        raise FileNotFoundError(f"The file {json_output} was not created by Whisper.")
    with open(json_output, 'r') as f:
        transcription = json.load(f)
    return transcription

def perform_diarization(audio_file, access_key):
    # Applies Falcon's speaker diarization on the audio file
    falcon = pvfalcon.create(access_key=access_key)
    segments = falcon.process_file(audio_file)
    falcon.delete() # Clean up Falcon instance after processing
    # Display macOS notification when diarization is complete
    subprocess.run(["osascript", "-e", 'display notification "Falcon Diarization Complete!" with title "Falcon AI"']) 

def merge_transcripts(transcription, diarization, overlap_threshold=0.2):
    # Merges transcripts from Whisper and diarization data from Falcon
    merged_output = []
    used_transcript_segments = set()

    for seg in diarization:
        speaker_tag = f"Speaker {seg.speaker_tag}"

        for part in transcription['segments']:
            if part['id'] in used_transcript_segments:
                continue  # Skip segments already used

            overlap_start = max(seg.start_sec, part['start'])
            overlap_end = min(seg.end_sec, part['end'])
            overlap_duration = max(0, overlap_end - overlap_start)

            diarization_duration = seg.end_sec - seg.start_sec
            transcription_duration = part['end'] - part['start']
            min_duration = min(diarization_duration, transcription_duration)

            if overlap_duration >= overlap_threshold * min_duration:
                merged_output.append({
                    'speaker': speaker_tag,
                    'start': overlap_start,
                    'end': overlap_end,
                    'text': part['text']
                })
                used_transcript_segments.add(part['id'])

 # Sort and merge close segments
    merged_output.sort(key=lambda x: (x['speaker'], x['start']))
    final_output = []
    for seg in merged_output:
        if final_output and seg['speaker'] == final_output[-1]['speaker'] and seg['start'] - final_output[-1]['end'] < 1:
            final_output[-1]['end'] = seg['end']  # Extend the previous segment
            final_output[-1]['text'] += ' ' + seg['text']
        else:
            final_output.append(seg)

    return final_output
def main():
    access_key = "YOUR_FALCON_ACCESS_KEY" # Replace with your actual Falcon access key
    audio_file = record_audio()
    transcription = transcribe_audio(audio_file)
    diarization = perform_diarization(audio_file, access_key)
    merged_output = merge_transcripts(transcription, diarization)
    # Print the final output with speaker tags and timestamps
    for m in merged_output:
        print(f"{m['speaker']} [{m['start']:.2f}-{m['end']:.2f}] {m['text'].strip()}")
    os.remove(audio_file)  # Clean up the audio file

if __name__ == "__main__":
    main()