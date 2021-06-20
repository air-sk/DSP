import thinkdsp
import matplotlib.pyplot as plt
signal_tri = thinkdsp.TriangleSignal(200)   #产生一个200Hz的三角波
plt.subplot(211)
signal_tri.plot()
wave = signal_tri.make_wave(duration=0.5, framerate=10000)
spectrum = wave.make_spectrum()
plt.subplot(212)
spectrum.plot()
plt.show()

