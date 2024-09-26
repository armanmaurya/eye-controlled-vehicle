"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking

class CustomTracking(GazeTracking):
    def __init__(self):
        super().__init__()

    def isBlinked(self):
        print("This is a custom function")