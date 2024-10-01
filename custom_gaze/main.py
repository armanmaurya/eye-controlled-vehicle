"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking
import datetime

class CustomTracking(GazeTracking):
    def __init__(self):
        super().__init__()
        self.blink_count = 0
        self.frames_below_thresh = 0
        

    def isBlinked(self):
        if self.is_blinking():
            self.frames_below_thresh += 1
        else:
            if self.frames_below_thresh >= 3:
                self.blink_count +=1
                self.frames_below_thresh = 0
                return True
            self.frames_below_thresh = 0

        print(self.frames_below_thresh)
        return False
            
        
            