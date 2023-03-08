import os
import librosa
import soundfile as sf
import numpy as np
from scipy.signal import wiener

from scipy.io import wavfile
import noisereduce as nr
from data_manipulation.generatepngs import saveFeaturesToPng

def denoise_wav(input_path, output_path):
    # Load audio file
    print(f'Loading {input_path}...')
    rate, data = wavfile.read(input_path)
    # perform noise reduction
    reduced_noise = nr.reduce_noise(y=data, sr=rate)
    wavfile.write(output_path, rate, reduced_noise)

    print(f'Denoised {input_path} to {output_path}...')

# Set source and output directories
source_dir = '/Users/dylanwalsh/Code/input/audio_files/audios_subset'
output_dir = '/Users/dylanwalsh/Code/input/audio_files/audios_denoised_nr'

# Loop through all directories and files in source directory
for root, dirs, files in os.walk(source_dir):
    for file in files:
        if file.endswith('.wav'):
            input_path = os.path.join(root, file)

            # Create output directory if it doesn't exist
            output_subdir = root.replace(source_dir, output_dir)
            if not os.path.exists(output_subdir):
                os.makedirs(output_subdir)

            output_path = os.path.join(output_subdir, file)

            # Apply denoising using spectral subtraction
            print(f'Denoising {input_path}...')
            # y_denoised = librosa.effects.denoise_wavelet(y, wavelet=wavelet, mode=mode)
            denoise_wav(input_path, output_path)

            # y_denoised = librosa.decompose.nn_filter(y, aggregate=np.median, metric='cosine', width=int(librosa.time_to_samples(0.025, sr=sr)))
            # y_denoised -= 0.5 * librosa.decompose.nn_filter(y_denoised, aggregate=np.median, metric='cosine', width=int(librosa.time_to_samples(0.25, sr=sr)))





print('Done!')
