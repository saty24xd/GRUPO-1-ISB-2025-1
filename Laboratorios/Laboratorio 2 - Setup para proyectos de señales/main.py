import neurokit2 as nk
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq

def plot_fft(signal, sampling_rate, title):
    N = len(signal)
    yf = fft(signal)
    xf = fftfreq(N, 1 / sampling_rate)[:N // 2]
    plt.plot(xf, 2.0/N * np.abs(yf[0:N // 2]))
    plt.title(title + " - Dominio de la frecuencia")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Amplitud")
    plt.grid(True)

emg1 = nk.emg_simulate(duration=10, sampling_rate=1000, burst_number=4)
emg2 = nk.emg_simulate(duration=10, sampling_rate=1000, burst_number=6, noise=0.05)
ecg1 = nk.ecg_simulate(duration=10, sampling_rate=1000, heart_rate=70)
ecg2 = nk.ecg_simulate(duration=10, sampling_rate=1000, heart_rate=85, noise=0.01)

plt.figure(figsize=(12, 8))
plt.subplot(4, 1, 1)
plt.plot(emg1)
plt.title("EMG 1 - Dominio del tiempo")
plt.subplot(4, 1, 2)
plt.plot(emg2)
plt.title("EMG 2 - Dominio del tiempo")
plt.subplot(4, 1, 3)
plt.plot(ecg1)
plt.title("ECG 1 - Dominio del tiempo")
plt.subplot(4, 1, 4)
plt.plot(ecg2)
plt.title("ECG 2 - Dominio del tiempo")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 8))
plt.subplot(4, 1, 1)
plot_fft(emg1, 1000, "EMG 1")
plt.subplot(4, 1, 2)
plot_fft(emg2, 1000, "EMG 2")
plt.subplot(4, 1, 3)
plot_fft(ecg1, 1000, "ECG 1")
plt.subplot(4, 1, 4)
plot_fft(ecg2, 1000, "ECG 2")
plt.tight_layout()
plt.show()
