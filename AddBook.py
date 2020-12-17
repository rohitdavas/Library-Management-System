from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql

from connectServer import *
from GUI import GUI


class AddBook:
    """ a class that handles book adding"""

    def __init__(self, bookTableName, bookIssuedTableName):

        self.bookTableName = bookTableName
        self.bookIssuedTableName = bookIssuedTableName

    def book_register(self, ):

        bid = self.entry_bid.get()
        title = self.entry_title.get()
        author = self.entry_author.get()
        status = self.entry_status.get()
        status = status.lower()

        con, cur = connectServer()

        insert_books = "insert into " + self.bookTableName + " values('" + bid + "','" + title + "','" + author + "','" + status + "')"
        try:
            cur.execute(insert_books)
            con.commit()
            messagebox.showinfo('Success', "Book added successfully")
        except:
            messagebox.showinfo("Error", "Can't add data into Database")

        self.entry_bid.delete(0, END)
        self.entry_title.delete(0, END)
        self.entry_author.delete(0, END)

    def create_gui(self):
        self.GUI = GUI(page_title="Library", page_width=1500, page_height=750)

        # canvas
        self.GUI.create_canvas(img=None, bg="#ff6e40")

        # head_frame
        # location at (x,y) = (0.2,0.1) and (width, height)=(0.6,0.16)
        head_frame = self.GUI.create_frame(location=(0.2, 0.1, 0.6, 0.16))
        label = self.GUI.create_label(head_frame, text="Add Books", bg=self.GUI.button_background,
                                      fg=self.GUI.button_foreground, location=(0, 0, 1, 1), font_size=15)

        # books details frame
        # location at (x,y) = (0.1,0.4), (width, height) = (0.8,0.4)
        books_frame = self.GUI.create_frame(location=(0.1, 0.4, 0.8, 0.4), bg="black")

        # take input from user
        # bid, title, author, status

        label_bid = self.GUI.create_label(frame=books_frame, text="Book ID : ", bg="black", fg="white",
                                          location=(0.05, 0.2, 0.08, 0.08), font_size=11)

        self.entry_bid = self.GUI.create_entry(frame=books_frame, location=(0.3, 0.2, 0.62, 0.08))

        label_title = self.GUI.create_label(frame=books_frame, text="Title: ", bg="black", fg="white",
                                            location=(0.05, 0.35, 0.08, 0.08), font_size=11)
        self.entry_title = self.GUI.create_entry(frame=books_frame, location=(0.3, 0.35, 0.62, 0.08))

        label_author = self.GUI.create_label(frame=books_frame, text="Author: ", bg="black", fg="white",
                                             location=(0.05, 0.50, 0.08, 0.08), font_size=11)
        self.entry_author = self.GUI.create_entry(frame=books_frame, location=(0.3, 0.5, 0.62, 0.08))

        label_status = self.GUI.create_label(frame=books_frame, text="Status(Avail/issued): ", bg="black", fg="white",
                                             location=(0.05, 0.65, 0.08, 0.08), font_size=11)
        self.entry_status = self.GUI.create_entry(frame=books_frame, location=(0.3, 0.65, 0.62, 0.08))
        self.entry_status.insert(0, "Available")

    def add_book(self):
        self.create_gui()
        # Submit Button
        self.GUI.create_button(text="SUBMIT", command=self.book_register, location=(0.28, 0.9, 0.18, 0.08))
        self.GUI.create_button(text="Quit", command=self.GUI.root.destroy, location=(0.53, 0.9, 0.18, 0.08))
        self.GUI.root.mainloop()
