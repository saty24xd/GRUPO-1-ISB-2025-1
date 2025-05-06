import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import welch

folder = "samples"
output_folder = "visualized"
os.makedirs(output_folder, exist_ok=True)

fs = 1000  # Frecuencia de muestreo (Hz)

for filename in os.listdir(folder):
    if filename.endswith(".txt"):
        path = os.path.join(folder, filename)

        # Saltar líneas del encabezado
        with open(path, 'r') as f:
            lines = f.readlines()
            skiprows = 0
            for line in lines:
                if line.startswith("#"):
                    skiprows += 1
                else:
                    break

        try:
            df = pd.read_csv(path, sep="\t", skiprows=skiprows, header=None)

            # Buscar la columna con más variación (no la de ceros)
            variaciones = df.std()
            señal_idx = variaciones.idxmax()
            signal = df.iloc[:, señal_idx]

            tiempo = np.arange(len(signal)) / fs  # Frecuencia de muestreo en Hz

            # Ploteo de la señal EEG en el dominio del tiempo
            plt.figure(figsize=(10, 4))
            plt.plot(tiempo, signal, color='blue', label="Señal EEG")
            plt.title(f"Señal EEG - {filename}")
            plt.xlabel("Tiempo (s)")
            plt.ylabel("Amplitud (mV)")
            plt.legend()
            plt.grid(True)
            plt.tight_layout()
            
            out_path_signal = os.path.join(output_folder, f"{filename[:-4]}_time.png")
            plt.savefig(out_path_signal)
            plt.close()

            # Cálculo y ploteo de la densidad espectral de potencia (PSD) usando Welch
            f, Pxx_den = welch(signal, fs, nperseg=256)
            plt.figure(figsize=(10, 4))
            plt.semilogy(f, Pxx_den, color='red', label="PSD - Método de Welch")
            plt.title(f"Densidad espectral de potencia - {filename}")
            plt.xlabel("Frecuencia (Hz)")
            plt.ylabel("PSD [V²/Hz]")
            plt.legend()
            plt.grid(True)
            plt.tight_layout()

            out_path_psd = os.path.join(output_folder, f"{filename[:-4]}_psd.png")
            plt.savefig(out_path_psd)
            plt.close()

            print(f"✅ Señal graficada: {filename} → {out_path_signal}")
            print(f"✅ PSD calculado: {filename} → {out_path_psd}")

        except Exception as e:
            print(f"❌ Error con {filename}: {e}")

