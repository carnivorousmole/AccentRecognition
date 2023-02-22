import os

import cv2
from build_model import extract_features

import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

def main():

    
    if not os.path.exists('./test_images'):
        os.makedirs('./test_images')

    # features = extract_features("/Users/dylan/AccentRecognition_Dylan/audios/_testing/siren.wav")
    features = extract_features("audios/arabic/arabic1.wav","fbe")
    # features = extract_features("/Users/dylan/AccentRecognition_Dylan/audios/_testing/chirp.wav")

    # Display the array as an image
    print(features[:,0:1000].shape)
    features = features[:,0:500]

    plt.imshow(np.flip(features,axis=0), aspect = 'auto', cmap='jet')
    # plt.savefig('./test_images/'+str(datetime.now())+'.png')
    plt.savefig('./test_images/mainsave.png')


    mel_s_as_int8 = (features*255).astype(np.uint8)
    img_gray = cv2.cvtColor(mel_s_as_int8, cv2.COLOR_GRAY2BGR)
    cv2.imwrite("./test_images/othersave.png", img_gray)

    img = cv2.imread("./test_images/othersave.png", cv2.IMREAD_GRAYSCALE)
    arr = img.astype(np.float32) / 255.0
    plt.imshow(np.flip(arr,axis=0), aspect = 'auto', cmap='jet')
    plt.savefig('./test_images/3save.png')




if __name__ == '__main__':
    main()