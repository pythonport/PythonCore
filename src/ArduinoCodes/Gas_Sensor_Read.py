import time
from pyfirmata2 import Arduino

# 1. Setup Arduino Connection
# Update 'COM3' to match your actual port (e.g., '/dev/ttyACM0' on Linux/Mac)
PORT = 'COM3' 
print(f"Connecting to Arduino on {PORT}...")

board = Arduino(PORT)
print("Successfully connected!")

# 2. Define the Callback Function
def smoke_sensor_callback(firmata_val):
    if firmata_val is not None:
        # Reconstruct the traditional 10-bit Arduino analog value
        arduino_raw = int(firmata_val * 1023)
        print(f"Firmata: {firmata_val:.4f}  |  Raw Arduino (0-1023): {arduino_raw}")

# 3. Setup Pin and Register the Callback
analog_pin = board.get_pin('a:0:i')
analog_pin.register_callback(smoke_sensor_callback)
analog_pin.enable_reporting()

# 4. Set Sampling Rate (Using the correct camelCase method)
# 1000ms = 1 second interval
board.setSamplingInterval(1000)

print("\nReading smoke sensor data. Press Ctrl+C to stop.")
print("-" * 60)

# 5. Keep the Main Script Alive
try:
    while True:
        # The main thread rests. The background thread calls the callback automatically.
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nTesting stopped by user.")

finally:
    board.exit()
    print("Arduino connection safely closed.")