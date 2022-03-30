import numpy as np
import matplotlib.pyplot as plt
from cmath import exp


def FFT(f):
    N = len(f)
    if N <= 1:
        return f
    even = FFT(f[0::2])
    odd = FFT(f[1::2])
    temp = np.zeros(N).astype(np.complex64)
    for u in range(N // 2):
        temp[u] = even[u] + exp(-2j * np.pi * u / N) * odd[u]
        temp[u + N // 2] = even[u] - exp(-2j * np.pi * u / N) * odd[u]
    return temp


x = np.random.random(16)
print('Własna funkcja FFT:')
print(FFT(x))
print('numpy.fft.fft:')
print(np.fft.fft(x))

samplingFrequency = 128
samplingInterval = 1 / samplingFrequency
time = np.arange(0, 4 * 2 * np.pi, samplingInterval * 2 * np.pi)

sin1 = 5 * np.sin(time)
sin2 = 3 * np.sin(2 * time)
sin3 = 5 * np.sin(5 * time)

sum_of_sin = sin1 + sin2 + sin3

figure, axis = plt.subplots(6, 1)
plt.subplots_adjust(hspace=2)

fft_func = np.fft.fft(sum_of_sin) / len(sum_of_sin)
fft_func = fft_func[range(int(len(sum_of_sin) / 2))]

fft_alg = FFT(sum_of_sin) / len(sum_of_sin)
fft_alg = fft_alg[range(int(len(sum_of_sin) / 2))]

tpCount = len(sum_of_sin)
values = np.arange(int(tpCount / 2))
timePeriod = tpCount / samplingFrequency
frequencies = values / timePeriod

axis[0].set_title('1st sine wave')
axis[0].plot(time, sin1)
axis[0].set_xlabel('Time')
axis[0].set_ylabel('Amplitude')

axis[1].set_title('2nd sine wave')
axis[1].plot(time, sin2)
axis[1].set_xlabel('Time')
axis[1].set_ylabel('Amplitude')

axis[2].set_title('3rd sine wave')
axis[2].plot(time, sin3)
axis[2].set_xlabel('Time')
axis[2].set_ylabel('Amplitude')

axis[3].set_title('Combined sine waves')
axis[3].plot(time, sum_of_sin)
axis[3].set_xlabel('Time')
axis[3].set_ylabel('Amplitude')

axis[4].set_title('Fourier transform with numpy fft function')
axis[4].plot(frequencies, abs(fft_func))
axis[4].set_xlabel('Frequency')
axis[4].set_ylabel('Amplitude')

axis[5].set_title('Fourier transform with own fft algorithm')
axis[5].plot(frequencies, abs(fft_alg))
axis[5].set_xlabel('Frequency')
axis[5].set_ylabel('Amplitude')

plt.show()

"""
fftx = FFT(x) / len(x)
fftx = fftx[range(int(len(x) / 2))]

tpCount = len(x)
values = np.arange(int(tpCount))
timePeriod = tpCount / samplingFrequency
frequenciesx = values / timePeriod

figure, axis = plt.subplots(2, 1)
plt.subplots_adjust(hspace=2)

axis[0].set_title('1')
axis[0].plot(frequenciesx, abs(np.fft.fft(x)))
axis[0].set_xlabel('Frequency')
axis[0].set_ylabel('Amplitude')

axis[1].set_title('2')
axis[1].plot(frequenciesx, abs(FFT(x)))
axis[1].set_xlabel('Frequency')
axis[1].set_ylabel('Amplitude')

plt.show()
"""
