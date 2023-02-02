import torch
import numpy as np
from matplotlib import pyplot as plt
from torchHHT import hht, visualization
from scipy.signal import chirp
import IPython
from scipy.signal import stft
from torch import fft
import os
from scipy.signal import stft
from torch import fft

import librosa
import librosa.display
import soundfile as sf
from scipy.io.wavfile import write

img_path = "/Users/dylan/AccentRecognition_Dylan/test_images/"

def downsample(arr, N2):
    N = arr.shape[1]  # width of the array
    M = N // N2   # new width of the downsampled array
    result = np.zeros((arr.shape[0], N2))  # create a new array with the new width
    for i in range(N2):
        result[:, i] = np.sum(arr[:, i*M:(i+1)*M], axis=1)  # take the average of M consecutive elements
    return result


def eval_hht(x,fs): 

    imfs, imfs_env, imfs_freq = hht.hilbert_huang(x, fs, num_imf=3)
    visualization.plot_IMFs(x, imfs, fs, save_fig=img_path+"emd.png" )

    lowest_imf = 0
    highest_imf = 1
    # spectrum, t, f = hht.hilbert_spectrum(imfs_env, imfs_freq, fs, num_data_points=1000, freq_res = 0.1)
    # spectrum, t, f = hht.hilbert_spectrum(imfs_env[lowest_imf:highest_imf+1,:], imfs_freq[lowest_imf:highest_imf+1,:], fs, num_data_points=1000, freq_res = 1)
    # spectrum, t, f = hht.hilbert_spectrum(imfs_env[lowest_imf:highest_imf+1,:], imfs_freq[lowest_imf:highest_imf+1,:], fs, num_data_points=1000, freq_res = 1)
    spectrum, t, f = hht.hilbert_spectrum(imfs_env, imfs_freq, fs, freq_lim=(0,80))

    return spectrum, t, f 
    

def main():

        
    SAMPLE_RATE =  1000  # 22050 / 16000 [Hz]
    # SAMPLE_RATE =  22050  # 22050 / 16000 [Hz]


    # Define and simulate a simple signal
    seconds = 2
    N = seconds*SAMPLE_RATE               
    t = np.linspace(0, seconds, N)
    A1 = 0.7
    A2 = 1
    omega_1 = 1
    omega_2 = 10
    x = A1*np.sin(2*np.pi*omega_1*t) + A2*np.sin(2*np.pi*omega_2*t)

    fs = SAMPLE_RATE
    t = torch.arange(fs*seconds) / fs
    x = torch.from_numpy(chirp(t, 10, 1, 20, method = "quadratic", phi=100)) * torch.exp(-4*(t-1)**2) + \
        torch.from_numpy(chirp(t, 2, 1.5, 10, method = "linear")) * torch.exp(-4*(t-1)**2)
    

    # plt.plot(t, x) 
    # plt.title("$x(t)$")
    # plt.xlabel("time")
    # plt.show()

    audio_file = "/Users/dylan/AccentRecognition_Dylan/audios/_testing/siren.wav"
    y, sr = librosa.load(audio_file, sr=None)

    y = librosa.core.resample(y=y, orig_sr=sr, target_sr=SAMPLE_RATE, scale=True) #resample at defined SAMPLE_RATE

    spectrum, t, f = eval_hht(x,SAMPLE_RATE)


    visualization.plot_HilbertSpectrum(spectrum, t, f, 
                                        save_spectrum=img_path+"Hilbert_spectrum.png", 
                                        save_marginal=img_path+"Hilbert_marginal.png")

    plt.figure(figsize=(20, 4))

    # f, t, Zxx = stft(x, fs, nperseg=1024, noverlap=1023, nfft=1024)
    # f_lim = int(60/f[1])
    # ax = plt.subplot(1, 3, 1)
    # plt.colorbar(ax.pcolormesh(t, f[:f_lim], 20 * np.log10(np.abs(Zxx))[:f_lim, :], shading='auto', cmap = plt.cm.jet),            
    #             label="energy(dB)")
    # ax.set_xlabel("time")
    # ax.set_ylabel("frequency")
    # ax.set_title("(a) Spectrogram (long window)")

    f, t, Zxx = stft(x, fs, nperseg=128, noverlap=127, nfft = 1024)
    f_lim = int(60/f[1])
    ax = plt.subplot(1, 3, 2)
    plt.colorbar(ax.pcolormesh(t, f[:f_lim], 20 * np.log10(np.abs(Zxx))[:f_lim, :], shading='auto', cmap = plt.cm.jet), 
                label="energy(dB)")
    ax.set_xlabel("time")
    ax.set_ylabel("frequency")
    ax.set_title("Spectrogram")

    # X = fft.fft(x)
    # ax = plt.subplot(1, 3, 3)
    # f_lim = int(100/fs*x.shape[0])
    # ax.plot(np.arange(f_lim)/x.shape[0]*fs, 20 * np.log10(np.abs(X))[:f_lim])
    # ax.set_xlim(0, 60)
    # ax.set_xlabel("frequency")
    # ax.set_ylabel("energy (dB)")
    # ax.set_title("(c) marginal spectrum.")
    plt.show()
    
