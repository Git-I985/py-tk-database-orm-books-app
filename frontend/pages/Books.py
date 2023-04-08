from frontend.components.Page import Page


class BooksPage(Page):
    page_title = 'Книги'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, page_title=self.page_title, ** kwargs)
