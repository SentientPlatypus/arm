import serial
import time
import sys

def send_serial_message(message):
    try:
        # Open the serial port
        ser = serial.Serial(
            port='/dev/serial0',   # Use '/dev/ttyAMA0' or '/dev/ttyS0' if '/dev/serial0' doesn't work
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )
        time.sleep(2)  # Wait for the serial connection to initialize

        # Send the message
        ser.write(message.encode())

        # Give the device some time to respond
        time.sleep(1)

        # Read the response (if any)
        response = ser.readline().decode().strip()
        print("Response:", response)

        # Close the serial port
        ser.close()
    except serial.SerialException as e:
        print("Error:", e)

# Example usage


if __name__ == "__main__":

    message = " ".join(sys.argv[1:])
    print(message)
    send_serial_message(message)
