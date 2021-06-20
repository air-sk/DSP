import thinkdsp
import matplotlib.pyplot as plt
from winsound import PlaySound
signal_tri = thinkdsp.SquareSignal(1100)
plt.subplot(211)
signal_tri.plot()
wave = signal_tri.make_wave(duration=5, framerate=10000)
spectrum = wave.make_spectrum()
wave.write("1.wav")
PlaySound("1.wav", flags=8)
plt.subplot(212)
spectrum.plot()
plt.show()

