import os
from PIL import Image

# update this function to concatenate 3 images instead of 2
def concat_matching_images(input_dir1, input_dir2, output_dir):
    for subdir, dirs, files in os.walk(input_dir1):
        for file in files:
            file_path1 = os.path.join(subdir, file)
            file_path2 = os.path.join(input_dir2, os.path.relpath(file_path1, input_dir1))
            if os.path.isfile(file_path2) and (file_path1.endswith('.jpg') or file_path1.endswith('.jpeg') or file_path1.endswith('.png')):
                try:
                    with Image.open(file_path1) as img1, Image.open(file_path2) as img2:
                        width1, height1 = img1.size
                        width2, height2 = img2.size
                        new_width = max(width1, width2)
                        new_height = height1 + height2
                        new_img = Image.new('RGB', (new_width, new_height))
                        new_img.paste(img1, (0, 0))
                        new_img.paste(img2, (0, height1))
                        out_dir = os.path.join(output_dir, os.path.relpath(subdir, input_dir1))
                        if not os.path.exists(out_dir):
                            os.makedirs(out_dir)
                        out_path = os.path.join(out_dir, file)
                        new_img.save(out_path)
                        print(f"Saved concatenated image to {out_path}")
                except:
                    print(f"Error processing {file_path1}")

input_dir1 = '/Users/dylanwalsh/Code/input/image_files/saved_audio_pngs-grayscale-128mel-0.5s'
input_dir2 = '/Users/dylanwalsh/Code/input/image_files/mel_spec_denoised_nr'
output_dir = '/Users/dylanwalsh/Code/comparison'

concat_matching_images(input_dir1, input_dir2, output_dir)
