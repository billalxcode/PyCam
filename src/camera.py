import cv2
from cv2 import VideoCapture
from cv2 import imwrite
from cv2 import waitKey as OpenCVWaitKey
from cv2 import cvtColor
from cv2 import COLOR_BGR2RGBA
from cv2 import flip
from cv2 import Canny
from cv2 import imshow
from cv2 import waitKey
from cv2 import destroyAllWindows
from cv2 import CascadeClassifier
from PIL import Image
from PIL import ImageTk

from src.utils import createFilename
from src.utils import getAbsPath
from src.utils import JoinPath

class Camera(object):
    def __init__(self):
        self.video = None

    def __del__(self):
        if self.video.isOpened():
            self.video.release()

    def convertFromArray(self, frame):
        return Image.fromarray(frame)

    def convertToTk(self, frame):
        return ImageTk.PhotoImage(image=frame)

    def convertToCanny(self, frame):
        return Canny(frame, 100, 50)

    def closeWindow(self):
        destroyAllWindows()

    def detectFace(self):
        ret, frame = self.readVideo()
        gray = cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detect = self.faceCascade.detectMultiScale(gray, minSize=(20, 20))
        for (x, y, w, h) in detect:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255,255,0), 2)
        return frame
    
    def detectEye(self):
        ret, frame = self.readVideo()
        gray = cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detect = self.eyecCascade.detectMultiScale(gray, minSize=(20, 20))
        for (x, y, w, h) in detect:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255,255,0), 2)

        return frame

    def snapshot(self):
        ret, frame = self.readVideo()
        if ret:
            filename = createFilename("photo", ".jpg")
            imwrite(filename, frame)
    
    def show(self, title, frame):
        imshow(title, frame)
        waitKey(1)

    def startVideo(self):
        path = JoinPath(getAbsPath() + "assets/data/", "haarcascade_frontalface_default.xml")
        self.video = VideoCapture(0)
        self.faceCascade = CascadeClassifier("assets/data/haarcascade_frontalface_default.xml")
        self.eyecCascade = CascadeClassifier("assets/data/haarcascade_eye.xml")

    def readVideo(self, color=None):
        if self.video.isOpened():
            ret, frame = self.video.read()
            frame = flip(frame, 1)
            if ret:
                if color is None:
                    return (ret, frame)
                else:
                    return (ret, cvtColor(frame, COLOR_BGR2RGBA))
            else:
                return (ret, None)
        else:
            return (ret, None)
