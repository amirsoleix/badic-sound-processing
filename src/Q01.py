from scipy.io import wavfile
from scipy import signal
import numpy as np

sr, file = wavfile.read('./musics/noisy.wav')  # Taking in the noisy wav file
fil = signal.firwin(101, [350, 2100], fs=sr, pass_zero=False)
file = signal.lfilter(fil , [1.2], file)
wavfile.write('./test/noise_reduced.wav', sr, file.astype(np.int16))

sr, file = wavfile.read('./musics/encrypted.wav')  # Taking in the encrypted wav file
file = file[::-1]
fil = signal.firwin(101, [650, 750, 1050, 1150], fs=sr, pass_zero=False)
file = signal.lfilter(fil , [1.2], file)
wavfile.write('./test/decrypted.wav', sr, file.astype(np.int16))