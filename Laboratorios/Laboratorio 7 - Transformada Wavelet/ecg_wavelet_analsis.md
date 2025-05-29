# Wavelet-Based ECG Signal Analysis for Human Recognition

Este estudio propone un sistema de identificación biométrica basado en señales ECG (electrocardiograma), usando análisis de wavelets como método principal de procesamiento. Es decir, en lugar de usar huellas dactilares, rostros o iris para identificar a una persona, se utiliza la señal eléctrica que produce su corazón.[1]

## Objetivo del Estudio

El trabajo investiga el uso del ECG como un identificador biométrico confiable, aprovechando su unicidad, dificultad de falsificación y permanencia en el tiempo. 
El procesamiento de la señal ECG. Para esto se uso técnicas basadas en wavelets para preprocesamiento y para extracción de características y clasificación.

---

## Flujo de Procesamiento

1. **Adquisición de datos ECG** de 26 registros desde bases públicas (MIT-BIH, ECG-ID, etc.).
2. **Denoising (eliminación de ruido)** usando la **Transformada Wavelet Discreta (DWT)**.
3. **Extracción de características** (energía y potencia) con la **Transformada Wavelet Continua (CWT)**.
4. **Clasificación** :
   - Se midió la **distancia euclidiana** entre firmas (vectores de características) para personas iguales y diferentes.
   - Se aplicó **Análisis Discriminante Lineal (LDA)** para mejorar el reconocimiento.

---

## Uso de Mother Wavelets

### 1. **Daubechies 5 (db5)**

