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


signal = Sawtoothchirp(start=220, end=880)
wave = signal.make_wave(duration=1, framerate=4000)
wave.apodize()
wave.write("1.wav")
PlaySound("1.wav", flags=8)
sp = wave.make_spectrogram(256)
sp.plot()
thinkdsp.decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')
plt.show()

