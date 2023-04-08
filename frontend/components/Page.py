import tkinter as tk
from frontend.components.PageTitle import PageTitle


class Page(tk.Frame):
    def __init__(self, *args, page_title, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(padx=20)
        self.configure(pady=20)
        # page_title = PageTitle(self, title=page_title)
        # page_title.pack(anchor='nw')
