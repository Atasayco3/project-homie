# Project Homie

A Python-based personal voice assistant designed to support natural voice interactions, execute commands, and eventually integrate conversational AI.

This project is being developed incrementally as a hands-on exploration of Python, speech recognition, text-to-speech, AI integration, and software engineering principles.

## Current Features

- Speech-to-text using SpeechRecognition.
- Microphone input through PyAudio.
- Text-to-speech responses using pyttsx3.
- Recognition of predefined conversational commands.
- Continuous listening with voice-activated shutdown.
- Timestamped, two-way conversation logging.

## Technologies

- Python 3.12
- SpeechRecognition
- PyAudio
- pyttsx3

## Installation

1. Clone the repository.
2. Create a Python virtual environment.
3. Activate the virtual environment.
4. Install dependencies using:

   `python -m pip install -r requirements.txt`

5. Run the application:

   `python main.py`

A working microphone, audio output, internet connection for the current speech recognition implementation, and compatible audio drivers are required.

## Planned Features

- More flexible speech recognition.
- Integration with a conversational language model.
- Persistent conversational memory.
- Computer automation and command execution.
- Improved voice customization.
- Potential smart-home integration.

## Privacy

Personal conversation logs, virtual environments, and local environment configuration files are excluded from version control using `.gitignore`.

## Project Status

Early development — functional voice interaction prototype.