import os
from PIL import Image
import numpy as np

def crop_images_in_directory(input_dir, output_dir, crop_size):
    image_dict = {}
    for subdir, dirs, files in os.walk(input_dir):
        for file in files:
            file_path = os.path.join(subdir, file)
            if file_path.endswith('.jpg') or file_path.endswith('.jpeg') or file_path.endswith('.png'):
                try:
                    with Image.open(file_path) as img:
                        width, height = img.size
                        if width >= crop_size[0] and height >= crop_size[1]:
                            crop_coords = (80, 0, crop_size[0], crop_size[1])
                            img = img.crop(crop_coords)
                            # Convert image to NumPy array
                            img_array = np.array(img)
                            # Check if the image array is already in the dictionary (i.e., if the image is a duplicate)
                            if file_path in image_dict or any(np.array_equal(img_array, image_array) for image_array in image_dict.values()):
                                print(f"Skipping duplicate image: {file_path}")
                            else:
                                image_dict[file_path] = img_array
                                out_dir = os.path.join(output_dir, os.path.relpath(subdir, input_dir))
                                if not os.path.exists(out_dir):
                                    os.makedirs(out_dir)
                                out_path = os.path.join(out_dir, file)
                                img.save(out_path)
                                print(f"Saved cropped image to {out_path}")
                        else:
                            print(f"Skipping small image: {file_path}")
                except:
                    print(f"Error processing {file_path}")

                    
# Example usage
input_dir = '/Users/dylanwalsh/Code/input/image_files/accent-data/arabic'
output_dir =  '/Users/dylanwalsh/Code/input/image_files/accent-data-cropped2/arabic'
crop_size = (300, 400) # crop size in pixels
crop_images_in_directory(input_dir, output_dir, crop_size)
