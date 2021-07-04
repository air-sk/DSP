import thinkdsp
import numpy as np
from thinkdsp import Chirp, SawtoothSignal, Sinusoid
import math
import matplotlib.pyplot as plt
from winsound import PlaySound


class Sawtoothchirp(Chirp):

    def evaluate(self, ts):
        freqs = np.linspace(self.start, self.end, len(ts))
        dts = np.diff(ts, prepend=0)
        dphis = math.pi * 2 * freqs * dts
        phases = np.cumsum(dphis)
        cycles = phases / (math.pi * 2)
        frac, _ = np.modf(cycles)
        ys = thinkdsp.normalize(thinkdsp.unbias(frac), self.amp)
        return ys


signal = Sawtoothchirp(start=2500, end=3000)
wave = signal.make_wave(duration=1, framerate=20000)
wave.write("2.wav")
PlaySound("2.wav", flags=8)
wave.make_spectrum().plot()
thinkdsp.decorate(xlabel='Frequency (Hz)')
plt.show()