def main2():
    fs = 22050
    duration = 2.0
    t = torch.arange(fs*duration) / fs
    x = torch.from_numpy(chirp(t, 100, 0.8, 200, method = "quadratic", phi=100)) * torch.exp(-4*(t-1)**2) + \
        torch.from_numpy(chirp(t, 800, 1.2, 1000, method = "linear")) * torch.exp(-4*(t-1)**2)

    # sf.write('/Users/dylan/AccentRecognition_Dylan/audios/_testing/chirp.wav', x.numpy(), fs)
    write("/Users/dylan/AccentRecognition_Dylan/audios/_testing/chirp.wav", fs, x.numpy())

    x, fs = librosa.load('/Users/dylan/AccentRecognition_Dylan/audios/_testing/chirp.wav')
    x, fs = librosa.load('/Users/dylan/AccentRecognition_Dylan/audios/_testing/siren.wav')



    # plt.plot(t, x) 
    # plt.title("$x(t)$")
    # plt.xlabel("time")
    # plt.show()
    
    spectrum, t, f =eval_hht(x,fs)

    visualization.plot_HilbertSpectrum(spectrum, t, f, 
                                    save_spectrum=img_path+"Hilbert_spectrum_SUM.png", 
                                    save_marginal=img_path+"Hilbert_marginal.png")

    plt.imshow((spectrum), aspect = 'auto', cmap='inferno')

    spectrum = np.rot90( spectrum.numpy(), k=3, axes=(0, 1))
    plt.imshow((spectrum), aspect = 'auto', cmap='jet')
    plt.show()

    # spectrum = librosa.power_to_db(spectrum)

    # plt.imshow(spectrum, aspect = 'auto', cmap='jet')
    # plt.show()
    spectrum = (downsample(spectrum,230))
    # plt.imshow((new_spectrum), aspect = 'auto', cmap='jet')
    # plt.show()
    # print((new_spectrum))
    spectrum = librosa.feature.melspectrogram(S = spectrum, sr = fs)
    # plt.imshow((new_spectrum2), aspect = 'auto', cmap='jet')
    # plt.show()

    plt.imshow((spectrum), aspect = 'auto', cmap='jet')
    plt.show()


    print("HERE 1st: "+ str(spectrum.shape))

    spectrum = np.abs(librosa.stft(x))**2
    print("HERE: "+ str(spectrum.shape))
    plt.imshow((spectrum), aspect = 'auto', cmap='jet')
    plt.show()
    S = librosa.feature.melspectrogram(S=spectrum, sr=fs)

    fig, ax = plt.subplots()
    S_dB = librosa.power_to_db(S, ref=np.max)
    img = librosa.display.specshow(S_dB, x_axis='time',
                            y_axis='mel', sr=fs,
                            fmax=8000, ax=ax)
    fig.colorbar(img, ax=ax, format='%+2.0f dB')
    ax.set(title='Mel-frequency spectrogram')
    plt.show()



if __name__ == '__main__':
    main()


