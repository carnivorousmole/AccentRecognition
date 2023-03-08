from scipy.io import wavfile
import noisereduce as nr
from generatepngs import saveFeaturesToPng

inputFile = '/Users/dylanwalsh/Code/input/audio_files/audios/arabic/arabic1.wav'
# load data
rate, data = wavfile.read(inputFile)
# perform noise reduction
reduced_noise = nr.reduce_noise(y=data, sr=rate)
wavfile.write("mywav_reduced_noise.wav", rate, reduced_noise)

saveFeaturesToPng("mywav_reduced_noise.wav", "mywav_reduced_noise.png")
saveFeaturesToPng(inputFile, "mywav.png")