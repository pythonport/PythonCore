import time
from pyfirmata2 import Arduino

# 1. Setup Arduino Connection
# Replace 'COM3' with your exact port (e.g., 'COM4', or '/dev/ttyACM0' on Linux/Mac)
PORT = 'COM3' 

print(f"Attempting to connect to Arduino on {PORT}...")

try:
    # Initialize the board
    board = Arduino(PORT)
    print("Success! Python is successfully communicating with your Arduino.")
    
    # Define Pin 13 as a Digital Output (The built-in LED)
    # 'd' = digital, '13' = pin number, 'o' = output
    led_pin = board.get_pin('d:13:o')
    
    print("\nStarting Blink Test. Watch the 'L' LED on your Arduino board!")
    print("Press Ctrl+C in this terminal to stop.\n")
    
    # 2. Blink Loop
    while True:
        for i in range(5):
            # Turn LED ON
            print("LED Status: ON  [High Voltage]")
            led_pin.write(1) 
            time.sleep(1.0) # Wait 1 second
            
            # Turn LED OFF
            print("LED Status: OFF [Low Voltage]")
            led_pin.write(0) 
            time.sleep(1.0) # Wait 1 second
        print("======")
        time.sleep(3.0)

except KeyboardInterrupt:
    print("\nBlink test stopped by user.")

except Exception as e:
    print(f"\nConnection Failed: {e}")
    print("\n--- TROUBLESHOOTING CHECKLIST ---")
    print(f"1. Is your Arduino actually assigned to {PORT}? Check your Device Manager or Arduino IDE.")
    print("2. Did you upload 'StandardFirmata' (not standard firmata plus or an empty sketch)?")
    print("3. Is the Arduino IDE Serial Monitor open? If yes, close it! It steals the port from Python.")

finally:
    # If the board connection was made, close it cleanly
    if 'board' in locals():
        board.exit()
        print("Arduino connection closed cleanly.")