import os
from google.cloud import speech_v1p1beta1 as speech

# Set the path to the audio file
directory_path = "/Users/dylanwalsh/Code/input/audio_files/audios_manual"

key_path = "/Users/dylanwalsh/keys/formal-theater-380811-968fef63f10f.json"

# Set the path to the output directory
output_directory_path = "/Users/dylanwalsh/Code/input/audio_files/audios_word_split"

def directory_contains_file_containing_string(directory_path, string_to_search):
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for filename in filenames:
            if string_to_search in filename:
                return True
    return False


# Create a file to store the error cases
error_file = open("error_cases.txt", "w")

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
    # Get the relative path of the root directory
    rel_path = os.path.relpath(root, directory_path)

    # Create the corresponding output directory
    # print the output and relative paths


    for file in files:
        # Check if the file is an audio file
        if file.endswith(".wav"):
            base, extension = os.path.splitext(file)
            if directory_contains_file_containing_string(output_directory_path, base + ".wav"):
                print(f"Already Processed: {file}...")
            else:
                # Set the path to the audio file
                audio_file = os.path.join(root, file)

                # Load the audio file
                with open(audio_file, "rb") as audio:
                    audio_data = audio.read()
                
                # Send the audio data to the Speech-to-Text API for transcription
                operation = client.long_running_recognize(config=config, audio=speech.RecognitionAudio(content=audio_data))

                print(f"Transcribing {audio_file}...")

                try:
                    result = operation.result(timeout=90)
                    transcription = result.results[0].alternatives[0].transcript
                    words = result.results[0].alternatives[0].words

                    print(f"Transcription: {transcription}")
                    # Split the audio file into separate .wav files for each word

                    # get start time of the first word
                    start_time_first_word = words[0].start_time.total_seconds()
                    words_so_far = ""

                    for i, word in enumerate(words):
                        
                        words_so_far += word.word + "_"

                         # Create the corresponding output directory
                        output_root_for_this_word = output_directory_path + "/" + word.word + "/" + rel_path
                        output_root_for_words_so_far = output_directory_path + "/" + words_so_far + "/" + rel_path
                        os.makedirs(output_root_for_this_word, exist_ok=True)
                        os.makedirs(output_root_for_words_so_far, exist_ok=True)

                        start_time = word.start_time.total_seconds()
                        end_time = word.end_time.total_seconds()

                        original_file_name = os.path.splitext(file)[0]

                        # Set the path to the new .wav file for this individual word
                        word_file_name = f"{original_file_name}.wav"
                        word_file_path = os.path.join(output_root_for_this_word, word_file_name)
                        # set the path for the words so far
                        words_file_name = f"{original_file_name}.wav"
                        words_file_path = os.path.join(output_root_for_words_so_far, words_file_name)

                        # Use FFmpeg to extract the word segment from the audio file and save it as a new .wav file
                        os.system(f"ffmpeg -hide_banner -loglevel error -i {audio_file} -ss {start_time} -to {end_time} -c copy -y {word_file_path}")
                        os.system(f"ffmpeg -hide_banner -loglevel error -i {audio_file} -ss {start_time_first_word} -to {end_time} -c copy -y {words_file_path}")

                        print(f"Saved {word_file_path}")
                        print(f"Saved {words_file_path}")

                except (IndexError, AttributeError) as e:
                    print(f"Error: {e}. Skipping {audio_file}...")
                    with open("error_cases.txt", "a") as error_file:
                        error_file.write(audio_file + "\n")