- **Tipo**: Wavelet ortonormal compacta
- **Orden**: 5 (número de momentos nulos)
- **Aplicación**: Se utilizó en la etapa de **DWT para eliminar ruido**.
![image](https://github.com/user-attachments/assets/c561f438-9b94-4345-aa7e-9b78d900af6a)
Fig.1. Efecto denoising en la señal ECG [1]
- **Motivo de selección**:
  - Su forma se asemeja al complejo **QRS** del ECG.
  - Permite separar ruido sin deformar la morfología de la señal.
  - Buen equilibrio entre resolución en tiempo y frecuencia.
- **Ventaja**:
  - Preserva características clave del ECG mientras elimina artefactos de alta frecuencia[2].
![image](https://github.com/user-attachments/assets/76d9dfc6-2c01-486f-8ed5-3c3cecb9b3af)
Fig.2. Mother wavelet Db5. Elaboracion propia.
### 2. **Morlet (cmor1.5-1.0)**

- **Tipo**: Wavelet compleja de tipo sinusoidal modulada
- **Parámetros**: 
  - Ancho de banda: 1.5
  - Frecuencia central: 1.0
- **Aplicación**: Se usó en la etapa de **CWT para extracción de características**.
- **Motivo de selección**:
  - Alta resolución tiempo-frecuencia.
  - Capacidad para detectar detalles sutiles y transitorios, tanto en escalas cortas (alta frecuencia) como largas (baja frecuencia).
  - Ideal para generar el **scalogram**(mapa de energía vs. escala y tiempo) y espectros de potencia del ECG.
- **Ventaja**:
  - Localiza patrones específicos del ECG en tiempo y frecuencia simultáneamente.
![image](https://github.com/user-attachments/assets/8a8fd9f2-7556-42b5-ab09-840e7e1a19c4)
Fig.3. Mother wavelet Morlet. Elaboracion propia.
---

## Impacto del Orden de la Wavelet

En la señal ECG, el orden de una wavelet afecta qué tan bien detecta ciertas características. Se escoge segun como se quiera representar. El orden más bajo detecta bien los detalles finos en poco tiempo (alta resolución temporal). Mientras que el orden más alto suaviza la señal y puede pasar por alto detalles rápidos (mejor resolución en frecuencia). De este modo las recomendaciones generales de uso de las db wavalets son [3]:

| Objetivo                      | Tipo de evento ECG           | Recomendación |
| ----------------------------- | ---------------------------- | ------------- |
| Detectar QRS rápido           | Transitorio, agudo           | db2 – db5     |
| Análisis general ECG          | Todo el ciclo P-QRS-T        | db4 – db8     |
| Alta resolución de frecuencia | Ondas lentas, filtrado suave | db6 – db10    |


El estudio emplea **db5** como un compromiso efectivo: suficientemente precisa para el QRS y robusta para limpieza de señal. Ofreciendo ademas un equilibrio entre tiempo y frecuencia.

---

## Resultados

El desempeño experimental del algoritmo de reconocimiento propuesto fue evaluado utilizando dos tipos de clasificadores: distancias euclidianas y Análisis Discriminante Lineal (LDA).

Primero, se calcularon las distancias euclidianas para dos características—energía y potencia—empleando un subconjunto de datos compuesto por registros de personas con múltiples mediciones (señales obtenidas en distintos momentos de un mismo individuo), incluyendo a P7, P6, P10, P11, P16 y P20.

Luego, se calcularon las distancias euclidianas para cada característica en un subconjunto de registros correspondientes a diferentes individuos. Finalmente, se evaluó el rendimiento global del algoritmo combinando ambas características mediante el clasificador LDA.

De este modo se obtuvo un 88.8% para distancias eucladianas entre las energy features y 83.3% entre las power features. Luego a traves de LDA se obtuvo un 83.3% de precisión global.

### Energy signature
![image](https://github.com/user-attachments/assets/79a13efa-2605-4e4e-b19b-68cfdba15450)
Fig.4. Energy signature para la misma persona en diferentes tiempos [1]
![image](https://github.com/user-attachments/assets/d0577217-61da-4dbd-87c4-83fdc62a3b44)
Fig.5. Energy signature para 3 diferentes personas [1]
#### Euclidean distance results
![image](https://github.com/user-attachments/assets/3f6aa06b-7db4-4bf1-abe9-5a0476374de5)
Tabla.1. Distancias Euclidianas entre las energy features de la misma Persona (en Diferentes Momentos)[1]
![image](https://github.com/user-attachments/assets/d46859bc-6669-458e-b78b-ed71b54b2f8f)
Tabla.2. Distancias Euclidianas entre las energy features de diferentes personas[1]

### Power signature
![image](https://github.com/user-attachments/assets/fe64f090-5b85-47a1-85aa-d53d5136e3a7)
Fig.6. Power signature para la misma persona en diferentes tiempos [1]
![image](https://github.com/user-attachments/assets/fcc118b6-1ae4-4d5f-b5bd-4b111072e19e)
Fig.5. Power signature para 3 diferentes personas [1]
#### Euclidean distance results
![image](https://github.com/user-attachments/assets/29bade39-0c36-4de4-be8d-914da699a97c)
Tabla.3. Distancias Euclidianas entre las power features de la misma Persona (en Diferentes Momentos)[1]
![image](https://github.com/user-attachments/assets/a1bb0232-8a04-4061-88e6-b8ac78ac5290)
Tabla.4. Distancias Euclidianas entre las power features de diferentes personas[1]

### Clasificación LDA basada en la combinación de características
![image](https://github.com/user-attachments/assets/0d13933f-472e-426a-b9e4-00282ddf8033)

Tabla.5. Clasificación LDA basada en características de wavelet (energía y potencia)[1]
---

## Conclusiones

- La selección adecuada de **mother wavelets** es crítica para el éxito del análisis ECG.
- **Daubechies 5** proporciona una plataforma robusta para limpieza de señal, ya que permite eliminar ruido sin distorsión.
- **Morlet wavelet** permite extraer representaciones ricas en información de la señal. Asi se usa para representar los patrones biométricos únicos de cada persona.
- El uso de wavelets ofrece una ventaja clara sobre técnicas clásicas (Fourier, estadísticas simples) al tratar señales no estacionarias como el ECG.
- El algoritmo propuesto logró un porcentaje de reconocimiento del 83.3%, demostrando la aplicabilidad de la señal ECG como biométrico para la identificación humana.

---

## Referencias 
- [1] A. A. Elamin and M. Y. Esmail, "Wavelet-Based ECG Signal Analysis for Human Recognition," 2020 International Conference on Computer, Control, Electrical, and Electronics Engineering (ICCCEEE), Khartoum, Sudan, 2021, pp. 1-7, doi: 10.1109/ICCCEEE49695.2021.9429655. keywords: {Biometrics (access control);Databases;Euclidean distance;Electrocardiography;Wavelet analysis;Feature extraction;Rhythm;Wavelet;Biometrics Recognition;ECG;Euclidean Distance;LDA},
- [2] C. Hitrangi Sawant y H. T. Patil,"ECG signal de-noising using discrete wavelet transform",International Journal of Electronics and Communication Computer Engineering, vol. 5, no. 4, pp. 23–28, 2014.
- [3] J. T. Bialasiewicz,"Application of Wavelet Scalogram and Coscalogram for Analysis of Biomedical Signals",in Proc. 2nd Int. Conf. on Biomedical Engineering and Systems, Barcelona, Spain, 2015.  
