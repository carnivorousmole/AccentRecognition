import os
import shutil

# Set source and output directories
source_dir = '/Users/dylanwalsh/Code/input/audio_files/audios'
output_dir = '/Users/dylanwalsh/Code/input/audio_files/audios_unsilenced'

# Loop through all directories and files in source directory
for root, dirs, files in os.walk(source_dir):
    for file in files:
        if '_unsilenced' in file:
            # Construct paths
            src_path = os.path.join(root, file)
            dst_path = os.path.join(root.replace(source_dir, output_dir), file.replace('_unsilenced', ''))

            # Create output directory if it doesn't exist
            output_subdir = os.path.dirname(dst_path)
            if not os.path.exists(output_subdir):
                os.makedirs(output_subdir)

            # Move file to output directory
            print(f'Moving {src_path} to {dst_path}...')
            shutil.move(src_path, dst_path)

print('Done!')

