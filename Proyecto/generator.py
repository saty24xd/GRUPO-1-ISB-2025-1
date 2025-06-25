import neurokit2 as nk
emg_signal = nk.emg_simulate(duration=10, sampling_rate=1000)
ecg_signal = nk.ecg_simulate(duration=10, sampling_rate=1000)
import os
import pandas as pd
import numpy as np
import random

# Parámetros
n_samples = 100
duration = 10  # segundos
sampling_rate = 1000  # Hz

data = []

output_dir = os.path.join("Proyecto", "generated_data")
os.makedirs(output_dir, exist_ok=True)  # Crear directorio si no existe

def simulate_signals(level):
    heart_rate = random.randint(60, 90) if level == 'bajo' else \
                 random.randint(90, 130) if level == 'medio' else \
                 random.randint(130, 160)

    ecg = nk.ecg_simulate(duration=duration, sampling_rate=sampling_rate, heart_rate=heart_rate)

    emg = nk.emg_simulate(duration=duration, sampling_rate=sampling_rate)
    noise = 0.01 if level == 'bajo' else 0.05 if level == 'medio' else 0.1
    emg += np.random.normal(0, noise, size=len(emg)) * (1 if level == 'bajo' else 1.5 if level == 'medio' else 2)

    return ecg, emg, heart_rate

for i in range(n_samples):
    nivel = random.choice(['bajo', 'medio', 'alto'])
    sujeto_id = f"S{i:03d}"
    ejercicio = 'press_banca'

    ecg, emg, hr = simulate_signals(nivel)

    df = pd.DataFrame({
        'Timestamp': np.linspace(0, duration, int(sampling_rate * duration)),
        'ECG_raw': ecg,
        'EMG_raw': emg,
        'HeartRate': hr,
        'Nivel_Esfuerzo': nivel,
        'Ejercicio': ejercicio,
        'ID_sujeto': sujeto_id
    })

    data.append(df)

dataset = pd.concat(data, ignore_index=True)
dataset.to_csv(os.path.join(output_dir, "dataset_sintetico_emg_ecg.csv"), index=False)
print("✅ Dataset generado y guardado como 'dataset_sintetico_emg_ecg.csv'")

