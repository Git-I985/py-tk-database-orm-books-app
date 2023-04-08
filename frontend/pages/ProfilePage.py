from frontend.components.Page import Page


class ProfilePage(Page):
    page_title = 'Профиль'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, page_title=self.page_title, ** kwargs)
        """
        # Если пользователь авторизован тогда показать его данные
            # Книги
            # Отзывы
            # Личные данные
            # Возможность редактировать профиль
        # Иначе показать форму авторизации или регистрации
        """
