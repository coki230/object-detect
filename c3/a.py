import time
from tkinter import *
from PIL import Image, ImageTk

class App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("750x550")
        self.img = Image.open("2.jpg")
        self.pimg = ImageTk.PhotoImage(self.img)
        self.text = "aaff"
        self.label = Label(self.window, text="12323", image=self.pimg)
        self.label.pack()
        Button(self.window, text=self.text, command=self.window.destroy).pack()
        Button(self.window, text="add", command=self.update_label).pack()

    def update_label(self):
        self.img = Image.open("3.png")
        self.pimg = ImageTk.PhotoImage(self.img)
        self.label.config(image=self.pimg)
        self.window.update()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()


