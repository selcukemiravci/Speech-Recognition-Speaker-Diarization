import os
import subprocess
import datetime
import pvfalcon
# This file is created to interact and experiment with the Falcon  with Whisper without using the merge transcripts function.

def record_audio():
    today = datetime.datetime.now().strftime('%Y%m%d')
    audio_file = f"./{today}.mp3"
    # Record audio using the specified device for 60 seconds
    subprocess.run(["ffmpeg", "-f", "avfoundation", "-i", ":YOUR INPUT DEVICE", "-t", "20", audio_file])
    return audio_file

def transcribe_audio(audio_file):
    # Transcribe the audio file using Whisper command-line tool
    subprocess.run(["whisper", audio_file, "--model", "medium", "--output_format", "txt"])
    # Send notification that Whisper transcription is complete
    subprocess.run(["osascript", "-e", 'display notification "Whisper Transcription Complete!" with title "Whisper AI"'])

def perform_diarization(audio_file, access_key):
    try:
        falcon = pvfalcon.create(access_key=access_key)
        segments = falcon.process_file(audio_file)
        for segment in segments:
            print(f"Speaker {segment.speaker_tag} from {segment.start_sec:.2f} to {segment.end_sec:.2f} seconds")
    finally:
        if 'falcon' in locals():
            falcon.delete()
    # Send notification that Falcon diarization is complete
    subprocess.run(["osascript", "-e", 'display notification "Falcon Diarization Complete!" with title "Falcon AI"'])

def main():
    access_key = "YOUR_ACCESS_KEY"  # Replace with your Falcon access key
    audio_file = record_audio()
    transcribe_audio(audio_file)
    perform_diarization(audio_file, access_key)
    os.remove(audio_file)

if __name__ == "__main__":
    main()
