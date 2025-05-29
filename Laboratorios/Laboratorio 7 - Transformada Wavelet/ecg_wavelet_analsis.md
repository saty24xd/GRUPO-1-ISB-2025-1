# Wavelet-Based ECG Signal Analysis for Human Recognition

Este estudio propone un sistema de identificación biométrica basado en señales ECG (electrocardiograma), usando análisis de wavelets como método principal de procesamiento. Es decir, en lugar de usar huellas dactilares, rostros o iris para identificar a una persona, se utiliza la señal eléctrica que produce su corazón. [1]

## Objetivo del Estudio

El trabajo investiga el uso del ECG como un identificador biométrico confiable, aprovechando su unicidad, dificultad de falsificación y permanencia en el tiempo.  
El procesamiento de la señal ECG se realizó usando técnicas basadas en wavelets para preprocesamiento, extracción de características y clasificación.

---

## Flujo de Procesamiento

1. **Adquisición de datos ECG** de 26 registros desde bases públicas (*MIT-BIH, ECG-ID, etc.*).
2. **Denoising (eliminación de ruido)** usando la **Transformada Wavelet Discreta (DWT)**.
3. **Extracción de características** (energía y potencia) con la **Transformada Wavelet Continua (CWT)**.
4. **Clasificación**:
   - Se midió la **distancia euclidiana** entre firmas (vectores de características) para personas iguales y diferentes.
   - Se aplicó **Análisis Discriminante Lineal (LDA)** para mejorar el reconocimiento.

---

## Uso de Mother Wavelets

### 1. **Daubechies 5 (db5)**

- **Tipo**: Wavelet ortonormal compacta  
- **Orden**: 5 (número de momentos nulos)  
- **Aplicación**: Se utilizó en la etapa de **DWT para eliminar ruido**.  

![image](https://github.com/user-attachments/assets/c561f438-9b94-4345-aa7e-9b78d900af6a)  

**Fig.1**. Efecto *denoising* en la señal ECG [1]  

**Motivo de selección**:  
- Su forma se asemeja al complejo **QRS** del ECG.  
- Permite separar ruido sin deformar la morfología de la señal.  
- Buen equilibrio entre resolución en tiempo y frecuencia.  
- **Ventaja**:  
  - Preserva características clave del ECG mientras elimina artefactos de alta frecuencia [2].  

![image](https://github.com/user-attachments/assets/76d9dfc6-2c01-486f-8ed5-3c3cecb9b3af)  

**Fig.2**. *Mother wavelet* Db5. Elaboración propia.  

### 2. **Morlet (cmor1.5-1.0)**

- **Tipo**: Wavelet compleja de tipo sinusoidal modulada  
- **Parámetros**:  
  - **Ancho de banda**: 1.5  
  - **Frecuencia central**: 1.0  
- **Aplicación**: Se usó en la etapa de **CWT para extracción de características**.  

**Motivo de selección**:  
- Alta resolución tiempo-frecuencia.  
- Capacidad para detectar detalles sutiles y transitorios, tanto en escalas cortas (alta frecuencia) como largas (baja frecuencia).  
- Ideal para generar el **scalogram** (*mapa de energía vs. escala y tiempo*) y espectros de potencia del ECG.  

**Ventaja**:  
- Localiza patrones específicos del ECG en tiempo y frecuencia simultáneamente.  

![image](https://github.com/user-attachments/assets/8a8fd9f2-7556-42b5-ab09-840e7e1a19c4)  

**Fig.3**. *Mother wavelet* Morlet. Elaboración propia.  

---

## Impacto del Orden de la Wavelet

En la señal ECG, el orden de una wavelet afecta qué tan bien detecta ciertas características.  
Se escoge según cómo se quiera representar.  
El orden más bajo detecta bien los detalles finos en poco tiempo (*alta resolución temporal*).  
Mientras que el orden más alto suaviza la señal y puede pasar por alto detalles rápidos (*mejor resolución en frecuencia*).  

De este modo, las recomendaciones generales de uso de las **db wavelets** son [3]:  

| **Objetivo**                     | **Tipo de evento ECG**       | **Recomendación** |
|-----------------------------------|-----------------------------|-------------------|
| Detectar QRS rápido               | Transitorio, agudo          | db2 – db5        |
| Análisis general ECG              | Todo el ciclo P-QRS-T       | db4 – db8        |
| Alta resolución de frecuencia     | Ondas lentas, filtrado suave | db6 – db10       |

El estudio emplea **db5** como un compromiso efectivo: suficientemente precisa para el **QRS** y robusta para limpieza de señal, ofreciendo además un equilibrio entre tiempo y frecuencia.

---

## Resultados

El desempeño experimental del algoritmo de reconocimiento propuesto fue evalu
