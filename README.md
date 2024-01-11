# Speech Recognition & Speaker Diarization with Whisper & Falcon 🗣️
 
 ## Introduction
Explore the transformative power of speech recognition and speaker diarization in this tutorial. We'll integrate [OpenAI's Whisper](https://github.com/openai/whisper) for advanced transcription and [Picovoice's Falcon](https://picovoice.ai/platform/falcon/) to precisely identify speakers, offering unparalleled audio conversation analysis.

## Background
Utilizing Whisper's capabilities for terminal-based transcriptions, we'll enhance it with Falcon's diarization to distinctively identify speakers. This integration improves transcription accuracy and enriches the context of who is speaking and when, enabling sophisticated AI-driven audio analysis. Join us as we demonstrate the power of these cutting-edge technologies in unison!

##Installation & Setup
###1. Audio Recording
Install [FFmpeg](https://ffmpeg.org/), an all-in-one tool for audio and video, which we'll use for recording audio and creating transcriptions with Whisper AI.

**Homebrew**
```brew install ffmpeg```

**Chocolatey**
```choco install ffmpeg```

Once installed, use FFmpeg to list all inputs on your machine. Select an input device for later use.

**Mac OS**
`ffmpeg -f avfoundation -list_devices true -i ""`

**Linux**
`ffmpeg -f alsa -list_devices true -i ""`

**Windows**
`ffmpeg -f dshow -list_devices true -i dummy
`

Note the exact name of the audio input you'll use.

###2. Whisper Speaker Recognition
To use OpenAI's Whisper for speaker recognition, follow these steps:

- **Install Python 3.8–3.11**
Check your Python version with python3 -V. If it's not within 3.8–3.11, download the latest 3.11 version from [python.org](https://www.python.org/).

- Install PIP
Ensure Python's package manager is installed with `python3 -m pip --version`
Install or upgrade it with:`python3 -m pip install --upgrade pip`

- **Install Whisper AI**
Install Whisper and its dependencies via:
`pip install -U openai-whisper`

###3. Falcon Speaker Diarization 
To install Picovoice's Falcon for speaker diarization:
Create an account and get your AccessKey from [Picovoice's Dashboard](https://console.picovoice.ai/).
Install the [pvleopard Python package](https://pypi.org/project/pvleopard/) using `pip3 install pvfalcon`

## Python Script for Audio Recording, Transcription, and Diarization

This Python script demonstrates the integration of Whisper for transcription and Falcon for speaker diarization. The script records audio, transcribes it, performs speaker diarization, and outputs the final transcript with speaker labels.

This integration of Whisper and Falcon offers devs a powerful tool 🛠️ for audio analysis. The script not only transcribes but also assigns text to specific speakers with timestamps 🕒. 

It's a perfect starting point for further customization. Dive into this project, tweak it, and adapt it to your needs 🤝!
