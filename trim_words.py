import os
import wave
import contextlib
import speech_recognition as sr

# Set the directory containing the .wav files
dir_path = "/Users/dylanwalsh/Code/input/audio_files/audios_manual_please_call_stella/english"

# Loop through all .wav files in the directory
for filename in os.listdir(dir_path):
    if filename.endswith(".wav"):
        filepath = os.path.join(dir_path, filename)
        
        # Open the .wav file and get its properties
        with contextlib.closing(wave.open(filepath, 'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duration = frames / float(rate)
            
            # Use speech recognition to get the transcript of the first three words
            r = sr.Recognizer()
            with sr.AudioFile(filepath) as source:
                audio_data = r.record(source, duration=4) # Record 4 seconds (to be safe)
            try:
                transcript = r.recognize_google(audio_data).split()[:3] # Get the first three words
            except sr.UnknownValueError:
                print(f"Speech recognition could not understand audio file {filename}")
                continue
            
            # Trim the .wav file to the length of the first three words
            new_duration = len(transcript) / float(rate)
            with wave.open(filepath, 'r') as f:
                new_filepath = os.path.join(dir_path, f"{filename[:-4]}_trimmed.wav")
                with wave.open(new_filepath, 'w') as nf:
                    nf.setnchannels(f.getnchannels())
                    nf.setsampwidth(f.getsampwidth())
                    nf.setframerate(f.getframerate())
                    nf.setnframes(int(new_duration * rate))
                    nf.writeframes(f.readframes(int(new_duration * rate)))
