from build_model import extract_features

import matplotlib.pyplot as plt



def main():
    features = extract_features("/Users/dylan/AccentRecognition/audios/arabic/arabic1.wav")
    # Display the array as an image
    plt.imshow(features, aspect = 'auto', cmap='jet')
    plt.show()


if __name__ == '__main__':
    main()