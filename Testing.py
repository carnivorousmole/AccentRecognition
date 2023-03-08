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

    # features = extract_features("/Users/dylan/AccentRecognition_Dylan/audios/_testing/siren.wav")
    features = extract_features("audios/french/french63.wav","fbe")
    # features = extract_features("/Users/dylan/AccentRecognition_Dylan/audios/_testing/chirp.wav")

     # plot the datav
    fig, ax = plt.subplots(figsize=(9, 3))

    features = np.log1p(features)
    # features = features +30 # a 30 dB boost? perhaps equivalent to amplification of sorts
    librosa.display.specshow(features, x_axis='time', y_axis='mel', sr=sr, hop_length=HOP_LENGTH) 
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel spectrogram')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')


    plt.savefig('./test_images/spec_save.png')




    
    










    # # save values of features
    # min =  np.amin(features)
    # max =  np.amax(features)
    
    #   # plot the data
    # fig, ax = plt.subplots()
    # im = ax.imshow(np.flip(features,axis=0), aspect='auto', cmap='bwr')

    # # add a color bar
    # cbar = ax.figure.colorbar(im, ax=ax)

    # # set the label for the color bar
    # cbar.ax.set_ylabel('Color Scale', rotation=-90, va="bottom")

    # plt.savefig('./test_images/mainsave.png')

    # # scale the float array features to 0-255
    # features = (features - min) * 255.0 / (max - min)
    # print("Scaled features:")
    # print("Max: ", np.amax(features))
    # print("Min: ", np.amin(features))

    # np.savetxt("mel_s.csv", features, delimiter=",")
    # mel_s_as_int8 = (features).astype(np.uint8)
    # print("Int features:")
    # print("Max: ", np.amax(mel_s_as_int8))
    # print("Min: ", np.amin(mel_s_as_int8))


    # img_gray = cv2.cvtColor(mel_s_as_int8, cv2.COLOR_GRAY2BGR)
    # cv2.imwrite("./test_images/othersave.png", img_gray)

    # img = cv2.imread("./test_images/othersave.png", cv2.IMREAD_GRAYSCALE)
    # # perform reverse scaling to get back to original values
    # arr = (img * (max - min) / 255.0) + min
    # print("re-read features:")
    # print("Max: ", np.amax(arr))
    # print("Min: ", np.amin(arr))
    # plt.imshow(np.flip(arr,axis=0), aspect = 'auto', cmap='bwr')
    # # plt.savefig('./test_images/'+str(datetime.now())+'.png')
    # plt.savefig('./test_images/rereadsave.png')



if __name__ == '__main__':
    main()