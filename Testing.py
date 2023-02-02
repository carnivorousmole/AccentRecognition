from build_model import extract_features

import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

def main():
    # features = extract_features("/Users/dylan/AccentRecognition_Dylan/audios/_testing/siren.wav")
    features = extract_features("/Users/dylan/AccentRecognition_Dylan/audios/arabic/arabic200.wav")
    # features = extract_features("/Users/dylan/AccentRecognition_Dylan/audios/_testing/chirp.wav")

    # Display the array as an image
    print(features[:,0:1000].shape)
    features = features[:,0:500]
    plt.imshow(np.flip(features,axis=0), aspect = 'auto', cmap='jet')
    plt.savefig('./test_images_2/'+str(datetime.now())+'.png')
    # plt.show()


if __name__ == '__main__':
    main()