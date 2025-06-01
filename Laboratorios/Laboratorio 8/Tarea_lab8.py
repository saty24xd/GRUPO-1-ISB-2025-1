#!pip install -U neurokit2

import neurokit2 as nk
import numpy as np
import scipy.signal as ss
import matplotlib.pyplot as plt
from scipy import signal

fs = 1000  # Freq de muestreo
duration = 20  # Duración en segundos
scales = [0.2, 0.4, 0.6, 0.8, 0.89, 1.0]  # Escalas a 20, 40, 60, 80 y 100%

symmetry_ratios = []

for escala in scales:
    emg_base = nk.emg_simulate(duration=duration, sampling_rate=fs, burst_number=10, noise=0.01)
    emg_left = emg_base.copy() # canal 1
    emg_right = emg_base * escala # canal 2 derecho escalado
    
    # se limpia cada par
    emg_left_clean = nk.emg_clean(emg_left, sampling_rate=fs) 
    emg_right_clean = nk.emg_clean(emg_right, sampling_rate=fs)
    
    # Extraigo la envolvente de cada par
    amp_left = nk.emg_amplitude(emg_left_clean)
    amp_right = nk.emg_amplitude(emg_right_clean)

    # Calculo el symetry ratio
    rms_izq = np.mean(amp_left)     # RMS proxy = media de la envolvente
    rms_der = np.mean(amp_right)
    symmetry = (min(rms_der, rms_izq) / max(rms_der, rms_izq)) * 100
    symmetry_ratios.append(symmetry)

    fig, axs = plt.subplots(1, 3, figsize=(15, 4))
    # Amplitud EMG – Lado Derecho
    axs[0].plot(amp_right, color='#ff5703')
    axs[0].set_title("Amplitud EMG – Lado Derecho")
    axs[0].set_xlabel("Muestra")
    axs[0].set_ylabel("Amplitud (µV)"); axs[0].grid()
    # Amplitud EMG – Lado Izquierdo
    axs[1].plot(amp_left, color='#337dff')
    axs[1].set_title("Amplitud EMG – Lado Izquierdo")
    axs[1].set_xlabel("Muestra")
    axs[1].set_ylabel("Amplitud (µV)"); axs[1].grid()
    # Comparación de RMS promedio
    axs[2].bar(["Derecho", "Izquierdo"], [rms_der, rms_izq], color=['#ff5703', '#337dff'])
    axs[2].set_title("Comparación de RMS Promedio")
    axs[2].set_ylabel("RMS (µV)"); axs[2].grid()

    fig.suptitle(f"Análisis EMG - Escalamiento del canal derecho: {int(escala*100)}%", fontsize=14); plt.tight_layout(rect=[0, 0, 1, 0.95]) # subtituloss
    plt.show()

    print(f"Simetría bilateral: {symmetry:.1f}%")

scales_pct = [int(s * 100) for s in scales]
umbral = 80 #

plt.figure()
bars = plt.bar(scales_pct, symmetry_ratios, color='#4682B4')  
plt.axhline(umbral, color='red', linestyle='--', linewidth=1.5, label='Umbral 80%') # umbral

plt.title('Symmetry Ratio vs Escalamiento EMG Derecho')
plt.xlabel('Escalamiento Canal Derecho (%)'); plt.ylabel('Symmetry Ratio (%)')
plt.ylim(0, 110); plt.grid(); plt.legend(); plt.tight_layout()

for i, bar in enumerate(bars):
    plt.text(bar.get_x() + bar.get_width()/2, symmetry_ratios[i] + 2,
             f"{symmetry_ratios[i]:.1f}%", ha='center', fontsize=9)

plt.show()

''' A partir de los resultados obtenidos, se observa que el Symmetry Ratio disminuye 
progresivamente a medida que se reduce la amplitud del canal derecho. El umbral del 
80% se supera cuando el canal derecho está escalado por debajo de aproximadamente 89%. 
'''
