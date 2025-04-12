# Laboratorio 3: Análisis de EMG con BitaLino 

En este laboratorio nos enfocamos en registrar y analizar señales electromiográficas (EMG) a partir de la plataforma BITalino. Este dispositivo ha demostrado ser una herramienta confiable para la adquisición de biosensores en diferentes investigaciones, con resultados equiparables a los de equipos comerciales (1,2).

## Introducción
El objetivo principal fue capturar y evaluar la actividad muscular en tres grupos específicos: bíceps braquial, deltoides lateral y bíceps femoral, tanto en reposo como durante tareas que exigen distintos niveles de esfuerzo. Además de comprobar el funcionamiento básico del BITalino, se buscó observar la influencia de la fatiga en la amplitud y características de la señal EMG.

## Objetivos
1. Configurar y ejecutar la adquisición de señales EMG utilizando BitaLino.  
2. Registrar la actividad eléctrica de los músculos seleccionados en reposo y en actividad.  
3. Examinar la variación de la amplitud y la presencia de ruido en las señales bajo diferentes condiciones.  
4. Generar gráficos que muestren la respuesta EMG y discutir los hallazgos más relevantes.

## Materiales y metodología

### Materiales
- BitaLino
- Laptop
- Electrodos
- Script de OpenSignal

### Metodología
1. **Conexión y configuración:** Se conectó el BitaLino a la computadora a través de Bluetooth y se aseguraron las configuraciones necesarias en el software OpenSignal.
2. **Colocación de electrodos:** Se ubicaron los electrodos en la zona muscular de interés (bíceps braquial, deltoides lateral), siguiendo las recomendaciones de anatomía para obtener lecturas más fiables.  
3. **Registro de señales en reposo:** Cada músculo se midió durante 30 segundos sin realizar actividad física intencional.  
4. **Registro de señales con actividad:**  
   - **Bíceps braquial:** Se realizaron curls de bíceps con y sin carga.  
   - **Deltoides lateral:** Se llevaron a cabo elevaciones laterales simples y con contrapeso.  
   - **Bíceps femoral:** Se efectuaron flexiones de rodilla para evaluar la respuesta durante la contracción.  
   En todos los casos, se mantuvo la medición durante 30 segundos, repitiendo tomas para comparar resultados y observar la aparición de fatiga.  
5. **Adquisición de datos:** Se almacenaron las señales obtenidas a lo largo de cada sesión y se generaron los correspondientes gráficos a partir de la información recopilada.  

Enlaces de las diferentes tomas (reposo y actividad en cada músculo) están disponibles en la siguiente lista:

- **Bíceps braquial**  
  - Reposo: Toma 1 - https://drive.google.com/file/d/1ou7gz9C0gXnLimJu7HMcETf8snbXXJhl/view?usp=sharing
  - Actividad (Curl de bíceps): 
    - Toma 1 - https://drive.google.com/file/d/1ZBnxqPcMhYi1JdIMZcHu9aHS5jDJ9y2o/view?usp=sharing
    - Toma 2 - https://drive.google.com/file/d/1Kz933VxDD_z7_xWAUoA1jPidlAEPdVVn/view?usp=sharing
    - Toma 3 - https://drive.google.com/file/d/107EHYXOmQXVJVX16lYMqAldProqZGe_Y/view?usp=sharing

- **Deltoides lateral**  
  - Reposo: Toma reposo - https://drive.google.com/file/d/18p22JrYv38N5F9x_m6AigM1L2V8P_3-j/view?usp=sharing
  - Actividad (Elevación lateral): 
    - Toma 1 - https://drive.google.com/file/d/1vO1vLFR57mSN-q1HQZzkEl9Hz0T00qBl/view?usp=sharing
    - Toma 2 - https://drive.google.com/file/d/1nd_9MNHqxO7vNAqhpJ7EhBq3iyre8je8/view?usp=sharing
    - Toma 3 - https://drive.google.com/file/d/1ZU8uy4eAhLbxjZvlXJTSTeval90Yre8D/view?usp=sharing
  - Con contrapeso (30 s): 
    - Toma 4 - https://drive.google.com/file/d/1r3fbSumU9PJPO1xza9l91hhUj8mg4lyB/view?usp=sharing
    - Toma 5 - https://drive.google.com/file/d/1NGn6QaVBCJNQptA5XYQhzWjQf1nK7VBp/view?usp=sharing
    - Toma 6 - https://drive.google.com/file/d/1d8HDOhkKJgR4Az1W65tEmTlfPdCppV9G/view?usp=sharing

## Análisis y discusión
Se evidencia que la señal de EMG en reposo es más sensible a la actividad que la señal de EMG en actividad. Esto se debe a que la actividad es más intensa y la reposo es menos intensa. Además, la señal de EMG en actividad tienen mayor ruido y amplitud que la de reposo, también se pudo observar que el cansancio acumulado limita la respuesta del EMG en las última mediciones.

Tras revisar los registros, se comprobó que las señales en reposo tienen una amplitud notablemente baja y, por consiguiente, son más susceptibles a interferencias. Por el contrario, durante la actividad (especialmente con carga), se observaron picos de mayor amplitud. Estos resultados se ajustan a lo reportado en otros trabajos, donde se describe un incremento significativo de la amplitud EMG conforme aumenta la fuerza ejercida (1,2).

Asimismo, se notó la influencia de la fatiga muscular: en las últimas repeticiones de cada ejercicio la amplitud de la señal tendía a disminuir, lo que coincide con el comportamiento típico de la fatiga descrito en la literatura. Dicho cansancio también puede incrementar el ruido en la señal, al existir movimientos involuntarios o cambios en la colocación de los electrodos.

### Limitaciones 
1. Se observó mucho ruido en las señales, lo cual puede ser dado por falta de equilibrio en la actividad o sensibilidad de electrodos

### Referencias
1. Martins A, Chen L, Silva H. BITalino: A Wearable Platform for the Acquisition of Biosignals. IEEE Trans Biomed Eng. 2014;61(3):787–97.  
2. da Silva RGS, Thompson BC, Freedman P, Harrington L. A Comparative Study of EMG Data Acquired Using BITalino (r)evolution and a Commercial EMG Device for Muscle Activation Detection. In: 2019 IEEE International Symposium on Medical Measurements and Applications (MeMeA). Piscataway, NJ: IEEE; 2019. p. 1–5.