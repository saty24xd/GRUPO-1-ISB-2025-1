# **Sistema Multimodal de Diagnóstico Temprano de Fatiga Muscular y Estrés Cardiometabólico con Biofeedback Activo**

## **Introducción**
En el ámbito deportivo, la fatiga muscular y el estrés cardiometabólico representan desafíos críticos. Estos fenómenos no solo limitan el rendimiento, sino que también aumentan el riesgo de lesiones graves. La integración de tecnologías biomédicas como la electromiografía (EMG) y la electrocardiografía (ECG), junto con modelos de inteligencia artificial (IA), permite anticipar estos estados con precisión y actuar de manera preventiva.

Este proyecto propone un sistema **portátil, no invasivo e inteligente** que combina EMG y ECG en tiempo real, utilizando una arquitectura CNN-LSTM con mecanismos de atención y biofeedback háptico. Todo el pipeline corre en edge computing con privacidad garantizada mediante IA federada.

## **Definición de la problemática**
Actualmente, los métodos tradicionales de monitoreo de fatiga y estrés:
- Son invasivos (ej. medición de lactato en sangre).
- Poseen alta variabilidad individual.
- Detectan la fatiga tardíamente.
- No integran señales musculares y cardiacas de forma sincronizada.

El 60% de las lesiones musculares en atletas de alto rendimiento están asociadas a fatiga no detectada, y el 34% sufre alteraciones cardiovasculares por estrés acumulado.

## **Soluciones actuales**
1. **Dispositivos univariados:** Myontec mBody (EMG) y Polar H10 (ECG).
2. **Sistemas de laboratorio:** Delsys Trigno, BIOPAC (alta precisión pero costosos y no portátiles).
3. **IA aplicada por separado:** CNN para EMG y LSTM para HRV, pero sin integración multimodal.
4. **Investigaciones recientes:** uso de ICEEMDAN, HRV no lineal y mecanismos de atención, aunque sin implementación en edge computing portátil.

## **Propuesta de solución**
Desarrollar un sistema multimodal de diagnóstico temprano que integre EMG y ECG, procesados en tiempo real por una arquitectura CNN-LSTM con atención, capaz de anticipar hasta 8 minutos antes eventos críticos como fatiga muscular y estrés cardiometabólico. Este sistema incluye:
- Adquisición sincrónica con BITalino Revolution (1 kHz).
- Procesamiento avanzado con ICEEMDAN y HRV no lineal.
- Clasificación mediante red CNN-LSTM con capa de atención.
- Interfaz visual + biofeedback háptico vía pulsera BLE.
- Ejecución en Raspberry Pi 4 usando TensorFlow Lite + IA federada.

## **Metodología**
### **1. Adquisición de señales**
- **Hardware:** BITalino Revolution.
- **ECG:** Derivación I (3 electrodos Ag/AgCl).
- **EMG:** Electrodos bipolares secos en vientre muscular (ej. cuádriceps).
- **Frecuencia:** 1 kHz.
- **Sincronización:** Señal óptica integrada.

### **2. Procesamiento de señales**
- **EMG:**
  - Filtrado (20–450 Hz).
  - Wavelets (‘db4’, nivel 5) para eliminar artefactos.
  - ICEEMDAN para extracción de modos intrínsecos.
- **ECG:**
  - Filtrado (0.5–40 Hz).
  - Algoritmo Pan-Tompkins para picos R.
  - HRV: SDNN, RMSSD, entropía muestral.

### **3. Modelo de IA híbrido**
- **Entrada:** características fusionadas EMG + ECG.
- **Arquitectura:**
  - CNN 1D para EMG (3 capas, kernels 3x1).
  - LSTM bidireccional para HRV (2 capas, 64 unidades).
  - Atención con 4 cabezas (tipo transformer).
- **Entrenamiento:** datasets MIT-BIH, NINAPRO DB5 y datos propios.
- **Optimización:** AdamW, lr=0.001, regularización L2.

### **4. Validación**
- 15 atletas (edad 25±3) en cicloergómetro incremental.
- Correlación con lactato y cortisol.
- Resultados:
  - Precisión fatiga: **96.2%**
  - Sensibilidad estrés: **94.8%**
  - Anticipación: **8±2 min**
  - Latencia inferencia: 320 ms

### **5. Interfaz de usuario**
- **Framework:** Next.js con componentes visuales adaptativos y gráficos interactivos.
- **Funcionalidad:**
  - Visualización en tiempo real de señales EMG y ECG (RAW y procesadas).
  - Semáforo de riesgo con umbrales personalizados (historial del usuario).
  - Dashboard con métricas resumidas (fatiga, estrés, HRV, frecuencia muscular).
  - Conexión BLE con pulsera vibratoria que emite alertas según nivel de riesgo.
- **Tecnologías adicionales:** Plotly.js (gráficos), TailwindCSS (UI), BLE API (conexión biofeedback).

## **Actividades experimentales**
- Ejercicios propuestos: sentadillas, planchas, curl de bíceps, abdominales.
- Niveles: baja, media y alta intensidad.
- Simultánea adquisición de EMG y ECG.
- Registro de metadatos: edad, sexo, tipo de ejercicio, duración, ubicación sensores.

## **Análisis de señales**
- **EMG:** RMS, MAV, mediana y media de frecuencia.
- **ECG:** Intervalos RR, HRV, índice LF/HF, entropía.
- Transformada Wavelet usada: **Daubechies ‘db4’**.
- Implementación en Python + TensorFlow Lite.

## **Innovaciones clave**
- **ICEEMDAN + atención:** robustez frente a ruido.
- **IA federada:** personalización sin compartir datos.
- **Edge computing:** inferencia local en Raspberry Pi.
- **Costo accesible:** prototipo <$500 (vs. >$5,000 en mercado).

## **Aplicaciones**
- **Deporte:** prevención de lesiones, biofeedback en HIIT.
- **Salud:** detección de miopatías, seguimiento en rehabilitación.

## **Limitaciones y trabajo futuro**
- **Artefactos por sudor:** exploración de electrodos textiles.
- **Generalización a fibras musculares distintas.**
- **Integración de SpO2 (sensor MAX30102).**
- **Despliegue en AWS HealthLake para análisis longitudinal.**

## **Conclusión**
Este sistema representa una **solución pionera, costo-efectiva y portátil** para monitorear el estado fisiológico de atletas en tiempo real. Mediante la fusión de señales biomédicas y modelos de IA interpretables, sienta las bases para un nuevo paradigma de prevención personalizada en salud y deporte.

---

**Equipo de desarrollo:**  
Axel Balboa · Marx Ríos · Álvaro Aquije · André Rubio · Sebastián Torres  
**Fecha:** 2025-1  
**Versión:** 1.0  

---

## **Referencias**
- Enoka RM, Duchateau J. *Muscle fatigue: what, why and how*. J Physiol. 2008.
- Meeusen R, et al. *Overtraining syndrome*. Med Sci Sports Exerc. 2013.
- De Luca CJ. *EMG in biomechanics*. J Appl Biomech.
- Shaffer F, Ginsberg JP. *HRV metrics overview*. Front Public Health. 2017.
- Joyo MK, et al. *Edge Computing for Real-Time Fatigue Detection*. IEEE Sensors J. 2023.
- Ahmed SF, et al. *Muscle Fatigue Detection with EMG*. IEEE ICETAS. 2020.
- Romero C. *Análisis de fatiga muscular con HD-EMG*. Univ. Alicante, 2024.
- Flower Framework. https://flower.dev  
(entre otras, ver anexos para lista completa de papers y patentes)
