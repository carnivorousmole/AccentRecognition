import os

import cv2
from build_model import extract_features

import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

def main():

    # want to save these in an outside directory?
    output_dir = '../saved_audio_pngs'
    # creating directory if it doesnt exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


    # loop through all files in directory and subdirectories
    for root, dirs, files in os.walk("audios"):
        # print the current filename
        for filename in files:
            # print filename
            # if filename contains wav
            if filename.endswith(".wav") and not filename.endswith("_unsilenced.wav"):

                # extract features from the file
                features = extract_features(root + '/' + filename,"fbe")

       

                plt.imshow(np.flip(features,axis=0), aspect = 'auto', cmap='jet')
                # save figure to file, replacing the .wav with .png and saving in the output directory, with the same subdirectory structure
                # create the subdirectory if it doesn't exist
                if not os.path.exists(output_dir + root[6:]):
                    os.makedirs(output_dir + root[6:])
                plt.savefig(output_dir + root[6:] + '/' + filename[:-4] + '.png')

                # # save values of features
                # min =  np.amin(features)
                # max =  np.amax(features)

                # # scale the float array features to 0-255
                # features = (features - min) * 255.0 / (max - min)
                # print("Scaled features:")
                # print("Max: ", np.amax(features))
                # print("Min: ", np.amin(features))

                # np.savetxt("mel_s.csv", features, delimiter=",")
                # mel_s_as_int8 = (features).astype(np.uint8)
        
                # img_gray = cv2.cvtColor(mel_s_as_int8, cv2.COLOR_GRAY2BGR)
                # cv2.imwrite("./test_images/othersave.png", img_gray)

                # img = cv2.imread("./test_images/othersave.png", cv2.IMREAD_GRAYSCALE)
                # # perform reverse scaling to get back to original values
                # arr = (img * (max - min) / 255.0) + min

                # plt.imshow(np.flip(arr,axis=0), aspect = 'auto', cmap='jet')
                # # plt.savefig('./test_images/'+str(datetime.now())+'.png')
                # plt.savefig('./test_images/rereadsave.png')



if __name__ == '__main__':
    main()