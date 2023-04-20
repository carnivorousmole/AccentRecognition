import os
import shutil
from tqdm import tqdm

input_dir = "/Users/dylanwalsh/Code/input/audio_files/audios_word_split"
output_dir = "/Users/dylanwalsh/Code/input/audio_files/audios_word_split_by_numbers"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Count the number of subdirectories in the input directory
num_subdirs = sum(os.path.isdir(os.path.join(input_dir, subdir)) for subdir in os.listdir(input_dir))

# Use tqdm to show progress while copying files
with tqdm(total=num_subdirs, desc="Copying audio files") as pbar:
    for subdir in os.listdir(input_dir):
        if not os.path.isdir(os.path.join(input_dir, subdir)):
            continue

        word_count = subdir.count('_')
        output_subdir = os.path.join(output_dir, str(max(word_count, 1)))

        if not os.path.exists(output_subdir):
            os.makedirs(output_subdir)

        src_dir = os.path.join(input_dir, subdir)
        dst_dir = os.path.join(output_subdir, subdir)

        for root, dirs, files in os.walk(src_dir):
            rel_root = os.path.relpath(root, src_dir)
            new_root = os.path.join(dst_dir, rel_root)

            if not os.path.exists(new_root):
                os.makedirs(new_root)

            for file in files:
                src_path = os.path.join(root, file)
                dst_path = os.path.join(new_root, file)
                shutil.copy2(src_path, dst_path)

        pbar.update(1)

print("Done!")
