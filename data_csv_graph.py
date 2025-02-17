import matplotlib.pyplot as pl
import pandas as pd
import time as t
import numpy as np

# Start time measurement
start_time = t.time()

# Read the data from the CSV file
data = pd.read_csv("data.csv")

# If there is time information in the second column, use it as the X-axis
if data.shape[1] > 1:
    time_values = data.iloc[:, 1].values  # Assuming the second column represents time
else:
    time_values = np.arange(len(data))  # Otherwise, number the samples

# Get the pin values (first column)
pin_values = data.iloc[:, 0].values

# Apply moving average to reduce noise (optional)
window_size = 5  # Window size for moving average (can be adjusted if needed)
filtered_values = np.convolve(pin_values, np.ones(window_size)/window_size, mode='valid')

# Plot the data
pl.plot(time_values[:len(filtered_values)], filtered_values, color='red', label='Pin', linewidth='0.5')

# Set plot labels and title
pl.xlabel('Sample')  
pl.ylabel('RMS Value')
pl.title('Pin Voltage Graph')

# Print time taken to plot the graph
print("Time taken to plot the graph:", round(t.time() - start_time, 3), "seconds")

# Display the legend and show the plot
pl.legend()
pl.show()
