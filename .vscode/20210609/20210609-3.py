import thinkdsp
import matplotlib.pyplot as plt
from winsound import PlaySound
import numpy as np
signal_tri = thinkdsp.TriangleSignal(440)
plt.subplot(411)
signal_tri.plot()
wave = signal_tri.make_wave(duration=0.01, framerate=10000)
spectrum = wave.make_spectrum()
plt.subplot(412)
spectrum.plot()
print(spectrum.hs[0])
print(np.angle(spectrum.hs[0]))
print(np.abs(spectrum.hs[0]))
spectrum.hs[0] = 100
print(spectrum.hs[0])
print(type(spectrum.hs[0]))
wave = spectrum.make_wave()
plt.subplot(413)
wave.plot()
spectrum = wave.make_spectrum()
plt.subplot(414)
spectrum.plot()
plt.show()

