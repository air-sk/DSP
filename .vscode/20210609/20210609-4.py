import thinkdsp
import matplotlib.pyplot as plt
import numpy as np
def af(spectrum):
    number = np.size(spectrum.hs)
    # print(number)
    for i in range(number):
        if i == 0:
            spectrum.hs[0]=0
        else:
            # print(spectrum.hs[i])
            spectrum.hs[i]=spectrum.hs[i]/spectrum.fs[i]
            # print(spectrum.fs[i])
            # print(spectrum.hs[i])
    return spectrum
signal_tri = thinkdsp.TriangleSignal(200)   #生成一个200Hz的方波
plt.subplot(331)
signal_tri.plot()
wave = signal_tri.make_wave(duration=0.01, framerate=10000)
spectrum = wave.make_spectrum()
plt.subplot(334)
spectrum.plot()
s = af(spectrum)
plt.subplot(337)
s.plot()
signal_squ = thinkdsp.SquareSignal(200)   #生成一个200Hz的三角波
plt.subplot(332)
signal_squ.plot()
wave = signal_squ.make_wave(duration=0.01, framerate=10000)
spectrum = wave.make_spectrum()
plt.subplot(335)
spectrum.plot()
s = af(spectrum)
plt.subplot(338)
s.plot()
signal_saw = thinkdsp.SawtoothSignal(200)   #生成一个200Hz的锯齿波
plt.subplot(333)
signal_saw.plot()
wave = signal_saw.make_wave(duration=0.01, framerate=10000)
spectrum = wave.make_spectrum()
plt.subplot(336)
spectrum.plot()
s = af(spectrum)
plt.subplot(339)
s.plot()

plt.show()


