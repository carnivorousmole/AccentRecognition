import os

import cv2
from build_model import extract_features

import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

def main():

    # creating directory if it doesnt exist
    if not os.path.exists('./test_images'):
        os.makedirs('./test_images')

    # features = extract_features("/Users/dylan/AccentRecognition_Dylan/audios/_testing/siren.wav")
    features = extract_features("audios/arabic/arabic1.wav","fbe")
    # features = extract_features("/Users/dylan/AccentRecognition_Dylan/audios/_testing/chirp.wav")

    # shorten to a number of samples
    features = features[:,0:500] 
    # print min and max values of features array verbosely
    print("Original features:")
    print("Max: ", np.amax(features))
    print("Min: ", np.amin(features))


    
    
    # save values of features
    min =  np.amin(features)
    max =  np.amax(features)


    plt.imshow(np.flip(features,axis=0), aspect = 'auto', cmap='jet')
    # plt.savefig('./test_images/'+str(datetime.now())+'.png')
    plt.savefig('./test_images/mainsave.png')

    # scale the float array features to 0-255
    features = (features - min) * 255.0 / (max - min)
    print("Scaled features:")
    print("Max: ", np.amax(features))
    print("Min: ", np.amin(features))

    np.savetxt("mel_s.csv", features, delimiter=",")
    mel_s_as_int8 = (features).astype(np.uint8)
    print("Int features:")
    print("Max: ", np.amax(mel_s_as_int8))
    print("Min: ", np.amin(mel_s_as_int8))


    img_gray = cv2.cvtColor(mel_s_as_int8, cv2.COLOR_GRAY2BGR)
    cv2.imwrite("./test_images/othersave.png", img_gray)

    img = cv2.imread("./test_images/othersave.png", cv2.IMREAD_GRAYSCALE)
    # perform reverse scaling to get back to original values
    arr = (img * (max - min) / 255.0) + min
    print("re-read features:")
    print("Max: ", np.amax(arr))
    print("Min: ", np.amin(arr))
    plt.imshow(np.flip(arr,axis=0), aspect = 'auto', cmap='jet')
    # plt.savefig('./test_images/'+str(datetime.now())+'.png')
    plt.savefig('./test_images/rereadsave.png')



if __name__ == '__main__':
    main()