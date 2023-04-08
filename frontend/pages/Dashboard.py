from frontend.components.Page import Page
import tkinter as tk
import tkinter.ttk as ttk
from backend.app import Book, User, Review


class DashboardPage(Page):
    page_title = 'Главная'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, page_title=self.page_title, ** kwargs)
        # self.title("Ttk Treeview")

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=1)

        self.update()

    def clear(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def update(self):
        self.clear()

        new_books_frame = ttk.LabelFrame(
            self.container, text='Новые книги')

        new_books_frame.pack(fill='both', expand=1)

        new_books_frame.pack_propagate(False)

        new_reviews_frame = ttk.LabelFrame(
            self.container, text='Новые отзывы')

        new_reviews_frame.pack(fill='both', expand=1)

        new_reviews_frame.pack_propagate(False)

        new_books_frame_columns = (
            "reviews",
            "author",
            "name",
            # "description",
            "genre",
            "release",
            "isbn",
            "publisher",
        )

        new_books_table = ttk.Treeview(new_books_frame, show="headings",
                                       columns=new_books_frame_columns)

        new_books_table.heading("reviews", text="оценки")
        new_books_table.heading("author", text="Автор")
        new_books_table.heading("name", text="Название")
        # tree.heading("description", text="Описание")
        new_books_table.heading("genre", text="Жанр")
        new_books_table.heading("release", text="Дата выхода")
        new_books_table.heading("isbn", text="ISBN")
        new_books_table.heading("publisher", text="Издательство")

        # SCROLLBARSTART

        new_books_table_ysb = ttk.Scrollbar(new_books_table, orient=tk.VERTICAL,
                                            command=new_books_table.yview)
        new_books_table.configure(yscroll=new_books_table_ysb.set)
        new_books_table_ysb.pack(side='right', fill='y')

        new_books_table_xsb = ttk.Scrollbar(new_books_table, orient=tk.HORIZONTAL,
                                            command=new_books_table.xview)
        new_books_table.configure(xscroll=new_books_table_xsb.set)
        new_books_table_xsb.pack(side='bottom', fill='x')

        # SCROLLBAREND

        for book in Book.select():
            new_books_table.insert("", tk.END, values=[
                len(book.reviews) or 'нет оценок',
                book.author,
                book.name,
                # book.description,
                book.genre,
                book.release,
                book.isbn,
                book.publisher,
            ])

        new_books_table.pack(expand=1, fill='both', padx=10, pady=10)

        # REVIEWS

        new_reviews_table_columns = (
            "author",
            "book",
            "rating",
            "comment",
            "date",
        )

        new_reviews_table = ttk.Treeview(new_reviews_frame, show="headings",
                                         columns=new_reviews_table_columns)

        new_reviews_table.heading("book", text="Книга")
        new_reviews_table.heading("author", text="Автор")
        new_reviews_table.heading("rating", text="Оценка")
        # tree.heading("description", text="Описание")
        new_reviews_table.heading("comment", text="Комментарий")
        new_reviews_table.heading("date", text="Дата отзыва")

        # SCROLLBARSTART

        new_reviews_table_ysb = ttk.Scrollbar(new_reviews_table, orient=tk.VERTICAL,
                                              command=new_reviews_table.yview)
        new_reviews_table.configure(yscroll=new_reviews_table_ysb.set)
        new_reviews_table_ysb.pack(side='right', fill='y')

        new_reviews_table_xsb = ttk.Scrollbar(new_reviews_table, orient=tk.HORIZONTAL,
                                              command=new_reviews_table.xview)
        new_reviews_table.configure(xscroll=new_reviews_table_xsb.set)
        new_reviews_table_xsb.pack(side='bottom', fill='x')

        # SCROLLBAREND

        # TODO top 10
        # TODO popup
        for review in Review.select():
            new_reviews_table.insert("", tk.END, values=[
                review.author.firstname + ' ' + review.author.lastname,
                review.book.name,
                str(review.rating) + '/5',
                review.text,
                review.date,
            ])

        new_reviews_table.pack(expand=1, fill='both', padx=10, pady=10)
