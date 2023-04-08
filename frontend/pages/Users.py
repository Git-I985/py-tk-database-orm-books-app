from frontend.components.Page import Page


class UsersPage(Page):
    page_title = 'Пользователи'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, page_title=self.page_title, ** kwargs)
