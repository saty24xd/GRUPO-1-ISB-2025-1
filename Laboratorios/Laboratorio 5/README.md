# Laboratorio 5

## Introducción
La electroencefalografía (EEG) es una técnica no invasiva que permite registrar la actividad eléctrica del cerebro mediante electrodos colocados en el cuero cabelludo. Esta técnica se basa en la detección de potenciales eléctricos generados por la actividad sináptica de las neuronas corticales, y ha sido ampliamente utilizada para el estudio de estados de conciencia, procesos cognitivos, y diagnósticos clínicos como epilepsia o trastornos del sueño.
El sistema de posicionamiento 10–20 es un estándar internacional para la colocación de electrodos EEG. En esta práctica se utilizaron las ubicaciones Fp1, Fp2 y O2, asociadas con las regiones frontales y occipitales del cerebro. Se empleó el dispositivo BiTalino (r)evolution Board Kit BLE/BT, el cual posee una ganancia interna de 40,000 y filtro pasabanda de 0.8–48 Hz, permitiendo registrar señales cerebrales con una resolución de 10 bits.
El objetivo fue registrar y analizar señales EEG en diferentes condiciones: basal (ojos abiertos y cerrados), durante una tarea cognitiva y con presencia de artefactos, reconociendo la presencia de bandas de frecuencia características como delta (δ), theta (θ), alfa (α) y beta (β), relacionadas con distintos estados mentales y funciones cerebrales

## Procedimiento
Preparación del sistema: Se instaló el software OpenSignals y se emparejó el dispositivo BiTalino. Se configuró el canal A4 para EEG.

1. Colocación de electrodos: Tras limpiar las áreas correspondientes, se colocaron los electrodos en las posiciones Fp1, Fp2 y mastoide. 
2. Adquisición de datos: Se registraron señales EEG en las siguientes condiciones:
  - Basal con ojos abiertos (1 min)
  - Basal con ojos cerrados (1 min)
  - Tarea cognitiva (2 min): conteo regresivo de 7 en 7 desde 100
  - Artefactos controlados (2 min): parpadeo y masticación
  - Libre (6 min): actividad definida por el grupo (ej. música o respiración)

## Resultados
| Condición | Gráfica | Descripción |
| --------- | ------- | ----------- |
| Basal con ojos abiertos | ![EEG](visualized/basal1eegv1.png) | Primera toma con los ojos abiertos mirando a un punto fijo |
| Basal con ojos abiertos | ![EEG](visualized/basal1eegv2.png) | Segunda toma con los ojos abiertos mirando a un punto fijo |
| Basal con ojos cerrados | ![EEG](visualized/basal2eegv1.png) | Primera toma con los ojos cerrados |
| Basal con ojos cerrados | ![EEG](visualized/basal2eegv2.png) | Segunda toma con los ojos cerrados |
| Tarea cognitiva | ![EEG](visualized/Plano1eeg.png) | Se hicieron preguntas basadas en: https://link.springer.com/article/10.3758/s13415-019-00703-5/tables/1 |
| Artefactos controlados | ![EEG](visualized/artefacteegv1.png) | Primera toma de parpadear cada 2 s y masticar |
| Artefactos controlados | ![EEG](visualized/artefacteegv2.png) | Segunda toma de parpadear cada 2 s y masticar |
| Libre1 | ![EEG](visualized/librev1eeg.png) | Se puso al participante a escuchar distintos generos musicales |
| Libre2 | ![EEG](visualized/librev2eeg.png) | Se le preguntaron preguntas complejas que tuvieran un promedio de respuesta de 1 minuto |

## Discusión
¿Qué banda de frecuencia predomina al cerrar los ojos? 
Al cerrar los ojos, la actividad en la banda alfa (8-13 Hz) tiende a aumentar, especialmente en regiones occipitales. Esta banda está asociada con estados de relajación y disminución de procesamiento visual.

¿Qué filtro es imprescindible para EEG y por qué? 
Un filtro pasabanda (band-pass) de 0.8-48 Hz es esencial. Este filtro elimina componentes de corriente continua (DC) y artefactos de baja frecuencia, además de suprimir interferencias de la red eléctrica (50/60 Hz), mejorando la calidad de la señal.

¿Puedes modular conscientemente tu señal EEG? Da un ejemplo. 
Sí, es posible modular la señal EEG de manera consciente. Un ejemplo es el control de ritmo mu (8-12 Hz) en la corteza motora. Al imaginar movimientos sin ejecutarlos físicamente, se puede observar una disminución en la potencia de esta banda, lo que se usa en interfaces cerebro-computadora (BCI).

¿Se observan diferencias entre Fp1 y Fp2? ¿Por qué podrían ocurrir? 
Sí, pueden existir diferencias entre Fp1 (hemisferio izquierdo) y Fp2 (hemisferio derecho). Estas diferencias pueden deberse a:

  - Asimetrías funcionales en el procesamiento de emociones y funciones ejecutivas.
  
  - Interferencia de artefactos como movimientos oculares y actividad muscular.
  
  - Variabilidad anatómica en la disposición de estructuras corticales.

## Referencias
1. Nunez, P. L., & Srinivasan, R. (2006). Electric Fields of the Brain: The neurophysics of EEG. Oxford University Press.
2. Niedermeyer, E., & da Silva, F. L. (2005). Electroencephalography: Basic principles, clinical applications, and related fields. Lippincott Williams & Wilkins.
3. BrainyCalc Insights. EEG Filters: Types and Examples. 2024 Dic. Disponible en: https://insights.brainycalc.com/2024/12/eeg-filters-types-and-examples.html
4. Ramírez J, López C. Análisis de señales EEG en aplicaciones médicas. Rev Mex Ing Bioméd. 2013;34(1):15-27. Disponible en: https://www.scielo.org.mx/scielo.php?script=sci_arttext&pid=S0188-95322013000100002
5. Curso EEG. Módulo I: Montajes EEG. Disponible en: https://vsip.info/curso-eeg-modulo-i-montajes-pdf-free.html


