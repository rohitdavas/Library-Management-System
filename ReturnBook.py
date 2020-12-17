from tkinter import *
from tkinter import messagebox
from connectServer import *
from GUI import GUI

class ReturnBook:
    """ issue book"""

    def __init__(self, book_table_name, book_issued_table_name, image_path=None):
        self.book_table_name = book_table_name
        self.book_issued_table_name = book_issued_table_name
        self.image_path = image_path

    def create_gui(self):
        self.GUI = GUI(page_title="Library", page_width=800, page_height=400)
        self.GUI.create_canvas(img=None, bg="#FFBB00")

        head_frame = self.GUI.create_frame(location=(0.25, 0.1, 0.5, 0.13), bg="#FFBB00")
        self.GUI.create_label(head_frame, text="Return Book", bg="black", fg="white", font_size=15,
                              location=(0, 0, 1, 1))

        # details frame
        details_frame = self.GUI.create_frame(location=(0.1, 0.3, 0.8, 0.5), bg="black")

        label_bid = self.GUI.create_label(details_frame, "Book ID: ", "black", "white", (0.05, 0.02), 11)
        self.entry_bid = self.GUI.create_entry(details_frame, (0.3, 0.02, 0.5, 0.1))

        self.GUI.create_button(text="Return", command=self.return_, location=(0.28, 0.9, 0.18, 0.08))
        self.GUI.create_button(text="Quit", command=self.GUI.root.destroy, location=(0.53, 0.9, 0.18, 0.08))

    def return_(self):

        bid = self.entry_bid.get()
        bid_query = "select bid from " + self.book_issued_table_name
        status_query = "select status from " + self.book_table_name + " where bid = '"+bid+"'"
        update_sql = f"update {self.book_table_name} set status = 'available' where bid = {bid}"
        delete_sql = "delete from "+self.book_issued_table_name+" where bid = '"+bid+"'"
        # print(status_query)


        try:
            con, cur = connectServer()

            cur.execute(bid_query)
            con.commit()
            all_bids = [x[0] for x in cur]

            if bid in all_bids:
                cur.execute(status_query)
                con.commit()
                all_status = [x[0] for x in cur]
                index = all_bids.index(bid)

                if all_status[index] == 'issued':
                    cur.execute(delete_sql)
                    con.commit()
                    cur.execute(update_sql)
                    con.commit()
                    messagebox.showinfo('Success', "Book returned Successfully")

                else:
                    messagebox.showinfo('Message', "Book Already returned.")

            else:
                messagebox.showinfo("Error", "Book ID not present")
        except:
            messagebox.showinfo("Error", "Can't fetch Book IDs")

        self.entry_bid.delete(0, END)


    def return_book(self):
        self.create_gui()
        self.GUI.root.mainloop()


