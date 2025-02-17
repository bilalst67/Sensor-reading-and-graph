import smbus
import time
import math
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as an

# ADS1015 settings
I2C_ADDRESS = 0x48  # I2C address of ADS1015
V_REF = 3.3  # Reference voltage for ADS1015
ADC_MAX = 2047  # Maximum value for 12-bit resolution of ADS1015
SAMPLE_COUNT = 100  # Number of samples to take for RMS calculation

# I2C Connection
bus = smbus.SMBus(1)

# Zero point calibration
zero_point = 0

def ads1015_read():
    """Reads raw ADC data and voltage from the ADS1015."""
    bus.write_i2c_block_data(I2C_ADDRESS, 0x01, [0xC2, 0x83])  # Configuration for ADS1015
    time.sleep(0.002)  # ADC conversion time
    data = bus.read_i2c_block_data(I2C_ADDRESS, 0x00, 2)  # Read ADC data

    raw = (data[0] << 8) | data[1]  # Combine two bytes to get a 16-bit value
    raw = raw >> 4  # Adjust for the 12-bit ADC resolution

    if raw & 0x800:  # Adjust for negative values (12-bit signed conversion)
        raw -= 1 << 12  

    voltage = (raw / ADC_MAX) * V_REF  # Calculate voltage from the ADC value
    return raw, voltage

def rms_calculate(voltage_values):
    """Calculates the RMS value from the voltage samples."""
    sum_of_squares = np.sum(np.array(voltage_values) ** 2)  # Sum of squares of voltages
    rms_value = math.sqrt(sum_of_squares / len(voltage_values)) * 21.5  # Compute RMS and scale it
    return rms_value

def calibrate():
    """Calibrates the sensor and determines the zero point."""
    global zero_point
    measurements = []
    for _ in range(1000):  
                try:
                    _, voltaj = ads1015_oku()
                except IOError:  # We catch IO errors
                    voltaj=0    #When it fails, it sets the voltage value to 0 and provides you with feedback by returning a constant value. For example, if the last measured value was 200, it continues with 200.
                    continue  # Continue loop on error
        measurements.append(voltage)
        time.sleep(0.005)  # Faster calibration
    zero_point = round(sum(measurements) / len(measurements), 3)  # Set zero point more precisely
    print(f"Calibration Complete: Zero Point = {zero_point} V")

def plot_animation():
    """Draws a live graph of the voltage."""
    fig, ax = plt.subplots()  # Create a figure and axis for the plot
    x = []  # List for X values (sample number)
    y = []  # List for Y values (RMS values)
    line, = ax.plot([], [], color="red")  # Initialize a line object to plot data
    ax.set_xlabel("Sample")
    ax.set_ylabel("RMS Value")
    ax.set_title("Voltage Graph")

    def animate(i):
        """Function to update the graph every frame."""
        voltage_values = []  # List to store voltage readings
        global rms_value
        for _ in range(SAMPLE_COUNT):
                    try:
                        _, voltaj = ads1015_oku()
                    except IOError:  # We catch IO errors
                        voltaj=0    #When it fails, it sets the voltage value to 0 and provides you with feedback by returning a constant value. For example, if the last measured value was 200, it continues with 200.
                        continue  # Continue loop on error
            voltage -= zero_point  # Remove the zero point offset
            voltage_values.append(voltage)
            time.sleep(0.001)
        rms_value = rms_calculate(voltage_values)  # Calculate RMS value
        rms_value = round(rms_value * 14.32, 2)  # Scale the RMS value
        x.append(i)
        y.append(rms_value)
        print((rms_value))  # Print the current RMS value
        if len(x) > 100:  # Keep only the last 100 points in the plot
            x.pop(0)
            y.pop(0)
        write_data(rms_value)  # Save the RMS value to CSV
        line.set_data(x, y)  # Update the plot with new data
        ax.relim()  # Recalculate axis limits
        ax.autoscale_view()  # Autoscale the plot
        return line,

    ani = an.FuncAnimation(fig, animate, interval=10, cache_frame_data=False)  # Create animation
    plt.show()

def write_data_title():
    """Writes the header to the CSV file."""
    with open("data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["RMS"])

def write_data(data):
    """Writes the measured RMS value to the CSV file."""
    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([data])

# --- Main Program ---
write_data_title()  # Write the header to the CSV file
zero_point = 0.271  # Manually set the zero point for the sensor
# Dynamic zero point calibration (commented out)
#calibrate() #Starts the calibration and assigns the resulting zero point to the zero point above. It may not be assigned, so change it yourself.
plot_animation() #It receives data from the sensor and draws graphs simultaneously. If you are going to use it, there is no need for the while loop below.
voltage_values = []

while True:     
    for _ in range(ORNEK_SAYISI):
        try:
            _, voltaj = ads1015_oku()
        except IOError:  # We catch IO errors
            voltaj=0    #When it fails, it sets the voltage value to 0 and provides you with feedback by returning a constant value. For example, if the last measured value was 200, it continues with 200.
            continue  # Continue loop on error
        voltaj -= zero_point  # If no error occurs, this action is performed.
        voltajlar.append(voltaj)
        time.sleep(0.001)
    
    rms_deger = rms_hesapla(voltajlar)
    rms_deger = round(rms_deger * 12.5, 2)
    print(rms_deger)
    write_data(rms_deger)
    time.sleep(0.05)
