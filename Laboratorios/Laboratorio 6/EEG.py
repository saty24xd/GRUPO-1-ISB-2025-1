import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import welch, butter, firwin, filtfilt

folder = "samples_eeg"
output_folder = "FIR-IIR_eeg"
os.makedirs(output_folder, exist_ok=True)

fs = 1000  # Frecuencia de muestreo en Hz

# Diseño de filtro FIR
fir_order = 101
fir_band = firwin(fir_order, [100, 490], pass_zero=False, fs=fs)

# Diseño de filtro IIR (Butterworth)
iir_order = 4
iir_band = butter(iir_order, [100, 490], btype='bandpass', fs=fs, output='ba')

for filename in os.listdir(folder):
    if filename.endswith(".txt"):
        path = os.path.join(folder, filename)

        # Saltar encabezado
        with open(path, 'r') as f:
            lines = f.readlines()
            skiprows = sum(1 for line in lines if line.startswith("#"))

        try:
            df = pd.read_csv(path, sep="\t", skiprows=skiprows, header=None)

            # Seleccionar señal con más variación
            señal_idx = df.std().idxmax()
            signal = df.iloc[:, señal_idx].values
            tiempo = np.arange(len(signal)) / fs

            # Filtrado FIR
            filtered_fir = filtfilt(fir_band, [1], signal)

            # Filtrado IIR
            b, a = iir_band
            filtered_iir = filtfilt(b, a, signal)

            # Graficar señales filtradas
            for filtro, nombre_filtro, data in zip([filtered_fir, filtered_iir], ["FIR", "IIR"], [filtered_fir, filtered_iir]):
                plt.figure(figsize=(10, 4))
                plt.plot(tiempo, signal, label="Original", alpha=0.5)
                plt.plot(tiempo, data, label=f"Filtrada ({nombre_filtro})", linewidth=1.5)
                plt.title(f"Señal Filtrada ({nombre_filtro}) - {filename}")
                plt.xlabel("Tiempo (s)")
                plt.ylabel("Amplitud (mV)")
                plt.legend()
                plt.grid(True)
                plt.tight_layout()

                out_path_filtered = os.path.join(output_folder, f"{filename[:-4]}_filtered_{nombre_filtro}.png")
                plt.savefig(out_path_filtered)
                plt.close()

            print(f"✅ Filtrado y graficado: {filename}")

        except Exception as e:
            print(f"❌ Error con {filename}: {e}")
