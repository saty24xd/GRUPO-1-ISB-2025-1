# Análisis Comparativo de Técnicas de Procesamiento de Señales EEG: FFT, Wavelets y Descomposición Modal

## Introducción

El electroencefalograma (EEG) es una técnica no invasiva que registra la actividad eléctrica del cerebro desde el cuero cabelludo. Su análisis es crucial en contextos clínicos como el diagnóstico de epilepsia, monitoreo de la profundidad anestésica y desarrollo de interfaces cerebro-computadora (BCI). Debido a la naturaleza no estacionaria del EEG, se requiere el uso de métodos robustos de procesamiento de señales para extraer información relevante.

Este informe analiza y compara tres enfoques principales a partir de la revisión de tres artículos científicos recientes:

- Wang et al. (2022) – *Redundant Discrete Wavelet Transform (RDWT)*  
- Al-Fahoum & Al-Fraihat (2014) – *Métodos clásicos en tiempo-frecuencia*  
- Yamochi et al. (2024) – *Empirical Wavelet Transform (EWT) y Wavelet Mode Decomposition (WMD)*

---

## 1. Métodos de Extracción de Características

### 1.1 Fast Fourier Transform (FFT)

**Ventajas:**
- Alta velocidad de cálculo
- Adecuado para señales estacionarias

**Desventajas:**
- Incapacidad de representar correctamente eventos transitorios del EEG
- Resolución temporal limitada

**Referencia:** Al-Fahoum & Al-Fraihat, 2014

---

### 1.2 Wavelet Transform (WT)

Permite un análisis tiempo-frecuencia multiescala utilizando funciones base llamadas wavelets.

**Tipos:**
- **Discrete Wavelet Transform (DWT):** Comúnmente usada, pero sufre de *translation variability (TV)* debido al downsampling.
- **Redundant DWT (RDWT):** Variante sin downsampling que elimina la TV.

**Ventajas del RDWT (Wang et al., 2022):**
- Invarianza ante traslaciones
- Mejor preservación de características temporales
- Recomendada para aplicaciones clínicas sensibles, como BCI

---

### 1.3 Empirical Wavelet Transform (EWT)

**Propuesta por:** Gilles (2013)  
**Implementación reciente en EEG:** Yamochi et al., 2024

**Características:**
- Decomposición adaptativa según el espectro de la señal
- Filtros de Meyer construidos empíricamente
- Alta resolución tiempo-frecuencia

**Limitación:**
- Las bandas de frecuencia varían entre pacientes y entre épocas de análisis

---

### 1.4 Wavelet Mode Decomposition (WMD)

**Desarrollado por:** Yamochi et al., 2024

**Características:**
- Utiliza Meyer wavelets con bandas predefinidas (δ, θ, α, β, γ)
- Control total sobre los rangos de frecuencia
- Extracción de modos con alta precisión y estabilidad intersujeto

**Resultados:**
- Mostró la mayor correlación con el índice BIS de profundidad anestésica (R² = 0.899)
- Superó a FFT, DWT, EWT y VMD en precisión y estabilidad

---

## 2. Comparación de Métodos

| Método | Estacionario | Adaptativo | Res. Tiempo-Frec. | Invarianza a Traslaciones | Precisión Clínica |
|--------|--------------|------------|--------------------|----------------------------|-------------------|
| FFT    | Sí           | No         | Baja               | No                         | Baja              |
| DWT    | Sí           | No         | Media              | No (TV)                    | Moderada          |
| RDWT   | Sí           | No         | Alta               | Sí                         | Alta              |
| EWT    | Parcial      | Sí         | Alta               | No                         | Variable          |
| WMD    | Parcial      | Sí         | Alta               | Sí                         | Muy alta          |

---

## 3. Conclusión

Los métodos basados en wavelets representan una mejora significativa respecto a las técnicas tradicionales para el análisis de señales EEG. En particular:

- **RDWT** ofrece una mejora estructural sobre el DWT al eliminar la variabilidad por traslación.
- **WMD** combina las ventajas de las wavelets con control preciso sobre bandas de frecuencia, mostrando una correlación superior con parámetros clínicos reales como el BIS.
- **FFT** y **DWT** presentan limitaciones notables en la resolución y estabilidad de características extraídas.

---

## Referencias

- Wang, X.-Y., et al. (2022). *Intelligent Extraction of Salient Feature From Electroencephalogram Using Redundant Discrete Wavelet Transform*. Front. Neurosci., 16:921642. https://doi.org/10.3389/fnins.2022.921642

- Al-Fahoum, A.S., & Al-Fraihat, A.A. (2014). *Methods of EEG Signal Features Extraction Using Linear Analysis in Frequency and Time-Frequency Domains*. ISRN Neuroscience, 2014:730218. https://doi.org/10.1155/2014/730218

- Yamochi, S., et al. (2024). *Wavelet transform-based mode decomposition for EEG signals under general anesthesia*. PeerJ, 12:e18518. https://doi.org/10.7717/peerj.18518
