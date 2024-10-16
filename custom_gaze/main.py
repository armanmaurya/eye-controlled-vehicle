"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import threading
import cv2
from gaze_tracking import GazeTracking
import datetime

class CustomTracking(GazeTracking):
    def __init__(self):
        super().__init__()
        self.blink_count = 0
        self.frames_below_thresh = 0
        self.last_blink_time = datetime.datetime.now()
        self.blink_reset_threshold = datetime.timedelta(seconds=0.5)  # Reset threshold time
        self.final_blink_count = 0
        self.final_detection_timer = None  # Timer to detect final blink sequence
        

    def DetectBlink(self):
        current_time = datetime.datetime.now()

        # # Reset blink count if time since last blink exceeds threshold
        # if current_time - self.last_blink_time > self.blink_reset_threshold:
        #     self.blink_count = 0

        if self.is_blinking():
            self.frames_below_thresh += 1
        else:
            if self.frames_below_thresh <= 7 and self.frames_below_thresh > 0:
                self.blink_count +=1
                self.frames_below_thresh = 0
                self.last_blink_time = current_time  # Update last blink time

                if self.final_detection_timer:
                    self.final_detection_timer.cancel()
                
                self.final_detection_timer  = threading.Timer(1, self.set_final_blink_count)
                self.final_detection_timer.start()  # Start a new timer

                # return True
            self.frames_below_thresh = 0

        # print(self.frames_below_thresh)
        # return False

    def set_final_blink_count(self):
        self.final_blink_count = self.blink_count
        self.blink_count = 0
        print("Final blink count:", self.final_blink_count, self.blink_count)
            
        
            