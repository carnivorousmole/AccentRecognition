import torch
import numpy as np
from matplotlib import pyplot as plt
from torchHHT import hht, visualization
from scipy.signal import chirp
import IPython
from scipy.signal import stft
from torch import fft
import os

import librosa
import librosa.display

img_path = "/Users/dylan/AccentRecognition_Dylan/Hilbert-Huang-transform/img/"


def eval_hht(x,fs): 
    imfs, imfs_env, imfs_freq = hht.hilbert_huang(x, fs, num_imf=5)
    # visualization.plot_IMFs(x, imfs, fs)
    lowest_imf = 2
    highest_imf = 5
    # spectrum, t, f = hht.hilbert_spectrum(imfs_env[lowest_imf:highest_imf+1,:], imfs_freq[2:,:], fs, time_scale=fs, freq_res = 1)
    spectrum, t, f = hht.hilbert_spectrum(imfs_env[lowest_imf:highest_imf+1,:], imfs_freq[2:,:], fs, num_data_points=1000, freq_res = 1)

    return spectrum, t, f 
    

def main():

        
    SAMPLE_RATE =  22050  # 22050 / 16000 [Hz]

    # Define and simulate a simple signal
    seconds = 5
    N = seconds*SAMPLE_RATE               
    t = np.linspace(0, seconds, N)
    A1 = 0.7
    A2 = 1
    omega_1 = 4000
    omega_2 = 1500
    x = A1*np.sin(2*np.pi*omega_1*t) + A2*np.sin(2*np.pi*omega_2*t)

    audio_file = "/Users/dylan/AccentRecognition_Dylan/audios/_testing/siren.wav"
    y, sr = librosa.load(audio_file, sr=None)
    SAMPLE_RATE =  22050  # 22050 / 16000 [Hz]

    y = librosa.core.resample(y=y, orig_sr=sr, target_sr=SAMPLE_RATE, scale=True) #resample at defined SAMPLE_RATE

    spectrum, t, f = eval_hht(y,SAMPLE_RATE)


    visualization.plot_HilbertSpectrum(spectrum, t, f, 
                                        save_spectrum=img_path+"Hilbert_spectrum.png", 
                                        save_marginal=img_path+"Hilbert_marginal.png")

    # x and t are the signal and time axis


if __name__ == '__main__':
    main()