import neurokit2 as nk
import pandas as pd

# Simulate
emg2 = nk.emg_simulate(duration=10, burst_number=2, burst_duration=1.0)
emg2_long = nk.emg_simulate(duration=10, burst_number=2, burst_duration=1.5)
emg5 = nk.emg_simulate(duration=10, burst_number=5, burst_duration=1.0)

# Visualize
emg_df = pd.DataFrame({"EMG2": emg2, "EMG2_Longer": emg2_long, "EMG5": emg5})
nk.signal_plot(emg_df,subplots=True)