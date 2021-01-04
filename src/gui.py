from tkinter import Canvas
from tkinter import Button
from tkinter import Frame
from tkinter import Tk
from tkinter import NE
from tkinter import NW
from tkinter import CENTER

class GUI(object):
    def __init__(self):
        self.root = Tk()
        self.panel = Canvas(self.root, width=700, height=600)
        self.btnUpFrame = Frame(self.root)
        self.btnUpFrame.grid(row=3, column=0,columnspan=2)
        self.frame = None

    def createButton(self, command):
        self.button = Button(self.btnUpFrame, text="Snapshot", width=20, command=command)
        self.button.grid(row=1, column=2)

    def createButtonCanny(self, command):
        self.btnCan = Button(self.btnUpFrame, text="Turn on canny detection", width=20, command=command)
        self.btnCan.grid(row=1, column=0)
        

    def createButtonFace(self, command):
        self.btnFace = Button(self.btnUpFrame, text="Turn on face detector", width=20, command=command)
        self.btnFace.grid(row=1, column=1)

    def createButtonEye(self, command):
        self.btnEye = Button(self.btnUpFrame, text="Turn on eye detector", width=20, command=command)
        self.btnEye.grid(row=1, column=4)

    def after(self, delay, function):
        self.root.after(delay, function)

    def set_frame(self, frame):
        self.frame = frame

    def update(self):
        self.panel.create_image(30, 0, image=self.frame, anchor=NW)
        
    def run(self):
        self.panel.grid(row=0, column=0)
        
        self.root.title("Video")
        self.root.mainloop()