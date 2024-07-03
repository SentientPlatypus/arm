import serial
import time

def send_serial_message(message):
    try:
        # Open the serial port
        ser = serial.Serial('/dev/serial0', 9600, timeout=1)
        time.sleep(2)  # Wait for the serial connection to initialize

        # Send the message
        ser.write(message.encode())

        # Read the response (optional)
        response = ser.readline().decode().strip()
        print("Response:", response)

        # Close the serial port
        ser.close()
    except serial.SerialException as e:
        print("Error:", e)

# Example usage
message = '#1 P1000'
send_serial_message(message)
