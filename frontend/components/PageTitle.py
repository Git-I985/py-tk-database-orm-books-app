from tkinter import ttk


class PageTitle(ttk.Label):
    def __init__(self, *args, title, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.configure(text=title)
