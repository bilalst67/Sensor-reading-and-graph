# Sensor Reading and Graph

## Project Summary

This project involves reading voltage sensor data using the ADS1015 ADC module and a Raspberry Pi Zero 2 W. The collected data is then processed and visualized. The connections are established via I2C communication, and the sensor output is connected to the ADS1015 input channel.

### Key Features
- Reads voltage data from the sensor using ADS1015.
- Communicates via I2C with Raspberry Pi Zero 2 W.
- Logs data for further processing.
- Generates graphs from collected data.

## Materials

| Quantity | Material              |
|---------:|----------------------|
|       1  | Voltage Sensor       |
|       1  | ADS1015              |
|       1  | Raspberry Pi Zero 2 W |
|       1  | Breadboard           |
|       4  | Female-Female Cable  |
|       3  | Female-Male Cable    |
|       1  | Male-Male Cable      |

## Cable Connections

| Sensor Pin | ADS1015 Pin | Raspberry Pi Pin | Breadboard |
|------------|------------|------------------|------------|
| OUT        | AI0        |                  |            |
| GND        | GND        | Any GND          | Any GND    |
|            | VDD        | 3.3V (Pin 1)     |            |
|            | SCL        | Clock (Pin 5)    |            |
|            | SDA        | Data (Pin 3)     |            |
|            | ADDR       | Any GND          |            |

## Project Workflow
1. **Hardware Setup:** Connect the voltage sensor to ADS1015 and Raspberry Pi following the wiring table.
2. **Enable I2C:** Activate I2C on Raspberry Pi using:
   ```sh
   sudo raspi-config
   ```
   - Navigate to `Interfacing Options` → `I2C` → `Enable`.
3. **Install Dependencies:** Install required libraries:
   ```sh
   pip install adafruit-circuitpython-ads1x15
   ```
4. **Run the Script:** Execute the following command to read and visualize sensor data:
   ```sh
   python3 data_read.py
   ```

## License

This project is licensed under the General Public License - see the [LICENSE](LICENSE) file for details.

