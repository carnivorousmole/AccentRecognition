import os
import shutil

source_dir = '/Users/dylanwalsh/Code/input/audio_files/audios_word_split'
text = 'Please call Stella.  Ask her to bring these things with her from the store:  Six spoons of fresh snow peas, five thick slabs of blue cheese'

# split the text into a list of words, and convert all words to lowercase
words = [word.lower() for word in text.split()]

for word in words:
    target_dir = f'/Users/dylanwalsh/Code/input/audio_files/audios_word_split_indiv/{word}' # create separate output directory for each word
    os.makedirs(target_dir, exist_ok=True) # create the directory if it doesn't exist
    
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if word in file.lower():
                src_path = os.path.join(root, file)
                dst_path = src_path.replace(source_dir, target_dir)
                shutil.copy2(src_path, dst_path)
