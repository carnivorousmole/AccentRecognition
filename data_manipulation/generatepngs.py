import os
import cv2
from build_model import extract_features
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np


def process_audio_files(source_dir, output_dir):
    # creating directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for language in ['english', 'french', 'arabic', 'hindi', 'german']:
        # change the maximum value of i depending on the language
        if language == 'english':
            max = 100
        elif language == 'french':
            max = 63
        elif language == 'arabic':
            max = 100
        elif language == 'hindi':
            max = 18
        elif language == 'german':
            max = 36
        else:
            max = 100

        for i in range(1, max+1):
            filepath =  language + '/' + language + str(i) + ".wav"

            # if filename exists in source directory
            if os.path.exists(source_dir + '/' + filepath):
                # if output file does not already exist
                if not os.path.exists(output_dir  + '/' + filepath[:-4] + '.png'):
                    # save figure to file, replacing the .wav with .png and saving in the output directory, with the same subdirectory structure
                    # create the subdirectory if it doesn't exist
                    if not os.path.exists(output_dir + '/'  + language):
                        os.makedirs(output_dir + '/'  + language)

                    saveFeaturesToPng(source_dir + '/' + filepath, output_dir + '/' + filepath[:-4] + '.png')

                else:
                    print("File already exists: " + output_dir  + '/' + filepath[:-4] + '.png')


def saveFeaturesToPng(inputPath, outputPath):
    # save values of features

    features = extract_features(inputPath,"fbe")

    min = np.amin(features)
    max = np.amax(features)
    # scale the float array features to 0-255
    features = (features - min) * 255.0 / (max - min)
    # convert to int
    mel_s_as_int8 = (features).astype(np.uint8)
    # flip the array for the sake of readability
    mel_s_as_int8 = np.flip(mel_s_as_int8, axis=0)

    img_gray = cv2.cvtColor(mel_s_as_int8, cv2.COLOR_GRAY2BGR)
    cv2.imwrite(outputPath, img_gray)
    # print that this image has been saved
    print("Saved: " + outputPath)


if __name__ == '__main__':

    iteration = 'denoised_nr'
    source_dir = '/Users/dylanwalsh/Code/input/audio_files/' + 'audios_' + iteration
    output_dir = '/Users/dylanwalsh/Code/input/image_files/' + 'mel_spec_' + iteration
    process_audio_files(source_dir, output_dir)
