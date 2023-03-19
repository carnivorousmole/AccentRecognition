# remove filename extra details to return .wav file to just its originalLanguageNumber.wav

import os
import re

# Define the directory path where the files are located
directory_path = "/Users/dylanwalsh/Code/input/audio_files/audios_word_split"

# Define the regex pattern to match the filename format
pattern = r"^(.*?)_.*?\.(\w+)$"

# Loop through all the files in the directory and its subdirectories
for root, dirs, files in os.walk(directory_path):
    for file in files:
        # Check if the file matches the pattern
        match = re.match(pattern, file)
        if match:
            # Extract the prefix and extension
            prefix, extension = match.groups()
            # Define the new file name
            new_name = prefix + '.' + extension
            # Get the original file path
            original_path = os.path.join(root, file)
            # Get the new file path
            new_path = os.path.join(root, new_name)
            # Rename the file
            os.rename(original_path, new_path)
