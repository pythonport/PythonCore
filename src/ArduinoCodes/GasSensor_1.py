import time
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pyfirmata2 import Arduino

# 1. Setup Arduino Connection
# Replace 'COM3' with your verified working port from the blink test
PORT = 'COM3' 

print(f"Connecting to Arduino on {PORT}...")
board = Arduino(PORT)
print("Connected successfully!")

# 2. Setup Data Storage
# We use a deque with a max length to create a rolling buffer automatically
max_points = 100
y_data = collections.deque([0.0] * max_points, maxlen=max_points)
x_data = list(range(max_points))

# 3. Define the Callback Function
# The Arduino sends data in the background; this updates our data buffer
def smoke_sensor_callback(firmata_val):
    if firmata_val is not None:
        y_data.append(firmata_val)

# Configure the A0 pin with our callback function
analog_pin = board.get_pin('a:0:i')
analog_pin.register_callback(smoke_sensor_callback)
analog_pin.enable_reporting()

# Set sampling rate to 100ms (10 times a second) using correct camelCase
board.setSamplingInterval(100)

# 4. Setup Matplotlib Plot
fig, ax = plt.subplots()
line, = ax.plot(x_data, list(y_data), r'-', color='firebrick', linewidth=2)

ax.set_title("Real-Time Smoke Sensor Readings (MQ-2)")
ax.set_ylabel("Gas Level (Normalized 0.0 - 1.0)")
ax.set_xlabel("Time (Rolling Window)")
ax.set_ylim(0, 1.0)
ax.grid(True)

# 5. Animation Update Loop
def update_plot(frame):
    # Update the y-axis line data with our current rolling buffer values
    line.set_ydata(list(y_data))
    return line,

# Start the animation tracking
try:
    print("\nLaunching real-time graph. Close the graph window or press Ctrl+C to stop.")
    ani = animation.FuncAnimation(fig, update_plot, interval=100, blit=True, cache_frame_data=False)
    plt.show()

except KeyboardInterrupt:
    print("\nStopping graph execution...")

finally:
    # Ensure the board disconnects safely when the user exits
    board.exit()
    print("Arduino connection safely closed.")