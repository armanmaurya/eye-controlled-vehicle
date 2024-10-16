"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""
import serial
import time
import cv2
from custom_gaze import CustomTracking
import datetime
import logging
from wheel_chair import WheelChair



def connect_serial(port='COM5', baudrate=9600):
    """Attempts to connect to the serial device."""
    while True:
        try:
            ser = serial.Serial(port, baudrate)
            print("Device connected successfully.")
            return ser
        except serial.SerialException:
            logging.warning("Waiting for Device")
            time.sleep(1)

going_right = False
going_front = False
going_left = False

def main():
    gaze = CustomTracking()
    webcam = cv2.VideoCapture(0)
    wheelChair = WheelChair()

    if not webcam.isOpened():
        logging.error("Could not open webcam.")
        return

    # ser = connect_serial()
    wheelChair.connect_serial()
    try:
        while True:
            # We get a new frame from the webcam
            ret, frame = webcam.read()
            if not ret:
                logging.error("Failed to capture frame from webcam.")
                break

            # We send this frame to GazeTracking to analyze it
            gaze.refresh(frame)

            frame = gaze.annotated_frame()
            text = ""

            gaze.DetectBlink()

            if gaze.final_blink_count == 2:
                text = "Blinking"
                # if gaze.is_right():
                #     print("Going right")
                #     wheelChair.rotateRight()
                # elif gaze.is_left():
                #     print("Going left")
                #     wheelChair.rotateLeft()
                if gaze.is_center():
                    gaze.final_blink_count = 0
                    print("Going Forward")
                    wheelChair.toggleMoving()
            elif gaze.final_blink_count == 3:
                print("Going Backward")
                gaze.final_blink_count = 0
                wheelChair.moveBackward()

            if gaze.is_left():
                if wheelChair.isRotating == False:
                    wheelChair.rotateLeft()
                    wheelChair.isRotating = True
            if gaze.is_right():
                if wheelChair.isRotating == False:
                    wheelChair.rotateRight()
                    wheelChair.isRotating = True
            if gaze.is_center():
                if wheelChair.isRotating:
                    wheelChair.stop()
                    wheelChair.isRotating = False

            if gaze.is_center() and wheelChair.isRotating:
                wheelChair.stop()
                print("Stop")

            
            if gaze.is_right():
                text = "Looking right"
            elif gaze.is_left():
                text = "Looking left"
            elif gaze.is_center():
                text = "Looking center"
                # ser.write(b'3')


            cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

            left_pupil = gaze.pupil_left_coords()
            right_pupil = gaze.pupil_right_coords()
            cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
            cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

            cv2.imshow("Demo", frame)

            if cv2.waitKey(1) == 27:
                break

    finally:
        webcam.release()
        wheelChair.disconnect_serial()
        cv2.destroyAllWindows()
        logging.info("Resources released and program terminated.")

if __name__ == "__main__":
    main()