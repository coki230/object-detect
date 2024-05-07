import os.path
import uuid
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageGrab
import win32ui
import cv2

class App:
    def __init__(self):

        self.window = Tk()
        self.split = "  "
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
        self.img_label_info = []
        self.pimg = None
        self.current_img_num = None
        self.canvas = None
        self.load_canvas()
        self.labels = []
        self.label_index = IntVar()
        self.label_name = StringVar()
        # self.frame = Frame

        # set the label
        Entry(self.window, textvariable=self.label_index).grid(row=1, column=0)
        Entry(self.window, textvariable=self.label_name).grid(row=1, column=1)
        Button(self.window, text="addLabel", command=self.add_label).grid(row=1, column=2)

        Entry(self.window, textvariable=self.path).grid(row=2, column=0)
        Button(self.window, text="loadImg", command=self.load_img).grid(row=2, column=1)

        self.cmb_train_or_val = ttk.Combobox(self.window)
        self.cmb_train_or_val.grid(row=3, column=0)
        self.cmb_train_or_val['value'] = ("train", "val")
        self.cmb_type = ttk.Combobox(self.window)
        self.cmb_type.grid(row=3, column=1)
        Button(self.window, text="next", command=self.next_img).grid(row=3, column=2)
        self.label = Label(self.window)
        self.label.grid(row=3, column=3)
        self.label_all = Label(self.window)
        self.label_all.grid(row=3, column=4)


    def add_label(self):
        self.labels.append(str(self.label_index.get()) + "-" + self.label_name.get())
        self.label_index.set(self.label_index.get() + 1)
        self.label_name.set('')
        self.cmb_type['value'] = self.labels

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

    def get_label_format_data(self):
        center_x = (self.end_x - self.star_x) / 2 / self.img_resize_x
        center_y = (self.end_y - self.star_y) / 2 / self.img_resize_y
        width = (self.end_x - center_x) / 2 / self.img_resize_x
        height = (self.end_y - center_y) / 2 / self.img_resize_y
        return str(center_x) + self.split + str(center_y) + self.split + str(width) + self.split + str(height)

    def mouse_release(self, event):
        self.draw_rectangle(event, "release")
        self.img_label_info.append(self.cmb_type.get().split("-")[0] + self.split + self.get_label_format_data())
        print(self.star_x, self.star_y, self.end_x, self.end_y)
        print(self.cmb_type.get())

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
        if self.current_img_num is None:
            self.current_img_num = 0
        else:
            # generate the img and the label
            file_name = str(uuid.uuid1())
            type = self.cmb_train_or_val.get() if self.cmb_train_or_val.get() is not None else "train"
            self.img.save(self.path.get() + "\\images\\" + type + "\\" + file_name + ".jpg")
            with open(self.path.get() + "\\labels\\" + type + "\\" + file_name + ".txt", 'w') as file:
                for line in self.img_label_info:
                    file.write(line + "\n")
            self.img_label_info = []

        if self.current_img_num > len(self.items) - 1:
            self.label.config(text="all pic have labeled")
        else:
            self.label.config(text=self.current_img_num)
            self.img_show(self.current_img_num)
            self.current_img_num = self.current_img_num + 1


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
        self.path.set("C:\\Users\\UX506994\\Desktop\\pic")

        path = self.path.get()
        if os.path.isdir(path):
            self.items = os.listdir(path)
        self.next_img()
        self.label_all.config(text=len(self.items))
        self.check_and_make_dir()

    def check_and_make_dir(self):
        if not os.path.exists(self.path.get() + "\\images"):
            os.mkdir(self.path.get() + "\\images")
        if not os.path.exists(self.path.get() + "\\labels"):
            os.mkdir(self.path.get() + "\\labels")
        if not os.path.exists(self.path.get() + "\\images\\train"):
            os.mkdir(self.path.get() + "\\images\\train")
        if not os.path.exists(self.path.get() + "\\images\\val"):
            os.mkdir(self.path.get() + "\\images\\val")
        if not os.path.exists(self.path.get() + "\\labels\\train"):
            os.mkdir(self.path.get() + "\\labels\\train")
        if not os.path.exists(self.path.get() + "\\labels\\val"):
            os.mkdir(self.path.get() + "\\labels\\val")




    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()


