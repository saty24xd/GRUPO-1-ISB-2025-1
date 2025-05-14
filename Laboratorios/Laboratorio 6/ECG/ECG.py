import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, bessel, firwin, filtfilt

# Carpeta de entrada y salida
folder = "ECG_samples"  
output_folder = "FIR-IIR_ecg"
os.makedirs(output_folder, exist_ok=True)

# Parámetros
fs = 1000  # Frecuencia de muestreo
fc = 40   # Frecuencia de corte en Hz
wn = fc / (fs / 2)  # Frecuencia normalizada

# Diseño de filtros
iir_order = 4
fir_order_hamming = 101
fir_order_blackman = 151

# FIR (ventanas)
fir_hamming = firwin(fir_order_hamming, wn, window='hamming', fs=fs)
fir_blackman = firwin(fir_order_blackman, wn, window='blackman', fs=fs)

# IIR
b_butter, a_butter = butter(iir_order, wn, btype='low', fs=fs)
b_bessel, a_bessel = bessel(iir_order, wn, btype='low', fs=fs, norm='phase')

# Procesamiento de archivos
for filename in os.listdir(folder):
    if filename.endswith(".txt"):
        path = os.path.join(folder, filename)

        # Detectar líneas de encabezado
        with open(path, 'r') as f:
            lines = f.readlines()
            skiprows = sum(1 for line in lines if line.startswith("#"))

        try:
            df = pd.read_csv(path, sep="\t", skiprows=skiprows, header=None)

            # Seleccionar la columna más significativa
            signal_idx = df.std().idxmax()
            signal = df.iloc[:, signal_idx].values
            time = np.arange(len(signal)) / fs

            # Aplicar filtros
            filtered = {
                "butter": filtfilt(b_butter, a_butter, signal),
                "bessel": filtfilt(b_bessel, a_bessel, signal),
                "hamming": filtfilt(fir_hamming, [1], signal),
                "blackman": filtfilt(fir_blackman, [1], signal),
            }

            # Guardar señales y gráficas
            for key, sig_filt in filtered.items():
                # Graficar
                plt.figure(figsize=(10, 4))
                plt.plot(time, signal, label="Original", alpha=0.4)
                plt.plot(time, sig_filt, label=f"Filtrado ({key})", linewidth=1.5)
                plt.title(f"{filename} - Filtro {key.capitalize()}")
                plt.xlabel("Tiempo (s)")
                plt.ylabel("Amplitud")
                plt.legend()
                plt.grid(True)
                plt.tight_layout()

                # Guardar gráfica
                img_path = os.path.join(output_folder, f"{filename[:-4]}_{key}.png")
                plt.savefig(img_path)
                plt.close()

                # Guardar señal filtrada
                csv_path = os.path.join(output_folder, f"{filename[:-4]}_{key}.csv")
                pd.DataFrame(sig_filt).to_csv(csv_path, index=False, header=False)

            print(f"✅ Procesado: {filename}")

        except Exception as e:
            print(f"❌ Error en {filename}: {e}")
