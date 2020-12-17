from tkinter import *
from tkinter import messagebox
from connectServer import *
from GUI import GUI


class DeleteBook:

    def __init__(self, book_table, issue_table):
        self.book_table = book_table
        self.issue_table = issue_table

    def create_gui(self):
        self.GUI = GUI(page_title="Library", page_width=1000, page_height=500)
        self.GUI.create_canvas(img=None, bg="#006B38")
        head_frame = self.GUI.create_frame(location=(0.25, 0.1, 0.5, 0.13))
        head_label = self.GUI.create_label(frame=head_frame, text="Delete Book", bg="black", fg="white", font_size=15,
                                           location=(0, 0, 1, 1))

        delete_frame = self.GUI.create_frame(location=(0.25, 0.3, 0.5, 0.5), bg="black")

        delete_body = self.GUI.create_label(delete_frame, text="Book ID", bg="black", fg="white", font_size=11,
                                            location=(0.05, 0.5, 0.3, 0.1))
        self.delete_entry = self.GUI.create_entry(delete_frame, location=(0.4, 0.5, 0.3, 0.13))

        self.GUI.create_button(text="SUBMIT", command=self.delete_book, location=(0.28, 0.9, 0.18, 0.08))
        self.GUI.create_button(text="Quit", command=self.GUI.root.destroy, location=(0.53, 0.9, 0.18, 0.08))

    def delete_book(self):
        bid = self.delete_entry.get()

        deleteSql = "delete from " + self.book_table + " where bid = '" + bid + "'"
        deleteIssue = "delete from " + self.issue_table + " where bid = '" + bid + "'"

        con, cur = connectServer()
        try:
            cur.execute(deleteSql)
            con.commit()
            cur.execute(deleteIssue)
            con.commit()
            messagebox.showinfo('Success', "Book Record Deleted Successfully")
        except:
            messagebox.showinfo("Please check Book ID")

        self.delete_entry.delete(0, END)

    def delete(self):

        self.create_gui()

        self.GUI.root.mainloop()
