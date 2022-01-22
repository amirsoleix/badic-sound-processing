from scipy.io import wavfile
import wavio as wv
import numpy as np

def phaseChange(A, file):
    j = complex(0, 1)
    dff = np.fft.fft(file)
    transZ = [0]*len(dff)
    for i in range(len(dff)):
        transZ[i] = ((A + np.exp(i * j)) / (A * np.exp(-i * j) + 1))
    firf = [dff[k] * transZ[k] for k in range(len(dff))]
    return np.fft.ifft(firf)

sr, file = wavfile.read("./musics/phaser_before.wav")
x = phaseChange(0.2, file)
x = phaseChange(0.2, x)
x = phaseChange(0.2, x)
wv.write("./musics/phaser_after.wav", np.abs(x), sr, sampwidth=4)