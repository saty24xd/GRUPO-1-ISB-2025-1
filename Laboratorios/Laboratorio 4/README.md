# Laboratorio 4

## Introducción
El electrocardiograma (ECG) es un procedimiento no invasivo que registra la actividad eléctrica del corazón mediante electrodos colocados en puntos específicos del cuerpo. Esta técnica permite detectar diversas patologías cardíacas como arritmias, cardiomiopatías, enfermedades	 de las arterias coronarias, entre otras [1]. La señal obtenida se analiza a través de ondas características (P, QRS y T), cada una representando un evento eléctrico específico dentro del ciclo cardíaco. [1]
Para lograr un análisis estructurado, se utilizan derivaciones, que son combinaciones específicas de estos electrodos. Entre las principales se encuentran las derivaciones bipolares de Einthoven: Lead I, Lead II y Lead III, las cuales forman el denominado triángulo de Einthoven. Este triángulo conecta los brazos derecho (RA) e izquierdo (LA) y la pierna izquierda (LL), permitiendo visualizar la dirección y magnitud de la despolarización cardíaca en diferentes ejes.

![](images/intro.png)

La derivación Lead I mide la diferencia de potencial entre el brazo derecho (RA, negativo) y el brazo izquierdo (LA, positivo). Lead II mide entre el brazo derecho (RA, negativo) y la pierna izquierda (LL, positivo). Finalmente, Lead III registra entre el brazo izquierdo (LA, negativo) y la pierna izquierda (LL, positivo). Estas tres derivaciones permiten obtener una visión completa de la actividad eléctrica en el plano frontal del corazón.
En esta práctica, se utilizó el kit BITalino (r)evolution junto con el software OpenSignals para adquirir señales de ECG. Se trabajó inicialmente con Lead I, colocando electrodos en las clavículas (RA y LA) y la referencia en la cresta ilíaca, y luego se configuraron Lead II y Lead III para completar el registro según el esquema de Einthoven.

## Objetivos específicos de la práctica
1. Adquirir señales biomédicas de ECG utilizando el kit BITalino (r)evolution.
2. Realizar la correcta configuración del dispositivo BITalino y del software OpenSignals (r)evolution.
3. Extraer, visualizar y analizar las señales ECG obtenidas en diferentes condiciones fisiológicas (reposo, apnea, post ejercicio)

## Resultados
### Señales ECG - REPOSO

| Condición    | Derivada 1                       | Derivada 2                       | Derivada 3                       |
|--------------|-----------------------------------|-----------------------------------|-----------------------------------|
| **Reposo 1** | ![](visualized/r1dev1.png)         | ![](visualized/r1dev2.png)        | ![](visualized/r1dev3.png)        |
| **Reposo 2** | ![](visualized/r2dev1.png)         | ![](visualized/r2dev2.png)        | ![](visualized/r2dev3.png)        |

### Señales ECG - Movimiento

| Condición    | Derivada 1                       | Derivada 2                       | Derivada 3                       |
|--------------|-----------------------------------|-----------------------------------|-----------------------------------|
| **Movimiento 1** | ![](visualized/mov1dev1.png)         | ![](visualized/mov1dev2.png)        | ![](visualized/mov1dev3.png)        |
| **Movimiento 2** | ![](visualized/mov2dev1.png)         | ![](visualized/mov2dev2.png)        | ![](visualized/mov2dev3.png)        |

### Señales ECG - Respiración

| Condición    | Derivada 1                       | Derivada 2                       | Derivada 3                       |
|--------------|-----------------------------------|-----------------------------------|-----------------------------------|
| **Respiración 1** | ![](visualized/respiracion1dev1.png)         | ![](visualized/respiracion1dev2.png)        | ![](visualized/respiracion1dev3.png)        |
| **Respiración 2** | ![](visualized/respiracion2dev1.png)         | ![](visualized/respiracion2dev2.png)        | ![](visualized/respiracion2dev3.png)        |

## Análisis y discusión
A continuación se presentan las señales obtenidas en los tres condiciones experimentales

1. Señales en Reposo
- Reposo 1 y Reposo 2 muestran señales estables, de frecuencia cardíaca moderada, con complejos QRS bien definidos.
- Hay baja presencia de ruido, ideal para un registro en reposo.
- La línea base se mantiene estable, indicando ausencia de artefactos de movimiento o mala conexión.

2. Señales en Movimiento
Movimiento 1 y Movimiento 2 presentan:
- Mayor variabilidad en la amplitud.
- Presencia de artefactos visibles, probablemente generados por movimiento muscular (EMG) y desplazamientos de los electrodos.
- Alteraciones en la línea base más frecuentes, normales en registros de ECG durante movimiento.

Comparación
El patrón observado confirma las expectativas: en reposo, las señales son más limpias, mientras que en movimiento aparecen más ruidos y alteraciones.
Este cambio en la calidad de la señal entre condiciones evidencia un análisis crítico adecuado de las señales adquiridas.

## Referencias
1. My EKG. Derivaciones cardíacas, significado [Internet]. My EKG. Disponible en: https://www.my-ekg.com/generalidades-ekg/derivaciones-cardiacas.php​

2. PLUX Biosignals. OpenSignals (r)evolution (Download) [Internet]. PLUX Biosignals; [citado 2025 abr 29]. Disponible en: https://support.pluxbiosignals.com/knowledge-base/introducing-opensignals-revolution/​

3. BITalino. BITalino (r)evolution Lab Guide [Internet]. BITalino; [citado 2025 abr 29]. Disponible en: https://bitalino.com/storage/uploads/media/homeguide0-gettingstarted.pdf​
