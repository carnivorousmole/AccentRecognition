import os
import shutil
import re

source_dir = '/Users/dylanwalsh/Code/input/audio_files/audios_word_split'
text = 'Please call Stella.  Ask her to bring these things with her from the store:  Six spoons of fresh snow peas, five thick slabs of blue cheese'

words = [word.lower() for word in text.split()]

words = [re.sub('[^a-zA-Z]+', '', word) for word in words]

for word in words:
    target_dir = f'/Users/dylanwalsh/Code/input/audio_files/audios_word_split_indiv/{word}'
    os.makedirs(target_dir, exist_ok=True)
    print(f"Created directory '{target_dir}'")

for root, dirs, files in os.walk(source_dir):
    for file in files:
        for word in words:
            if word in file.lower():
                src_path = os.path.join(root, file)
                dst_dir = os.path.join('/Users/dylanwalsh/Code/input/audio_files/audios_word_split_indiv', word, os.path.relpath(root, source_dir))
                dst_path = os.path.join(dst_dir, file)
                os.makedirs(dst_dir, exist_ok=True)
                print(f"Created directory '{dst_dir}'")
                shutil.copy2(src_path, dst_path)
                print(f"Copied '{file}' to '{dst_path}'")
