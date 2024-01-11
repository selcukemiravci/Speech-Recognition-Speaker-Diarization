import pvfalcon

def main():
    # Replace 'YOUR_ACCESS_KEY' with your actual Picovoice Falcon access key
    access_key = "01Qbu3lPruanfLbozZgehd8JjvmFrfPP1E9sTQxuS1j1nM1w++5kCQ=="

    # Path to your audio file
    audio_file_path = "sample audio.mp3"  # Replace with the path to your audio file

    try:
        # Create an instance of the Falcon diarization engine
        falcon = pvfalcon.create(access_key=access_key)

        # Perform speaker diarization on the audio file
        segments = falcon.process_file(audio_file_path)

        # Print the diarization results
        print("Diarization segments:")
        for segment in segments:
            print(f"Speaker {segment.speaker_tag} from {segment.start_sec:.2f} to {segment.end_sec:.2f} seconds")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Clean up resources
        if 'falcon' in locals():
            falcon.delete()

if __name__ == "__main__":
    main()
