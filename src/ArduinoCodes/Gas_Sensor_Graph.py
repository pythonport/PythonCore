'''
Created on Jul 3, 2026

@author: admin
'''
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pyfirmata2 import Arduino

# 1. Setup Arduino Connection
# Replace 'COM3' with your actual port (e.g., '/dev/ttyACM0' on Linux/Mac)
PORT = 'COM3' 
board = Arduino(PORT)

# Set up the sampling rate (sampling every 100ms)
sampling_rate = 100 
board.samplingOn(sampling_rate)

# Define the analog pin (A0)
analog_pin = board.get_pin('a:0:i') 

# 2. Setup Plot Data Lists
max_data_points = 100  # Number of points shown on screen at one time
x_data = list(range(max_data_points))
y_data = [0.0] * max_data_points

# 3. Create Figure and Axis for Plotting
fig, ax = plt.subplots()
line, = ax.plot(x_data, y_data, r'-', linewidth=2)

ax.set_title("Real-Time Smoke Sensor Readings (MQ-2)")
ax.set_ylabel("Gas Concentration Level (Normalized 0.0 - 1.0)")
ax.set_xlabel("Time (Rolling Window)")
ax.set_ylim(0, 1.0) # Firmata scales analog 0-5V to a 0.0-1.0 float range
ax.grid(True)

# 4. Animation Update Function
def update_plot(frame):
    # Read the latest sensor value from Firmata
    sensor_value = analog_pin.read()
    
    # Firmata returns None if it hasn't registered a reading yet
    if sensor_value is None:
        sensor_value = 0.0
        
    # Append new data and keep list size constant (rolling window)
    y_data.append(sensor_value)
    y_data.pop(0)
    
    # Update the chart line
    line.set_ydata(y_data)
    return line,

# 5. Start the Live Plot
try:
    # interval matches our sampling rate in milliseconds
    #ani = animation.FuncAnimation(fig, update_plot, interval=sampling_rate, blit=True)
    #plt.show()
    pass

except KeyboardInterrupt:
    print("Stopping application...")

finally:
    # Clean up and safely close connection
    board.exit()
    print("Arduino connection closed.")