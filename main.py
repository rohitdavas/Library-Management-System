from tkinter import *
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
from connectServer import *

from BackgroundImage import get_background_image
from GUI import GUI
from AddBook import AddBook
from DeleteBook import DeleteBook
from ViewBooks import ViewBook
from IssueBook import IssueBook
from ReturnBook import ReturnBook
from viewIssued import ViewIssued

class Library:
    """ IIT Jammu library """

    def __init__(self, image_path, min_width=400, min_height=400):
        self.con, self.cur = connectServer()

        self.image_path = image_path
        self.title = "Library"

        # database table names
        database_name = "Library2"
        self.books_table_name = "books"
        self.issued_books_table_name = "books_issued"
        create_new_db(name=database_name, books_table_name=self.books_table_name, books_issued_table_name=self.issued_books_table_name)

        # initialise the root frame of tkinter
        self.main_page = GUI(page_title=self.title)
        self.add_book_page = AddBook(bookTableName=self.books_table_name,
                                     bookIssuedTableName=self.issued_books_table_name)
        self.delete_page = DeleteBook(book_table=self.books_table_name, issue_table=self.issued_books_table_name)
        self.view_page = ViewBook(self.books_table_name, self.issued_books_table_name)
        self.issue_page = IssueBook(self.books_table_name, self.issued_books_table_name)
        self.return_page = ReturnBook(self.books_table_name, self.issued_books_table_name)
        self.issued_page = ViewIssued(self.books_table_name, self.issued_books_table_name)

    def main(self):
        # get background image
        img = get_background_image(self.image_path)
        # create a basic canvas
        canvas1 = self.main_page.create_canvas(img)
        self.main_page.create_head_frame(text="Welcome to IIT Jammu Library")
        # add buttons to it
        self.main_page.create_button(text="Add book details", command=self.add_book_page.add_book,location=(0.28, 0.3, 0.45, 0.1))
        self.main_page.create_button(text="Delete Book", command=self.delete_page.delete,location=(0.28, 0.4, 0.45, 0.1))
        self.main_page.create_button(text="View Book List", command=self.view_page.view,location=(0.28, 0.5, 0.45, 0.1))
        self.main_page.create_button(text="View Issued List", command=self.issued_page.view, location=(0.28, 0.6, 0.45, 0.1))
        self.main_page.create_button(text="Issue Book to Student", command=self.issue_page.issue_book, location=(0.28, 0.7, 0.45, 0.1))
        self.main_page.create_button(text="Return Book", command=self.return_page.return_book, location=(0.28, 0.8, 0.45, 0.1))
        self.main_page.create_button(text="Quit", command=self.main_page.root.destroy, location=(0.28, 0.9, 0.45, 0.1))
        # loop it over
        self.main_page.root.mainloop()


if __name__ == "__main__":
    library = Library(image_path="Images/black.jpg", min_width=1000, min_height=400)
    library.main()
