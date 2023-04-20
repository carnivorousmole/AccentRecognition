import os
import glob

# Set the path of the directory you want to search for WAV files
directory_path1 = "/Users/dylanwalsh/Code/input/audio_files/audios_word_split/please_call_Stella_ask_her_"
directory_path2 = "/Users/dylanwalsh/Code/input/audio_files/audios_manual"

directory_path1 = "/Users/dylanwalsh/Code/input/audio_files/audios_word_split/please_call_Stella_ask_her_/english"
directory_path2 = "/Users/dylanwalsh/Code/input/audio_files/audios_manual/english"

# Get a list of all the WAV files in the directory and its subdirectories
wav_files1 = glob.glob(os.path.join(directory_path1, "**/*.wav"), recursive=True)
wav_files2 = glob.glob(os.path.join(directory_path2, "**/*.wav"), recursive=True)

# Count the number of WAV files
num_wav_files1 = len(wav_files1)
num_wav_files2 = len(wav_files2)

# Print the number of WAV files found
print(f"Found {num_wav_files1} WAV files in {directory_path1}")
print(f"Found {num_wav_files2} WAV files in {directory_path2}")
# percentage
print(f"Percentage of files in {directory_path1} that are in {directory_path2}: {num_wav_files1/num_wav_files2*100}%")