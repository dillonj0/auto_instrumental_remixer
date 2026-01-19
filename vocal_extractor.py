import soundfile as sf
import numpy as np

lyr, lyrr = sf.read('audio/ODESZA_say_my_name.wav')
ins, insr = sf.read('audio/ODESZA_say_my_name_instrumental.wav')

print('lyrical sample rate:', lyrr)
print('lyrical length:', len(lyr))

print('instrumental sample rate:', insr)
print('instrumental length:', len(ins))