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

def signal(t):
    return 5 * np.sin(t) + 3 * np.sin(2 * t) + 5 * np.sin(5 * t)

def define_data(n=128):
    data = []
    for i in range(n):
        data.append(signal(i))
    return np.array(data)

def remove_frequency(data, freq=0.9):
    for i in range(len(data)):
        if data[i] > freq:
            data[i] = 0
    return data

data = define_data()

plt.plot(data, color='orange', label='przed fft')
data = FFT(data)

for i in range(len(data)):
    data[i] = data[i]*(1-np.cos((2*np.pi*(i))/(len(data)-1)))/2

#plt.plot(data, color='orange', label='FFT')

data = remove_frequency(data)
#plt.plot(data, color='black', label='Removed frequency')

data = np.fft.ifft(data)
plt.plot(data, color='red', label='IFFT')

plt.legend()
plt.show()
