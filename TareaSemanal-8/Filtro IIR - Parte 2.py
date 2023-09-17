import numpy as np
import scipy.signal as sig
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.io as sio

from pytc2.sistemas_lineales import plot_plantilla

mat_struct = sio.loadmat('ecg.mat')
ecg_one_lead = mat_struct['ecg_lead']
ecg_one_lead = ecg_one_lead.flatten()
cant_muestras = len(ecg_one_lead)

fig_dpi = 100 # dpi

ws1 = 0.1   #Hz
wp1 = 1     #Hz
wp2 = 25    #Hz
ws2 = 35    #Hz


ripple = 0.1        # dB
attenuation = 20    # dB

fs = 1000 # Hz
nyq_frec = fs / 2


sos = sig.iirdesign(np.array([wp1, wp2]) / nyq_frec, np.array([ws1, ws2]) / nyq_frec, gpass=ripple, gstop=attenuation, analog=False, ftype='butter', output='sos')


ECG_f_win = sig.sosfiltfilt(sos, ecg_one_lead)

# Segmentos de interés
regs_interes = ( 
    [4000, 5500], # muestras
    [10e3, 11e3], # muestras
)

for ii in regs_interes:
    
    # intervalo limitado de 0 a cant_muestras
    zoom_region = np.arange(np.max([0, ii[0]]), np.min([cant_muestras, ii[1]]), dtype='uint')
    
    plt.figure(dpi= fig_dpi, facecolor='w', edgecolor='k')
    plt.plot(zoom_region, ecg_one_lead[zoom_region], label='ECG original', lw=2)
    plt.plot(zoom_region, ECG_f_win[zoom_region], label='ECG filtrado')
    
    plt.title('ECG muestras de ' + str(ii[0]) + ' a ' + str(ii[1]) )
    plt.ylabel('Adimensional')
    plt.xlabel('Muestras (#)')
    
    axes_hdl = plt.gca()
    axes_hdl.legend()
    axes_hdl.set_yticks(())
            
    plt.show()