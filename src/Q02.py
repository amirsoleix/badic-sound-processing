from scipy.io import wavfile
from math import sin, cos, ceil, floor, pi
import numpy as np

# The snippet is used to create mono-tone wav audio file
# sr, file = wavfile.read('./musics/3d_before.wav')
# for x in file:
#     x[1] = x[0] = int(x[0]/2 +x[1]/2)
# wavfile.write('./musics/3d_before.wav', sr, file.astype(np.int16))

print("Enter the percentage(%): ")
n = int(input())

sr,file = wavfile.read('./musics/3d_before.wav')
if n>50:
    if(n==100):
        for x in file:
            x[0] = 0
    else:
        for x in file:
            x[0] = int(((100-n)/n)*x[1])
if n<50:
    if(n==0):
        for x in file:
            x[1] = 0
    else:
        for x in file:
            x[1] = int((n/(100-n))*x[0])
wavfile.write('./musics/3d_after.wav',sr, file.astype(np.int16))

sr, file = wavfile.read('./musics/3d_before.wav')
i = 0
for x in file:
    x[0] = int(abs(sin(i/(sr*10)))*x[0])
    x[1] = int(abs(cos(i/(sr*10)))*x[1])
    i += 1
wavfile.write('./musics/3d_moving.wav',sr, file.astype(np.int16))


sr, file = wavfile.read('./musics/3d_before_2.wav')
i = 0
for x in file:
    x[0] = int(abs(ceil(sin(i/(sr*1.2))))*x[0])
    x[1] = int(abs(floor(sin(i/(sr*1.2))))*x[1])
    i += 1
wavfile.write('./musics/3d_moving_2.wav',sr, file.astype(np.int16))