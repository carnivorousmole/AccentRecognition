import os
import fnmatch
import librosa
import soundfile as sf
import shutil

# Set the directory path
source_directory = "/Users/dylanwalsh/Code/AccentRecognition_Dylan/audios"
directory = "/Users/dylanwalsh/Code/AccentRecognition_Dylan/audios_manual"

# Copy all contents of the source directory into the destination directory
shutil.copytree(source_directory, directory)

# Set the target duration for the shortened audio files
target_duration = 5.0  # in seconds

# Loop through all files and directories in the directory
for root, dirs, files in os.walk(directory):
    for filename in files:
        # Check if the file name contains "unsilenced" or ".mp3"
        if fnmatch.fnmatch(filename, "*unsilenced*") or fnmatch.fnmatch(filename, "*.mp3"):
            # Delete the file
            os.remove(os.path.join(root, filename))
            print(f"Deleted file: {os.path.join(root, filename)}")
        
        # Check if the file name contains ".wav"
        elif fnmatch.fnmatch(filename, "*.wav"):
            # Load the audio file and get the sample rate
            audio_path = os.path.join(root, filename)
            audio_exists = os.path.exists(audio_path)
            if audio_exists:
                audio, sr = librosa.load(audio_path, sr=None)

                # Calculate the number of samples for the target duration
                target_samples = int(target_duration * sr)

                # Shorten the audio to the target duration
                audio = audio[:target_samples]

                # Save the shortened audio file
                sf.write(audio_path, audio, sr)
                print(f"Shortened file: {audio_path}")
            else:
                print(f"File not found: {audio_path}")