import pandas as pd
import numpy as np
import neurokit2 as nk
from scipy.stats import skew, kurtosis
from scipy.signal import welch
from tqdm import tqdm
import os

# Cargar el dataset
input_dir = "Proyecto/generated_data"
df = pd.read_csv(os.path.join(input_dir, "dataset_sintetico_emg_ecg.csv"))

output_dir = "Proyecto/generated_analysis"
os.makedirs(output_dir, exist_ok=True)  # Crear directorio si no existe

# Parámetros
sampling_rate = 1000  # Hz
window_size = 10 * sampling_rate  # 10 segundos de datos por segmento

# Función para extraer características de ECG
def extract_ecg_features(ecg_signal, fs):
    try:
        # Procesar señal ECG
        ecg_cleaned = nk.ecg_clean(ecg_signal, sampling_rate=fs)
        rpeaks = nk.ecg_peaks(ecg_cleaned, sampling_rate=fs)[1]['ECG_R_Peaks']
        hrv_features = nk.hrv(rpeaks, sampling_rate=fs)
        
        # Características temporales
        ecg_mean = np.mean(ecg_signal)
        ecg_std = np.std(ecg_signal)
        ecg_skew = skew(ecg_signal)
        ecg_kurt = kurtosis(ecg_signal)
        
        # Características de frecuencia (PSD)
        freqs, psd = welch(ecg_signal, fs=fs, nperseg=fs*2)
        psd_total = np.sum(psd)
        psd_lf = np.sum(psd[(freqs >= 0.04) & (freqs < 0.15)]) / psd_total
        psd_hf = np.sum(psd[(freqs >= 0.15) & (freqs < 0.4)]) / psd_total
        
        # Seleccionar métricas HRV relevantes
        hrv_metrics = {
            'HRV_MeanNN': hrv_features['HRV_MeanNN'].iloc[0] if not hrv_features.empty else np.nan,
            'HRV_SDNN': hrv_features['HRV_SDNN'].iloc[0] if not hrv_features.empty else np.nan,
            'HRV_RMSSD': hrv_features['HRV_RMSSD'].iloc[0] if not hrv_features.empty else np.nan,
            'HRV_LF': hrv_features['HRV_LF'].iloc[0] if not hrv_features.empty else np.nan,
            'HRV_HF': hrv_features['HRV_HF'].iloc[0] if not hrv_features.empty else np.nan
        }
        
        return {
            'ECG_Mean': ecg_mean,
            'ECG_Std': ecg_std,
            'ECG_Skew': ecg_skew,
            'ECG_Kurtosis': ecg_kurt,
            'ECG_PSD_LF': psd_lf,
            'ECG_PSD_HF': psd_hf,
            **hrv_metrics
        }
    except Exception as e:
        print(f"Error procesando ECG: {e}")
        return {key: np.nan for key in [
            'ECG_Mean', 'ECG_Std', 'ECG_Skew', 'ECG_Kurtosis', 
            'ECG_PSD_LF', 'ECG_PSD_HF', 'HRV_MeanNN', 'HRV_SDNN', 
            'HRV_RMSSD', 'HRV_LF', 'HRV_HF'
        ]}

# Función para extraer características de EMG
def extract_emg_features(emg_signal, fs):
    try:
        # Procesar señal EMG
        emg_cleaned = nk.emg_clean(emg_signal, sampling_rate=fs)
        emg_amplitude = nk.emg_amplitude(emg_cleaned)
        
        # Características temporales
        emg_mean = np.mean(emg_amplitude)
        emg_std = np.std(emg_amplitude)
        emg_rms = np.sqrt(np.mean(emg_amplitude**2))
        emg_skew = skew(emg_amplitude)
        emg_kurt = kurtosis(emg_amplitude)
        
        # Características de frecuencia (PSD)
        freqs, psd = welch(emg_amplitude, fs=fs, nperseg=fs*2)
        psd_total = np.sum(psd)
        psd_median_freq = freqs[np.where(np.cumsum(psd) >= psd_total/2)[0][0]]
        
        return {
            'EMG_Mean': emg_mean,
            'EMG_Std': emg_std,
            'EMG_RMS': emg_rms,
            'EMG_Skew': emg_skew,
            'EMG_Kurtosis': emg_kurt,
            'EMG_Median_Freq': psd_median_freq
        }
    except Exception as e:
        print(f"Error procesando EMG: {e}")
        return {key: np.nan for key in [
            'EMG_Mean', 'EMG_Std', 'EMG_RMS', 'EMG_Skew', 
            'EMG_Kurtosis', 'EMG_Median_Freq'
        ]}

# Extraer características por sujeto y segmento
features_list = []

unique_subjects = df['ID_sujeto'].unique()
for subject in tqdm(unique_subjects, desc="Procesando sujetos"):
    subject_data = df[df['ID_sujeto'] == subject]
    
    ecg_signal = subject_data['ECG_raw'].values
    emg_signal = subject_data['EMG_raw'].values
    nivel_esfuerzo = subject_data['Nivel_Esfuerzo'].iloc[0]
    heart_rate = subject_data['HeartRate'].iloc[0]
    
    # Extraer características
    ecg_features = extract_ecg_features(ecg_signal, sampling_rate)
    emg_features = extract_emg_features(emg_signal, sampling_rate)
    
    # Combinar características
    features = {
        'ID_sujeto': subject,
        'Nivel_Esfuerzo': nivel_esfuerzo,
        'HeartRate': heart_rate,
        **ecg_features,
        **emg_features
    }
    
    features_list.append(features)

# Crear DataFrame con características
features_df = pd.DataFrame(features_list)

# Guardar resultados
features_df.to_csv(os.path.join(output_dir, "emg_ecg_features.csv"), index=False)
print("✅ Características extraídas y guardadas en 'emg_ecg_features.csv'")