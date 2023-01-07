import numpy as np
from scipy import ndimage
import emd

import matplotlib.pyplot as plt
import matplotlib.patches as patches


def eval_hht(x ,t, sample_rate):

    # Run a mask sift
    imf = emd.sift.mask_sift(x, max_imfs=5) #TODO how many IMF's? Does this matter?

    # Compute frequency statistics
    IP, IF, IA = emd.spectra.frequency_transform(imf, sample_rate, 'nht')

    #2D transform
    # Carrier frequency histogram definition
    freq_edges, freq_centres = emd.spectra.define_hist_bins(1, 50, 200, 'linear') #Can be Tuned

    # Can limit the IMF's that the hht is calculated for
    f, hht = emd.spectra.hilberthuang(IF, IA, freq_edges, mode='amplitude',sum_time=False)
    time_centres = t[:-1]+1/(2*sample_rate)

    return hht, time_centres, freq_centres

def main():
    # Define and simulate a simple signal
    sample_rate = 256
    seconds = 5
    N = seconds*sample_rate               
    t = np.linspace(0, seconds, N)
    A1 = 0.7
    A2 = 1
    omega_1 = 5
    omega_2 = 20
    # x = A1*np.sin(2*np.pi*omega_1*np.sin(2*np.pi*omega_3*t))+A2*np.sin(2*np.pi*omega_2*t)
    x = A1*np.sin(2*np.pi*omega_1*t) + A2*np.sin(2*np.pi*omega_2*t)

    hht, time_centres, freq_centres = eval_hht(x,t,sample_rate)

    # x and t are the signal and time axis

    emd.plotting.plot_hilberthuang(hht, time_centres, freq_centres,cmap='viridis')
    plt.show()

if __name__ == '__main__':
    main()

def old():

    # Plot the first 5 seconds of data
    plt.figure(figsize=(10, 2))
    plt.plot(t[:5*sample_rate], x[:5*sample_rate], 'k')
    # plt.show()

    # Run a mask sift
    imf = emd.sift.mask_sift(x, max_imfs=5) #TODO how many IMF's? Does this matter?

    # Compute frequency statistics
    IP, IF, IA = emd.spectra.frequency_transform(imf, sample_rate, 'nht')

    emd.plotting.plot_imfs(imf[:5*sample_rate, :])

    #2D transform

    # Carrier frequency histogram definition
    freq_edges, freq_centres = emd.spectra.define_hist_bins(1, 50, 200, 'linear') #Can be Tuned

    f, hht = emd.spectra.hilberthuang(IF, IA, freq_edges, mode='amplitude',sum_time=False)
    # f, hht = emd.spectra.hilberthuang(IF[:, 2, None], IA[:, 2, None], freq_edges, mode='amplitude', sum_time=False)
    time_centres = np.arange(1001)-.5

    plt.figure(figsize=(10, 8))
    # Add signal and IA
    plt.axes([.1, .6, .64, .3])
    plt.plot(imf[:, 2], 'k')
    plt.plot(IA[:, 2], 'r')
    plt.legend(['IMF', 'IF'])
    plt.xlim(50, 150)

    # Add IF axis and legend
    plt.axes([.1, .1, .8, .45])
    plt.plot(IF[:, 2], 'g', linewidth=3)
    plt.legend(['IF'])

    # Plot HHT
    plt.pcolormesh(time_centres, freq_edges, hht[:, :1000], cmap='hot_r', vmin=0)

    # Set colourbar
    cb = plt.colorbar()
    cb.set_label('Amplitude', rotation=90)

    # Add some grid lines
    for ii in range(len(freq_edges)):
        plt.plot((0, 1000), (freq_edges[ii], freq_edges[ii]), 'k', linewidth=.5)
    for ii in range(1000):
        plt.plot((ii, ii), (0, 25), 'k', linewidth=.5)

    # Overlay the IF again for better visualisation
    # plt.plot(IF[:, 2], 'g', linewidth=3)

    # Set lims and labels
    plt.xlim(50, 150)
    plt.ylim(0, 25)
    plt.xlabel('Time (samples)')
    plt.ylabel('Frequency (Hz)')
    plt.rcParams["figure.figsize"] = (20,10)
