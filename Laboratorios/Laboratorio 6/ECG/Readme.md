# Filtrado de Señales ECG con Filtros FIR e IIR

## Introducción

El electrocardiograma (ECG) permite registrar la actividad eléctrica del corazón, siendo una herramienta diagnóstica fundamental. Sin embargo, estas señales suelen estar contaminadas con ruido, especialmente en las altas frecuencias, debido a interferencias eléctricas, movimiento del paciente o artefactos musculares. Para mejorar la calidad de estas señales y su análisis posterior, se emplean filtros digitales como los FIR e IIR, que permiten atenuar el ruido preservando las características clínicas relevantes del ECG.

---

## Objetivos

- Aplicar técnicas de procesamiento digital a señales de ECG registradas en condiciones controladas para remover el ruido de alta frecuencia.
- Diseñar **al menos un filtro IIR** comparando entre dos tipos: **Bessel, Butterworth, Chebyshev o Elíptico**.
- Diseñar **al menos un filtro FIR** utilizando dos técnicas basadas en ventanas: **Hanning, Hamming, Bartlett, Rectangular o Blackman**.
- Comparar gráficamente y discutir el desempeño de cada filtro con respecto a la señal original.
- Generar un informe técnico en formato Markdown adecuado para documentación y publicación en GitHub.

---

## Metodología

Se utilizaron 9 señales de ECG recolectadas en un laboratorio previo, distribuidas en tres condiciones fisiológicas:

- **Basal 1**: reposo absoluto.
- **Respiración**: respiración controlada.
- **Post-ejercicio**: tras esfuerzo físico leve.

Cada condición cuenta con tres derivaciones. El procesamiento realizado fue:

1. **Lectura de archivos `.txt`** y detección automática de encabezados.
2. **Selección de la señal más significativa** de cada archivo (mayor desviación estándar).
3. **Aplicación de filtros**:
   - **IIR**:
     - Butterworth (orden 4)
     - Bessel (orden 4)
   - **FIR**:
     - Ventana Hamming (orden 101)
     - Ventana Blackman (orden 151)
4. **Filtrado digital sin distorsión de fase** usando `filtfilt`.
5. **Exportación de resultados**: gráficos y archivos CSV.
6. **Resumen visual** en formato tabla con miniaturas de resultados.

---

## Resultados

La siguiente tabla muestra un resumen por condición fisiológica. Cada grupo contiene tres derivaciones visualizadas para comparar:

| Estado             | Señal Cruda                               | Filtrada IIR                              | Filtrada FIR                              |                                           |                                           |                                           |                                           |                                           |                                           |
| ------------------ | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
|                    | Derivación 1                              | Derivación 2                              | Derivación 3                              | Derivación 1                              | Derivación 2                              | Derivación 3                              | Derivación 1                              | Derivación 2                              | Derivación 3                              |
| **Basal 1**        | ![](FIR-IIR_eeg/reposo_dev1_raw.png)      | ![](FIR-IIR_eeg/reposo_dev2_raw.png)      | ![](FIR-IIR_eeg/reposo_dev3_raw.png)      | ![](FIR-IIR_eeg/reposo_dev1_iir.png)      | ![](FIR-IIR_eeg/reposo_dev2_iir.png)      | ![](FIR-IIR_eeg/reposo_dev3_iir.png)      | ![](FIR-IIR_eeg/reposo_dev1_fir.png)      | ![](FIR-IIR_eeg/reposo_dev2_fir.png)      | ![](FIR-IIR_eeg/reposo_dev3_fir.png)      |
| **Respiración**    | ![](FIR-IIR_eeg/respiracion_dev1_raw.png) | ![](FIR-IIR_eeg/respiracion_dev2_raw.png) | ![](FIR-IIR_eeg/respiracion_dev3_raw.png) | ![](FIR-IIR_eeg/respiracion_dev1_iir.png) | ![](FIR-IIR_eeg/respiracion_dev2_iir.png) | ![](FIR-IIR_eeg/respiracion_dev3_iir.png) | ![](FIR-IIR_eeg/respiracion_dev1_fir.png) | ![](FIR-IIR_eeg/respiracion_dev2_fir.png) | ![](FIR-IIR_eeg/respiracion_dev3_fir.png) |
| **Post-ejercicio** | ![](FIR-IIR_eeg/movimiento_dev1_raw.png)  | ![](FIR-IIR_eeg/movimiento_dev2_raw.png)  | ![](FIR-IIR_eeg/movimiento_dev3_raw.png)  | ![](FIR-IIR_eeg/movimiento_dev1_iir.png)  | ![](FIR-IIR_eeg/movimiento_dev2_iir.png)  | ![](FIR-IIR_eeg/movimiento_dev3_iir.png)  | ![](FIR-IIR_eeg/movimiento_dev1_fir.png)  | ![](FIR-IIR_eeg/movimiento_dev2_fir.png)  | ![](FIR-IIR_eeg/movimiento_dev3_fir.png)  |


> 📌 *Cada derivación representa una señal distinta dentro del estado fisiológico correspondiente.*

---

## Discusión

De acuerdo con los objetivos planteados, se llevó a cabo un diseño y comparación de filtros digitales IIR y FIR para mejorar la calidad de las señales ECG. En el análisis gráfico, se observa que:

- **Filtros IIR (Butterworth y Bessel)** permitieron una buena atenuación del ruido sin alterar significativamente la morfología de la señal, siendo Butterworth más selectivo y Bessel más fiel en fase.
- **Filtros FIR (Hamming y Blackman)** mostraron una respuesta en frecuencia más controlada en la banda de parada, siendo el filtro con ventana Blackman el más efectivo en cuanto a supresión de ruido, aunque con mayor coste computacional.
- **Las derivaciones post-ejercicio** fueron las más afectadas por artefactos de alta frecuencia, evidenciando la necesidad de filtrado adecuado.
- La comparación entre métodos mostró que el **IIR Bessel** y el **FIR Hamming** logran un excelente equilibrio entre limpieza y conservación de forma, lo cual es fundamental en aplicaciones clínicas.

---

## Conclusiones

- Se cumplieron los objetivos del proyecto, logrando aplicar y comparar filtros digitales para eliminar ruido de alta frecuencia en señales ECG reales.
- Se diseñaron filtros IIR (Butterworth y Bessel) y FIR (Hamming y Blackman), comprobando sus efectos en tres estados fisiológicos distintos.
- Los resultados indican que filtros **Bessel** y **Hamming** ofrecen la mejor relación entre rendimiento y preservación de la forma de onda, haciendo de ellos candidatos óptimos para aplicaciones biomédicas.
- La metodología puede adaptarse fácilmente a otros tipos de señales fisiológicas o diferentes condiciones de captura.

---

## Referencias

1. Rangayyan, R. M. (2002). *Biomedical Signal Analysis*. IEEE Press.
2. Mitra, S. K. (2006). *Digital Signal Processing: A Computer-Based Approach*. McGraw-Hill.
3. Clifford, G. D., Azuaje, F., & McSharry, P. (2006). *Advanced Methods and Tools for ECG Data Analysis*. Artech House.
4. SciPy Signal Processing Toolbox: https://docs.scipy.org/doc/scipy/reference/signal.html
5. GitHub Markdown Guide: https://guides.github.com/features/mastering-markdown/
