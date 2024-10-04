import serial
import time

# Set up the serial connection (adjust the port and baud rate as needed)
ser = serial.Serial('COM4', 9600)  # Replace 'COM3' with your actual port, e.g., '/dev/ttyUSB0' for Linux
time.sleep(2)  # Wait for the connection to establish

# Send data to Arduino
while True:
    user_input = input("Enter 0 to turn OFF the LED, 1 to turn ON the LED: ")
    
    if user_input == '0':
        ser.write(b'0')  # Send byte 0 to Arduino
        # data = ser.readline().decode('utf-8').strip()
        print("LED OFF command sent.")

    elif user_input == '1':
        ser.write(b'1')  # Send byte 1 to Arduino
        # data = ser.readline().decode('utf-8').strip()
        print("LED ON command sent.")
    elif user_input == '2':
        ser.write(b'2')
        # data = ser.readline().decode('utf-8').strip()
        print("Rotating left")
    elif user_input == '3':
        ser.write(b'3')
        # data = ser.readline().decode('utf-8').strip()
        print("Rotating right")
    else:
        print("Invalid input. Please enter 0 or 1.")
        
    time.sleep(1)  # Delay to avoid sending data too fast

# Close the serial connection when done
ser.close()
