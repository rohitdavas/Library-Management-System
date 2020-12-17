from tkinter import *
from tkinter import messagebox
from connectServer import *
from GUI import GUI
from BackgroundImage import get_background_image


class IssueBook:
    """ issue book"""

    def __init__(self, book_table_name, book_issued_table_name, image_path=None):
        self.book_table_name = book_table_name
        self.book_issued_table_name = book_issued_table_name
        self.image_path = image_path

    def create_gui(self):
        self.GUI = GUI(page_title="Library", page_width=800, page_height=400)
        img = self.image_path if self.image_path is None else get_background_image(self.image_path)
        self.GUI.create_canvas(img, bg="#D6ED17")

        head_frame = self.GUI.create_frame(location=(0.25, 0.1, 0.5, 0.13), bg="#FFBB00")
        self.GUI.create_label(head_frame, text="Issue Book", bg="black", fg="white", font_size=15,
                              location=(0, 0, 1, 1))

        # details frame
        details_frame = self.GUI.create_frame(location=(0.1, 0.3, 0.8, 0.5), bg="black")

        label_bid = self.GUI.create_label(details_frame, "Book ID: ", "black", "white", (0.05, 0.02), 11)
        self.entry_bid = self.GUI.create_entry(details_frame, (0.3, 0.02, 0.5, 0.1))

        label_student_name = self.GUI.create_label(details_frame, "Student name: ", "black", "white", (0.05, 0.4), 11)
        self.entry_student = self.GUI.create_entry(details_frame, (0.3, 0.4, 0.5, 0.1))

        self.GUI.create_button(text="Issue", command=self.issue, location=(0.28, 0.9, 0.18, 0.08))
        self.GUI.create_button(text="Quit", command=self.GUI.root.destroy, location=(0.53, 0.9, 0.18, 0.08))

    def issue(self):

        bid = self.entry_bid.get()
        student_name = self.entry_student.get()

        bid_query = "select bid from " + self.book_table_name
        status_query = "select status from " + self.book_table_name
        issue_sql = "insert into " + self.book_issued_table_name + " values ('" + bid + "','" + student_name + "')"

        update_sql = f"update {self.book_table_name} set status = 'issued' where bid = {bid}"


        try:
            con, cur = connectServer()

            cur.execute(bid_query)
            con.commit()
            all_bids = [x[0] for x in cur]
            print(all_bids)

            if bid in all_bids:
                cur.execute(status_query)
                con.commit()
                all_status = [x[0] for x in cur]
                index = all_bids.index(bid)

                if all_status[index] == 'available':
                    cur.execute(issue_sql)
                    con.commit()
                    cur.execute(update_sql)
                    con.commit()
                    messagebox.showinfo('Success', "Book Issued Successfully")

                else:
                    messagebox.showinfo('Message', "Book Already Issued")

            else:
                messagebox.showinfo("Error", "Book ID not present")
        except:
            messagebox.showinfo("Error", "Can't fetch Book IDs")

        self.entry_bid.delete(0, END)
        self.entry_student.delete(0, END)

    def issue_book(self):
        self.create_gui()
        self.GUI.root.mainloop()
