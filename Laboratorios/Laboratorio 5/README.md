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

Durante la práctica se logró registrar señales EEG en condiciones controladas utilizando el sistema BITalino y el software OpenSignals, siguiendo la configuración del canal A4 y empleando los electrodos en las ubicaciones Fp1, Fp2 y mastoide, de acuerdo con el sistema internacional 10–20.

Se observó una diferencia cualitativa en la actividad eléctrica entre las condiciones de ojos abiertos y cerrados. Tal como se reporta en la literatura, al cerrar los ojos aumenta la potencia en la banda alfa (8–13 Hz), asociada con estados de relajación en reposo sin estímulos visuales. Aunque no se aplicó un análisis espectral (PSD) en este informe visual, se notan picos de mayor amplitud en los registros con ojos cerrados, lo cual sugiere esta predominancia.

Durante la **tarea cognitiva**, los registros muestran mayor variabilidad y actividad eléctrica más errática. Esto es coherente con el aumento de la actividad en la banda beta (13–30 Hz), vinculada a procesos de atención y cálculo mental. La gráfica respectiva muestra picos frecuentes y amplitudes más irregulares, lo cual es consistente con la activación cortical esperada.

En las condiciones de **artefactos controlados**, como el parpadeo y la masticación, se evidencia claramente la aparición de artefactos con amplitudes superiores a 80 µV, especialmente en forma de ondas abruptas y periódicas. Esto refleja la alta sensibilidad del canal EEG del BITalino a movimientos musculares y artefactos faciales, lo cual concuerda con las especificaciones técnicas del sistema (ganancia 40 000×).

Finalmente, en la condición **libre**, se observaron patrones que dependen del tipo de estímulo definido por el grupo (música o preguntas complejas). La comparación entre las gráficas de Libre1 (música) y Libre2 (preguntas) muestra mayor regularidad en la primera y mayor variabilidad en la segunda, indicando cómo diferentes estímulos pueden modular la actividad cerebral.

**Preguntas para discusión:**
- ¿Qué banda de frecuencia predomina al cerrar los ojos?  
  → La banda **alfa** (8–13 Hz), vinculada al reposo con ojos cerrados.
- ¿Qué filtro es imprescindible para EEG y por qué?  
  → El **pasabanda de 0.8–48 Hz** es esencial para eliminar DC y ruido de red eléctrica.
- ¿Puedes modular conscientemente tu señal EEG?  
  → Sí, por ejemplo cerrando los ojos o practicando respiración consciente.
- ¿Se observan diferencias entre Fp1 y Fp2? ¿Por qué podrían ocurrir?  
  → Aunque no se compararon explícitamente, podrían deberse a asimetrías funcionales entre hemisferios cerebrales.

## Conclusiones

- Se logró una adquisición adecuada de señales EEG en condiciones basales, cognitivas, con artefactos y estímulos libres, cumpliendo con la metodología propuesta.
- Se confirmó la sensibilidad del sistema a artefactos y la necesidad de filtros adecuados para mejorar la calidad de señal.
- Las señales EEG reflejaron patrones esperados según el estado mental: mayor potencia alfa en reposo con ojos cerrados y mayor actividad beta durante el cálculo mental.
- Las condiciones libres mostraron cómo diferentes estímulos pueden modificar la actividad cerebral, validando el uso del EEG para estudios neurocognitivos y aplicaciones biomédicas.
- El uso de BITalino y OpenSignals demostró ser una herramienta accesible y educativa para la introducción al análisis de señales cerebrales en contextos académicos.

## Referencias
1. Nunez, P. L., & Srinivasan, R. (2006). Electric Fields of the Brain: The neurophysics of EEG. Oxford University Press.
2. Niedermeyer, E., & da Silva, F. L. (2005). Electroencephalography: Basic principles, clinical applications, and related fields. Lippincott Williams & Wilkins.
3. BrainyCalc Insights. EEG Filters: Types and Examples. 2024 Dic. Disponible en: https://insights.brainycalc.com/2024/12/eeg-filters-types-and-examples.html
4. Ramírez J, López C. Análisis de señales EEG en aplicaciones médicas. Rev Mex Ing Bioméd. 2013;34(1):15-27. Disponible en: https://www.scielo.org.mx/scielo.php?script=sci_arttext&pid=S0188-95322013000100002
5. Curso EEG. Módulo I: Montajes EEG. Disponible en: https://vsip.info/curso-eeg-modulo-i-montajes-pdf-free.html


