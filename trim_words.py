import os
from google.cloud import speech_v1p1beta1 as speech

# Set the path to the audio file
directory_path = "/Users/dylanwalsh/Code/input/audio_files/audios_manual"

key_path = "/Users/dylanwalsh/keys/formal-theater-380811-968fef63f10f.json"

# Initialize the Google Speech-to-Text client
client = speech.SpeechClient.from_service_account_file(key_path)

# Set the audio configuration
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    language_code="en-US",
    enable_word_time_offsets=True,
)

# Recursively loop through the directory and its subdirectories
for root, dirs, files in os.walk(directory_path):
    for file in files:
        # Check if the file is an audio file
        if file.endswith(".wav"):
            # Set the path to the audio file
            audio_file = os.path.join(root, file)

            # Load the audio file
            with open(audio_file, "rb") as audio:
                audio_data = audio.read()

            # Send the audio data to the Speech-to-Text API for transcription
            operation = client.long_running_recognize(config=config, audio=speech.RecognitionAudio(content=audio_data))

            print(f"Transcribing {audio_file}...")

            # Get the transcription and timing information
            result = operation.result(timeout=90)
            transcription = result.results[0].alternatives[0].transcript
            words = result.results[0].alternatives[0].words

            # Split the audio file into separate .wav files for each word
            for i, word in enumerate(words):
                start_time = word.start_time.total_seconds()
                end_time = word.end_time.total_seconds()

                # Set the path to the new .wav file
                file_name = os.path.splitext(file)[0]
                word_file_name = f"{file_name}_{word.word}.wav"
                word_file_path = os.path.join(root, word_file_name)

                # Use FFmpeg to extract the word segment from the audio file and save it as a new .wav file
                os.system(f"ffmpeg -i {audio_file} -ss {start_time} -to {end_time} -c copy {word_file_path}")
                print(f"Saved {word_file_path}")
