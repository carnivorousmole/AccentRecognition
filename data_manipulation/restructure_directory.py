import os
import shutil

# Define the source directory
source_directory = "/Users/dylanwalsh/Code/input/audio_files/audios_word_split"

# Define the destination directory
destination_directory = "/Users/dylanwalsh/Code/input/audio_files/audios_word_split_reorganized"

# Loop through all the language directories in the source directory
for language_directory in os.scandir(source_directory):
    if language_directory.is_dir():
        # Loop through all the word directories in the current language directory
        for word_directory in os.scandir(language_directory.path):
            if word_directory.is_dir():
                # Create the destination directory for the current word directory
                destination_word_directory = os.path.join(destination_directory, word_directory.name)
                os.makedirs(destination_word_directory, exist_ok=True)
                # Create the subdirectory for the current language directory within the current word directory
                destination_language_directory = os.path.join(destination_word_directory, language_directory.name)
                os.makedirs(destination_language_directory, exist_ok=True)
                # Copy all the files from the current word directory to the destination language directory
                for file in os.scandir(word_directory.path):
                    if file.is_file():
                        shutil.copy(file.path, destination_language_directory)
