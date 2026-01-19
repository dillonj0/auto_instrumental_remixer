import soundfile as sf
import numpy as np

print('Importing audio...')
lyr, lyrr = sf.read('audio/ODESZA_say_my_name.wav')
ins, insr = sf.read('audio/ODESZA_say_my_name_instrumental.wav')

print('\tlyrical sample rate:', lyrr)
print('\tlyrical length:', len(lyr))

print('\tinstrumental sample rate:', insr)
print('\tinstrumental length:', len(ins))

print('Performing DFT...')
Lyr = np.fft.fft(lyr)
Ins = np.fft.fft(ins)

print('Isolating lyrics...')
L_only = Lyr - Ins # Only the lyrics should remain
l_only = np.fft.ifft(L_only)
l_only_real = np.real(l_only) # .wav has to be real-valued

print('Writing lyrics-only file...')
sf.write('audio/lyrics_only.wav', l_only_real, lyrr)