from tkinter import *


class GUI:
    """ the common GUI """

    def __init__(self, page_title, page_width=400, page_height=400):
        self.root = self.get_root(title=page_title, width=page_width, height=page_height)

        # style related parameters
        self.button_background = "black"
        self.button_foreground = "white"
        self.font = ("Courier", 15)

    def get_root(self, title, width, height):
        """ gives the root form """
        root_gui = Tk()
        root_gui.title(title)
        root_gui.minsize(width=width, height=height)
        root_gui.geometry("600x500")
        return root_gui

    def create_canvas(self, img, bg="white"):
        """creates a base canvas"""
        x = Canvas(self.root)
        if img is not None:
            x.create_image(300, 340, image=img)
            x.config(bg=bg, width=img.width(), height=img.height())
        else:
            x.config(bg=bg)
        x.pack(expand=True, fill=BOTH)

    def create_frame(self, location, bg="#FFBB00", bd=5):
        frame = Frame(self.root, bg=bg, bd=bd)
        r_x, r_y, r_w, r_h = location
        frame.place(relx=r_x, rely=r_y, relwidth=r_w, relheight=r_h)
        return frame

    def create_label(self, frame, text, bg, fg, location, font_size=15):
        label = Label(frame, text=text, bg=bg, fg=fg, font=('Courier', font_size))
        if len(location) == 4:
            label.place(relx=location[0], rely=location[1], relwidth=location[2], relheight=location[3])
        elif len(location) == 3:
            label.place(relx=location[0], rely=location[1], relheight=location[2])
        elif len(location) == 2:
            label.place(relx=location[0], rely=location[1])
        return label

    def create_head_frame(self, text):
        frame = self.create_frame(location=(0.2, 0.1, 0.6, 0.16))
        label = self.create_label(frame, text, bg=self.button_background, fg=self.button_foreground,
                                  location=(0, 0, 1, 1))

    def create_button(self, text, command, location, bg=None, fg=None):
        r_x, r_y, r_w, r_h = location
        if bg is None and fg is None:
            btn1 = Button(self.root, text=text, bg=self.button_background, fg=self.button_foreground, command=command)
        else:
            btn1 = Button(self.root, text=text, bg=bg, fg=bg, command=command)
        btn1.place(relx=r_x, rely=r_y, relwidth=r_w, relheight=r_h)

    def create_entry(self, frame, location):
        entry = Entry(frame)
        entry.place(relx=location[0], rely=location[1], relwidth=location[2], relheight=location[3])
        return entry
