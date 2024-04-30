import os.path
from tkinter import *
from PIL import Image, ImageTk, ImageGrab
import win32ui
import cv2

class App:
    def __init__(self):

        self.window = Tk()
        self.star_x = None
        self.star_y = None
        self.end_x = 0
        self.end_y = 0
        self.move_id = None
        self.window.geometry("750x550")
        self.img_resize_x = 300
        self.img_resize_y = 300
        self.path = StringVar()
        self.items = None

        self.img = None
        self.pimg = None
        self.current_img_num = None
        self.canvas = None
        self.load_canvas()
        # self.frame = Frame

        Entry(self.window, textvariable=self.path).grid(row=1, column=0)
        Button(self.window, text="loadImg", command=self.load_img).grid(row=1, column=1)
        Button(self.window, text="next", command=self.next_img).grid(row=2, column=0)

    def load_canvas(self):
        self.canvas = Canvas(self.window, height=self.img_resize_y, width=self.img_resize_x)
        self.canvas.create_image(0, 0, anchor='nw')
        self.canvas.grid(row=0, column=0)
        self.canvas.bind("<ButtonPress-1>", self.mouse_press)
        self.canvas.bind("<ButtonRelease-1>", self.mouse_release)
        self.canvas.bind("<B1-Motion>", self.mouse_move)


    def mouse_press(self, event):
        self.star_x = event.x
        self.star_y = event.y

    def mouse_move(self, event):
        self.draw_rectangle(event, "move")

    def mouse_release(self, event):
        self.draw_rectangle(event, "release")
        print(self.star_x, self.star_y, self.end_x, self.end_y)

    def draw_rectangle(self, event, type):
        if self.move_id is not None:
            self.canvas.delete(self.move_id)
        self.end_x = event.x
        self.end_y = event.y
        if type == "release":
            self.canvas.create_rectangle(self.star_x, self.star_y, self.end_x, self.end_y, outline="red")
        else:
            self.move_id = self.canvas.create_rectangle(self.star_x, self.star_y, self.end_x, self.end_y, outline="green")

    def img_show(self, num):
        self.load_canvas()
        if self.items is not None and num < len(self.items):
            self.img = Image.open(self.path.get() + "/" + self.items[num]).resize((self.img_resize_x, self.img_resize_y))
            self.pimg = ImageTk.PhotoImage(self.img)
            self.canvas.create_image(0, 0, anchor='nw', image=self.pimg)


    def next_img(self):
        self.current_img_num = self.current_img_num + 1
        self.img_show(self.current_img_num)

    def load_img(self):
        # self.canvas.postscript(file="test.eps")
        # save_img = Image.open("test.eps")
        # save_img_rgb = save_img.convert("RGB")
        # save_img_rgb.save("img.png")

        # self.window.update()  # UPDATE THE CANVAS DISPLAY
        # x = self.canvas.winfo_rootx()
        # y = self.canvas.winfo_rooty()
        # x1 = x + self.canvas.winfo_width()
        # y1 = y + self.canvas.winfo_height()
        # print(x,y,x1,y1)
        # print(self.canvas.info)
        # ImageGrab.grab().crop((x,y,x1,y1)).save("aaa.jpg")
        # bb = self.canvas.bbox()
        # ImageGrab.grab(bb).save("bbb.jpg")
        path = self.path.get()
        if os.path.isdir(path):
            self.items = os.listdir(path)
        self.current_img_num = 0
        self.img_show(num=self.current_img_num)




    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()


