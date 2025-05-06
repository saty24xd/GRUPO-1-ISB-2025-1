import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

folder = "samples"
output_folder = "visualized"
os.makedirs(output_folder, exist_ok=True)

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

            tiempo = np.arange(len(signal)) / 1000  # 1000 Hz
            plt.figure(figsize=(10, 4))
            plt.plot(tiempo, signal, color='blue')
            plt.title(filename)
            plt.xlabel("Tiempo (s)")
            plt.ylabel("Amplitud (mV)")
            plt.grid(True)
            plt.tight_layout()

            out_path = os.path.join(output_folder, f"{filename[:-4]}.png")
            plt.savefig(out_path)
            plt.close()

            print(f"✅ Señal graficada: {filename} → {out_path}")

        except Exception as e:
            print(f"❌ Error con {filename}: {e}")
