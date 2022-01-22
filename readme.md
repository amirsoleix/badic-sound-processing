# Basic Sound Processing  
The project consists of various sections, each one demanding knowledge from a different aspect of basic sound processing. The project is an assignment from **Signals and Systems** course in **Sharif University of Tehcnology**.
## Audio Decryption  
The `scipy` Python library is used to generate different band-pass filters using the `firwin` function. Once the right filter is applied to a noisy audio file it decrypts its message. More about the `firwin` can be found [here](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.firwin.html).  
Apart from the band-pass filters, audio reversal and amplifications are used, too. White noise in the background is reduced using band-stop filters.  
## 3D Effect  
The 3D effect is given to the audio by first reading a mono audio file, then separating left and right channels. Strengthening and weakening the amplitude in each channel produces a 3D effect on the audio, which is best exprienced using head phones. The resulting audio is in `src/musics`.  
## The Echo Effect
To give an echo effect to audio files, instances of recorded voice have to be replayed n times in intervals of t. The amplitude of replays is weakened using an exponential function. In this case the natural logarithm function was used. Parameters n and t can be modified by the user to experience different levels of echo effect. The effect is implemented by manipulating the arrays corresponding to audio amplitude of left and right audio channels.  
## The Phasor Effect  
The [phasor effect](https://en.wikipedia.org/wiki/Phaser_(effect)) as used in C3-PO voice in Star Wars franchise applies an all-pass filter which does not alter the amplitude but modifies the phase of the signal. This gives the audio some sort of artificial feel. The same method is used here to give an artifical feel to a short dialouge. You can find more about the techniques in audio processing used in various applications [here](https://repositorio.upct.es/xmlui/bitstream/handle/10317/8103/tfg-fue-ana.pdf?sequence=1&isAllowed=y).  

P.S. More about the details and results can be found in `report.pdf`.
