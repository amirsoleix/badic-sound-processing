from scipy.io import wavfile
from math import sin, cos, pi
import numpy as np

print("Enter the number of echoes and time (in seconds) before each one respectively: ")
n = int(input())
t = int(input())
sr,file = wavfile.read('./musics/3d_before_2.wav')
A = file
const = (2/100)**(1/(n+2)) # If we want to model real world n+2 must be changed to n, situation is exaggerated to enable for clear comparison
for i in range (0, file.size):
  for j in range(0, n):
    if(i+(j+1)*sr*t<file.size/2):
      A[i+(j+1)*sr*t][0]+=int((const**(j+1))*A[i][0])
      A[i+(j+1)*sr*t][1]+=int((const**(j+1))*A[i][1])
wavfile.write('./musics/echo.wav',sr, file.astype(np.int16))
