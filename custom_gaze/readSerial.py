import serial
import time

while True:
    try:
        ser = serial.Serial('/dev/ttyUSB0', 9600)
        print("Device connected successfully.")
        break
    except serial.SerialException as e:
        print(f"Waiting for Device")
        time.sleep(1)
        continue

while True:
    try:
        data = ser.readline().decode('utf-8').strip()
        if data:
            print(time.time(), data)
        else:
            print("No data received.")
    except serial.SerialException as e:
        print(f"Error reading data: {e}")
        time.sleep(1)
        continue
    except KeyboardInterrupt:
        print("Program interrupted by user.")
        break
