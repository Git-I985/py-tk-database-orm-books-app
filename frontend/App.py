import tkinter as tk
from tkinter import ttk
from frontend.pages.Books import BooksPage
from frontend.pages.Dashboard import DashboardPage
from frontend.pages.Users import UsersPage
from frontend.pages.ProfilePage import ProfilePage


class Tabs(ttk.Notebook):
    def __init__(self, *args, pages, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for Page in pages:
            self.add(Page(self), text=Page.page_title)


class App(tk.Tk):
    def __init__(self):
        """
            db connect
            update table
            table filling function
            fill table

            entities:
                Users
                Books
                Reviews

            pages:
                Dashboard
                Users list page
                User page
                    - userinfo
                    - user books
                    - user books reviews
                Books list page
                Book page
                    - book info
                    - book reviews
        """
        super().__init__()
        self.init_geometry()
        self.init_pages()
        # self.show_frame(DashboardPage)

    def init_geometry(self):
        self.geometry('800x400')
        # tell frame not to let its children control its size
        self.pack_propagate(0)

    def init_pages(self):
        self.tabs = Tabs(self, pages=[
            DashboardPage,
            BooksPage,
            UsersPage,
            ProfilePage,
        ])

        self.tabs.pack(expand=True, fill='both')
