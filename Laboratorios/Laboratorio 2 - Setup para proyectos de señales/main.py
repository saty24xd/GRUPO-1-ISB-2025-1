import neurokit2 as nk
import pandas as pd

# Simulated signals for EMG
emgA_long = nk.emg_simulate(duration=15, burst_number=5, burst_duration=2)
emgB_long = nk.emg_simulate(duration=15, burst_number=10, burst_duration=0.8)

# Simulated signals for ECG
ecgA_long = nk.ecg_simulate(duration=15, heart_rate=70, noise=0.1)
ecgB_long = nk.ecg_simulate(duration=15, heart_rate=55, noise=0.2)

emg_df = pd.DataFrame({"EMG2_Long": emgA_long, "EMG5": emgB_long})
ecg_df = pd.DataFrame({"ECG2_Long": ecgA_long, "ECG5": ecgB_long})

nk.signal_plot(emg_df,subplots=True)
nk.signal_plot(ecg_df,subplots=True)