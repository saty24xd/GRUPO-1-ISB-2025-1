import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

input_dir = "Proyecto/generated_analysis"

# Configurar estilo de los gráficos
sns.set(style="whitegrid", palette="muted")
plt.rcParams['figure.figsize'] = (14, 8)

# Definir el directorio donde se guardarán las imágenes
output_dir = os.path.join("Proyecto", "generated_analysis")
os.makedirs(output_dir, exist_ok=True)  # Crear directorio si no existe

# Cargar el dataset de características
df_features = pd.read_csv(os.path.join(input_dir, "emg_ecg_features.csv"))

# Verificar y limpiar datos
# Reemplazar valores infinitos con NaN
df_features.replace([np.inf, -np.inf], np.nan, inplace=True)

# Imputar valores NaN con la mediana de cada columna numérica
numeric_cols = df_features.select_dtypes(include=[np.number]).columns
df_features[numeric_cols] = df_features[numeric_cols].fillna(df_features[numeric_cols].median())

# Verificar que Nivel_Esfuerzo tenga los valores esperados
valid_levels = ['bajo', 'medio', 'alto']
df_features = df_features[df_features['Nivel_Esfuerzo'].isin(valid_levels)]

# Lista de características a visualizar (excluyendo ID_sujeto y Nivel_Esfuerzo)
features_to_plot = [
    'ECG_Mean', 'ECG_Std', 'ECG_Skew', 'ECG_Kurtosis', 'ECG_PSD_LF', 'ECG_PSD_HF',
    'HRV_MeanNN', 'HRV_SDNN', 'HRV_RMSSD', 'HRV_LF', 'HRV_HF',
    'EMG_Mean', 'EMG_Std', 'EMG_RMS', 'EMG_Skew', 'EMG_Kurtosis', 'EMG_Median_Freq',
    'HeartRate'
]

# Filtrar características que existen en el dataset
features_to_plot = [f for f in features_to_plot if f in df_features.columns]

# 1. Boxplots para mostrar la distribución de características por nivel de esfuerzo
for feature in features_to_plot:
    plt.figure()
    try:
        sns.boxplot(x='Nivel_Esfuerzo', y=feature, data=df_features, order=valid_levels)
        plt.title(f'Distribución de {feature} por Nivel de Esfuerzo')
        plt.xlabel('Nivel de Esfuerzo')
        plt.ylabel(feature)
        plt.savefig(os.path.join(output_dir, f'boxplot_{feature}.png'))
        plt.close()
    except Exception as e:
        print(f"Error al generar boxplot para {feature}: {e}")
        plt.close()

# 2. Matriz de correlación para explorar relaciones entre características
plt.figure()
correlation_matrix = df_features[features_to_plot].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', square=True)
plt.title('Matriz de Correlación de Características')
plt.savefig(os.path.join(output_dir, 'correlation_matrix.png'))
plt.close()

# 3. Pairplot para visualizar relaciones entre algunas características clave
selected_features = ['HeartRate', 'HRV_RMSSD', 'EMG_RMS', 'EMG_Median_Freq', 'Nivel_Esfuerzo']
selected_features = [f for f in selected_features if f in df_features.columns]
if len(selected_features) > 1:  # Necesitamos al menos 2 características para pairplot
    sns.pairplot(df_features[selected_features], hue='Nivel_Esfuerzo', palette='Set2', diag_kind='kde')
    plt.suptitle('Relaciones entre Características Seleccionadas', y=1.02)
    plt.savefig(os.path.join(output_dir, 'pairplot_features.png'))
    plt.close()

print(f"✅ Gráficos generados y guardados en {output_dir}")