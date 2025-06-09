import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pywt

from scipy.stats import skew, kurtosis
from sklearn.decomposition import PCA
import neurokit2 as nk

signals = {
    "ecgS1": ecgS1,
    "ecgS2": ecgS2,
    "ecgS3": ecgS3
}

# Modificar el bucle para añadir features de wavelets
all_features = []

for name, signal in signals.items():
    # DWT: aplicamos una wavelet 
    coeffs = pywt.wavedec(signal, wavelet='db4', level=4)  # 4 niveles: [A4, D4, D3, D2, D1]
    cA4, cD4, cD3, cD2, cD1 = coeffs

    # Extraer estadísticas de los coeficientes
    wavelet_feats = {
        'Mean_cA3': np.mean(cA4),
        'STD_cA3': np.std(cA4),
        'Energy_cA3': np.sum(cA4**2),
        'Skewness_cA3': skew(cA4),
        'Kurtosis_cA3': kurtosis(cA4),

        'Mean_cD4': np.mean(cD4),
        'STD_cD4': np.std(cD4),
        'Energy_cD4': np.sum(cD4**2),
        'Skewness_cD4': skew(cD4),
        'Kurtosis_cD4': kurtosis(cD4),
    }

    # Otras features del dominio temporal
    temporal_feats = {
        'Signal_Type'       : name,
        'Mean'              : np.mean(signal),
        'Median'            : np.median(signal),
        'STD'               : np.std(signal),
        'Skewness'          : skew(signal),
        'Kurtosis'          : kurtosis(signal, fisher=True)
    }

    # Combinar todo
    all_feats = {**temporal_feats, **wavelet_feats}
    all_features.append(pd.DataFrame([all_feats]))

# Unir todo en un solo DataFrame
combined_features_df = pd.concat(all_features, ignore_index=True)
print("=== DataFrame con características extraídas ===")
print(combined_features_df)