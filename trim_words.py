import os
from google.cloud import speech_v1p1beta1 as speech

# Set the path to the audio file
audio_file = "/Users/dylanwalsh/Code/input/audio_files/audios_manual/english/english15.wav"


client = speech.SpeechClient.from_service_account_file(key_path)

# Initialize the Google Speech-to-Text client
client = speech.SpeechClient.from_service_account_file(key_path)

# Load the audio file
with open(audio_file, "rb") as audio:
    audio_data = audio.read()

# Set the audio configuration
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    language_code="en-US",
    enable_word_time_offsets=True,
)


operation = client.long_running_recognize(config=config, audio=speech.RecognitionAudio(content=audio_data))

print("Waiting for operation to complete...")
result = operation.result(timeout=90)

for result in result.results:
    alternative = result.alternatives[0]
    print("Transcript: {}".format(alternative.transcript))
    print("Confidence: {}".format(alternative.confidence))

    for word_info in alternative.words:
        word = word_info.word
        start_time = word_info.start_time
        end_time = word_info.end_time

        print(
            f"Word: {word}, start_time: {start_time.total_seconds()}, end_time: {end_time.total_seconds()}"
        )
