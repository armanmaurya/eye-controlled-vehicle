import serial
import time

class WheelChair:
    def __init__(self) -> None:
        self.isMoving = False
        self.isRotating = False
        self.ser = None
        self.isRotating = False
        
    
    def toggleMoving(self):
        if self.isMoving:
            data = self.ser.readline().decode('utf-8').strip()
            print(data)
            self.ser.write(b'0')
            self.isMoving = False
        else:
            self.ser.write(b'1')
            self.isMoving = True

    def moveBackward(self):
        self.ser.write(b'4')
        self.isMoving = True

    def rotateRight(self):
        self.isRotating = True
        self.ser.write(b'3')
    
    def rotateLeft(self):
        self.isRotating = True
        self.ser.write(b'2')
    
    def stop(self):
        self.ser.write(b'0')
        self.isMoving = False
        self.isRotating = False

    def connect_serial(self, port='COM9', baudrate=9600):
        """Attempts to connect to the serial device."""
        while True:
            try:
                ser = serial.Serial(port, baudrate)
                print("Device connected successfully.")
                self.ser = ser
                break
            except serial.SerialException:
                print("Waiting for Device")
                time.sleep(1)
                continue

    def disconnect_serial(self):
        self.ser.close()
