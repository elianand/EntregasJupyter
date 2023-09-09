from scipy.signal import TransferFunction as tf
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

N = 2

fs_1 = 1
fs_2 = 10
fs_3 = 100

# Calculo de denominador y denominador butter normalizado de orden 2 
num, den = signal.butter(N, 1, analog=True, btype='highpass')


numz_1, denz_1 = signal.bilinear(num, den, fs_1)
numz_2, denz_2 = signal.bilinear(num, den, fs_2)
numz_3, denz_3 = signal.bilinear(num, den, fs_3)



# Transferencia digital
tf_dig_1 = signal.TransferFunction(numz_1, denz_1, dt=1/fs_1)
tf_dig_2 = signal.TransferFunction(numz_2, denz_2, dt=1/fs_2)
tf_dig_3 = signal.TransferFunction(numz_3, denz_3, dt=1/fs_3)


w_1, h_1 = signal.freqz(numz_1, denz_1, worN=5000, fs=fs_1)
w_2, h_2 = signal.freqz(numz_2, denz_2, worN=5000, fs=fs_2)
w_3, h_3 = signal.freqz(numz_3, denz_3, worN=5000, fs=fs_3)
w_analog, h_analog = signal.freqs(num, den, worN=5000)

# Graficar la respuesta en frecuencia (magnitud y fase)
plt.figure(figsize=(8, 6))
plt.subplot(2, 1, 1)
plt.plot(w_1*2*np.pi, 20 * np.log10(np.abs(h_1)))
plt.plot(w_2*2*np.pi, 20 * np.log10(np.abs(h_2)))
plt.plot(w_3*2*np.pi, 20 * np.log10(np.abs(h_3)))
plt.plot(w_analog, 20 * np.log10(np.abs(h_analog)))
plt.legend(['fs=1','fs=10','fs=100', 'Analogico'])
plt.title('Respuesta en Frecuencia')
plt.ylabel('Magnitud (dB)')
plt.xscale("log")
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(w_1*2*np.pi, np.angle(h_1))
plt.plot(w_2*2*np.pi, np.angle(h_2))
plt.plot(w_3*2*np.pi, np.angle(h_3))
plt.plot(w_analog, np.angle(h_analog))
plt.legend(['fs=1','fs=10','fs=100', 'Analogico'])
plt.xlabel('Frecuencia Normalizada (π rad/muestra)')
plt.ylabel('Fase (radianes)')
plt.xscale("log")
plt.grid()

plt.tight_layout()
plt.show()

