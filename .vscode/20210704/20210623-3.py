import thinkdsp
import numpy as np
from thinkdsp import Chirp, SawtoothSignal, Sinusoid
import math
import matplotlib.pyplot as plt
from winsound import PlaySound

wave = thinkdsp.read_wave('72475__rockwehrmann__glissup02.wav')
wave.make_spectrogram(512).plot(high=5000)
thinkdsp.decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')
plt.show()
