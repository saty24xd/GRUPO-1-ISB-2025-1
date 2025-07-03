Avance 2 del Proyecto - Sistema Multimodal de Monitoreo Fatiga Muscular y Estrés Cardiometabólico


1. Introducción

En el contexto del entrenamiento físico, la detección temprana de fatiga muscular y del estrés cardiometabólico es crucial para optimizar el rendimiento y prevenir lesiones. Aunque existen múltiples sistemas de monitoreo en el mercado, la mayoría presentan limitaciones como alto costo, escasa portabilidad o falta de integración entre múltiples fuentes fisiológicas. En particular, el entrenamiento con pesas como el bench press genera una carga muscular significativa sobre el pectoral mayor, que puede ser monitoreada mediante electromiografía de superficie (sEMG). Al mismo tiempo, la carga fisiológica acumulativa puede evaluarse con electrocardiografía (ECG), mediante análisis de la variabilidad de frecuencia cardiaca (HRV), indicador clave de fatiga central y estrés autonómico.

Este proyecto propone un sistema wearable, basado en dispositivos BITalino DiY Signals, para adquirir simultáneamente señales de sEMG y ECG post-ejercicio. Se busca analizar las condiciones fisiológicas del sujeto tras cada set de entrenamiento con el fin de identificar el umbral a partir del cual la recuperación muscular o cardiovascular no es suficiente para continuar el ejercicio de forma segura. Esta información será utilizada para construir un sistema de retroalimentación (biofeedback) en tiempo real.


2. Metodología

2.1. Protocolo de Adquisición

Participantes: Sujetos sanos, entre 20 y 30 años, sin patologías musculares o cardiovasculares previas.

Ejercicio: 5 sets de bench press (8–10 repeticiones) al 65-75% del 1RM.

Electrodos EMG: Posicionados sobre el pectoral mayor derecho (activo y referencia) y tierra sobre el acromion.

Electrodos ECG: Configuración Lead-I modificada (clavícula izquierda y costado derecho).

Adquisición: Posterior a cada set, el participante se recuesta en reposo y se adquieren simultáneamente 15 segundos de EMG y ECG a 1000 Hz.


2.2. Preprocesamiento

Filtros: Pasa banda 20-450 Hz para EMG; 0.5–100 Hz para ECG.

Eliminación de artefactos: Remoción manual de artefactos de movimiento y normalización por sujeto.


2.3. Extracción de Características

EMG: RMS, MAV, ZCR, Mediana de frecuencia (MF), Wavelet Energy.

ECG: HRV (intervalos RR), entropía, LF/HF.


2.4. Generación de Dataset

Se crearán 5 pares EMG/ECG reales.

Se replicarán en Edge Impulse mediante data augmentation (ruido, escalamiento, jitter).

Se etiquetarán tres estados: "Recuperado", "Fatiga Moderada", "Fatiga Alta".


3. Resultados esperados

Se espera que a medida que avanzan los sets:

La amplitud EMG (RMS) disminuya (indicador de fatiga muscular).

La frecuencia mediana de EMG se desplace hacia bajas frecuencias.

En ECG, se observe una reducción de HRV y aumento del índice LF/HF (estrés autonómico).


El sistema integrará ambas vías para predecir si el siguiente set debe realizarse o si el sujeto debe descansar, evitando riesgos por sobreesfuerzo.


4. Avances logrados

Se han adquirido exitosamente las primeras señales piloto con BITalino y se están segmentando en bloques de 15 segundos.

Se ha estandarizado la colocación de electrodos.

Se desarrolló el script en Python para limpieza y exportación compatible con Edge Impulse.


5. Próximas acciones

Finalizar adquisición de las 5 mediciones por sujeto.

Entrenar el modelo en Edge Impulse con las features extraídas.

Evaluar la capacidad predictiva del sistema mediante validación cruzada.

Implementar inferencia local en Raspberry Pi 5.



6. Bibliografía preliminar

[1] De Luca, C. J. (1997). The use of surface electromyography in biomechanics. J Appl Biomech.

[2] Shaffer, F., & Ginsberg, J. P. (2017). An overview of heart rate variability metrics and norms. Front Public Health.

[3] Colomer, C., et al. (2019). Multimodal Deep Learning for Fatigue Detection Using EMG and ECG. Sensors.

[4] Flower Framework for Federated Learning. https://flower.dev

[5] PhysioNet. MIT-BIH Arrhythmia Database. https://physionet.org/content/mitdb/1.0.0/

[6] Edge Impulse Docs. https://docs.edgeimpulse.com/
