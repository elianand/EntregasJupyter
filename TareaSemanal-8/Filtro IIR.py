import numpy as np
import scipy.signal as sig
import matplotlib as mpl
import matplotlib.pyplot as plt

from pytc2.sistemas_lineales import plot_plantilla



ws1 = 0.01 #Hz
wp1 = 0.03 #Hz
wp2 = 0.25 #Hz
ws2 = 0.35 #Hz


ripple = 0.5        # dB
attenuation = 40    # dB

fs = 2



sos = sig.iirdesign([wp1, wp2], [ws1, ws2], ripple, attenuation, analog=False, ftype='butter', output='sos')
w, h = sig.sosfreqz(sos, fs=fs)



plt.figure(1)
plt.cla()

plt.plot(w, 20 * np.log10(np.abs(h)), label='Filtro digital')

plt.title('Plantilla de diseño')
plt.xlabel('Frecuencia normalizada a Nyq [#]')
plt.ylabel('Amplitud [dB]')
plt.grid(which='both', axis='both')

plt.gca().set_xlim([0, 1])

plot_plantilla(filter_type = "bandpass" , fpass = [wp1, wp2], ripple = ripple , fstop = [ws1, ws2], attenuation = attenuation, fs = fs)
