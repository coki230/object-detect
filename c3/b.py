from tkinter import *
from PIL import ImageGrab, ImageTk, Image
from numpy import array
import os

class App(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.overrideredirect(1) # FRAMELESS CANVAS WINDOW

        self.width = 900
        self.height = 640
        self.img = Image.open("2.jpg").resize((self.width, self.height))
        self.pimg = ImageTk.PhotoImage(self.img)
        self.initialize()

    def initialize(self):
        self.c = Canvas(self, width=self.width, height=self.height, background='white')
        self.c.pack(side=RIGHT, expand=YES, fill=BOTH)
        self.c.create_image(0, 0, anchor='nw', image=self.pimg)
        self.run_anim() # RUN ANIMATION METHOD

    def run_anim(self):
        self.c.update()
        ImageGrab.grab((0,0,self.width,self.height)).save("savename" + '.jpg')

app = App(None)
app.mainloop()