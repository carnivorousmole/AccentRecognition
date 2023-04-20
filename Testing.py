import os

import cv2
from build_model import extract_features

import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

sr = 22050  # 22050 / 16000 [Hz]
SAMPLE_RATE = sr  # 22050 / 16000 [Hz]

WIN_LENGTH_MS = 25  # ms / 25 # time resolution is 
OVERLAP_MS = 10  # ms / 10

SAMPLE_RATE = 22050  # 22050 / 16000 [Hz]
HOP_LENGTH = int(SAMPLE_RATE * 0.001 * OVERLAP_MS) 

import librosa

def main():

    # creating directory if it doesnt exist
    if not os.path.exists('./test_images'):
        os.makedirs('./test_images')


    for feature in ['mfcc', 'fbe', 'mhfcc', 'hil']:

        # features = extract_features("/Users/dylan/AccentRecognition_Dylan/audios/_testing/siren.wav" ,"mfcc")
        features = extract_features("/Users/dylanwalsh/Code/input/audio_files/audios_word_split_by_numbers2/2/arabic/arabic1.wav"
                                    ,feature)
        # features = extract_features("/Users/dylan/AccentRecognition_Dylan/audios/_testing/chirp.wav")

        # plot the data
        fig, ax = plt.subplots(figsize=(9, 3))

        # features = np.log1p(features)
        # features = features +30 # a 30 dB boost? perhaps equivalent to amplification of sorts
        librosa.display.specshow(features, x_axis='time', y_axis='mel', sr=sr, hop_length=HOP_LENGTH) 
        plt.colorbar(format='%+2.0f dB')
        plt.title('Mel spectrogram')
        plt.xlabel('Time (s)')
        plt.ylabel('Frequency (Hz)')


        plt.savefig('./test_images/extraction_tests/{}_spec.png'.format(feature))


if __name__ == '__main__':
    main()