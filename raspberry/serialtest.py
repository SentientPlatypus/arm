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
# Example usage: Set servo 1 to position 1500 with a time of 1000ms
def set_servo_position(servo_id, position, time_ms):
    command = bytearray([0x55, 0x55, 0x08, 0x03, 0x01, 0x01, servo_id, position & 0xFF, (position >> 8) & 0xFF, time_ms & 0xFF, (time_ms >> 8) & 0xFF])
    send_serial_message(command)




if __name__ == "__main__":

    message = " ".join(sys.argv[1:])
    print(message)
    send_serial_message(message)
    # Set servo 1 to position 1500 with a time of 1000ms
    set_servo_position(1, 1000, 1000)
    # Example usage
