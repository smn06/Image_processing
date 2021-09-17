import cv2
from managers import WindowManager, CaptureManager
import filters
import depth

class Cameo(object):
    def __init__(self):
        self._windowManager = WindowManager('Cameo', self.onKeyPress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)
        self._curveFilter = filters.BGRPortraCurveFilter()

    def run(self):
        """ Run the main loop."""
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            # filtering the frame
            filters.strokeEdges(frame, frame)
            self._curveFilter.apply(frame, frame)

            self._captureManager.exitFrame()
            self._windowManager.processEvents()

    def onKeyPress(self, keycode):
        """ Handle a keypress.

        space -> Take a screenshot.
        tab -> Start/Stop recording a screencast.
        escape -> Quit.

        """

        if keycode == 32: # Space
            self._captureManager.writeImage('screen-shot.png')
        elif keycode == 9: # Tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('screencast.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27: # escape
            self._windowManager.destroyWindow()

"""
class CameoDepth(Cameo):
    def __init__(self):
        self._windowManager= WindowManager('Cameo',self.onKeyPress)
        device=cv2.CAP_OPENNI2_ASUS
        self._captureManager=CaptureManager(cv2.VideoCapture(0),self._windowManager,True)
        self._curveFilter=filters.BGRPortraCurveFilter()
    
    def run(self):
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            
            self._captureManager.channel=cv2.CAP_OPENNI_DISPARITY_MAP
            disparityMap=self._captureManager.frame
            
            self._captureManager.channel=cv2.CAP_OPENNI_VALID_DEPTH_MASK
            validDepthMask=self._captureManager.frame
            
            self._captureManager.channel=cv2.CAP_OPENNI_BGR_IMAGE
            frame=self._captureManager.frame
            if frame is None:
                self._captureManager.channel=cv2.CAP_OPENNI_IR_IMAGE
                frame=self._captureManager.frame
            if frame is not None:    
                mask=depth.createMedianMask(disparityMap,validDepthMask)
                frame[mask==0]= 0
                
                if self._captureManager.channel==cv2.CAP_OPENNI_BGR_IMAGE:
                    filters.strokeEdges(frame,frame)
                    self._curveFilter.apply(frame,frame)
                
            self._captureManager.exitFrame()
            self._windowManager.processEvents()

"""

if __name__ == "__main__":
    Cameo().run()
    #CameoDepth().run()
