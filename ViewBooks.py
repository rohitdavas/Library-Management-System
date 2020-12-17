from tkinter import *
from tkinter import messagebox
from connectServer import *
from GUI import GUI


class ViewBook:

    def __init__(self, book_table, issue_table):
        self.book_table = book_table
        self.issue_table = issue_table
        self.GUI = None

    def create_gui(self):
        self.GUI = GUI(page_title="Library", page_width=1000, page_height=500)
        self.GUI.create_canvas(img=None, bg="#12a4d9")
        head_frame = self.GUI.create_frame(location=(0.25, 0.1, 0.5, 0.13), bg="#FFBB00")
        self.GUI.create_label(head_frame, "Books", "black", "white", (0, 0, 1, 1), 15)

        details_frame = self.GUI.create_frame(location=(0.1, 0.3, 0.8, 0.6), bg="black")
        columns = "BID\t\tTitle\t\tAuthor\t\t\tStatus"
        self.GUI.create_label(details_frame, text=columns, location=(0.07, 0.1), bg="black", fg="white", font_size=11)
        columns = "-----------------------------------------------------------------------------"
        self.GUI.create_label(details_frame, text=columns, location=(0.05, 0.2), bg="black", fg="white", font_size=11)
        y = 0.25

        con, cur = connectServer()
        query = "SELECT * FROM " + self.book_table
        print(query)
        try:
            cur.execute(query)
            con.commit()
            for i in cur:
                text = self.format_string(i)
                self.GUI.create_label(details_frame, text, location=(0.07, y), bg="black", fg="white", font_size=11)
                y += 0.05
        except:
            messagebox.showinfo("Failed to fetch data from database")

        self.GUI.create_button(text="Quit", command=self.GUI.root.destroy, location=(0.1, 0.9, 0.18, 0.08))
        self.GUI.create_button(text="Refresh",command = self.refresh, location = (0.4, 0.9, 0.18, 0.08))

    def refresh(self):
        if self.GUI :
            self.GUI.root.destroy()
        self.view()

    def format_string(self, i ):
        text = f"{i[0]} {' ' * (12 - len(i[0]))}"
        text += f"{i[1]} {' ' * (17 - len(i[1]))}"
        text += f"{i[2]}  {' ' * (25 - len(i[2]))}"
        text += f"{i[3]}  {' ' * (17 - len(i[1]))}"
        return text

    def view(self):
        self.create_gui()
        self.GUI.root.mainloop()
