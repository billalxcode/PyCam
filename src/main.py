from src.gui import GUI
from src.camera import Camera

class Main(object):
    def __init__(self):
        self.gui = GUI()
        self.camera = Camera()
        self.camera.startVideo()
        self.detectCanny = False
        self.detectFace = False
        self.detectEye = False

    def funcDetectCanny(self):
        if self.detectCanny:
            self.detectCanny = False
            self.gui.btnCan.configure(text="Turn on canny detection")
        else:
            self.detectCanny = True
            self.gui.btnCan.configure(text="Turn off canny detection")
            self.camera.closeWindow()

    def funcDetectFace(self):
        if self.detectFace:
            self.detectFace = False
            self.gui.btnFace.configure(text="Turn on face detection")
        else:
            self.detectFace = True
            self.gui.btnFace.configure(text="Turn off face detection")
            self.camera.closeWindow()

    def funcDetectEye(self):
        if self.detectEye:
            self.detectEye = False
            self.gui.btnEye.configure(text="Turn on face detectoe")
        else:
            self.detectEye = True
            self.gui.btnEye.config(text="Turn off face detector")
            self.camera.closeWindow()

    def video_stream(self):
        ret, frame = self.camera.readVideo(color=True)
        
        if ret:
            if self.detectCanny:
                can = self.camera.convertToCanny(frame)
                self.camera.show("Canny Result: ", can)
            elif self.detectFace:
                rect = self.camera.detectFace()
                self.camera.show("Face", rect)
            elif self.detectEye:
                rect = self.camera.detectEye()
                self.camera.show("Eye", rect)
            else:
                self.camera.closeWindow()
            photo = self.camera.convertToTk(self.camera.convertFromArray(frame))
            self.gui.set_frame(photo)
            self.gui.update()
        self.gui.after(15, self.video_stream)

    def run(self):
        self.gui.createButton(command=self.camera.snapshot)
        self.gui.createButtonCanny(command=self.funcDetectCanny)
        self.gui.createButtonFace(command=self.funcDetectFace)
        self.gui.createButtonEye(command=self.funcDetectEye)
        self.video_stream()
        self.gui.run()
        