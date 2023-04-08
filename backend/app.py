from peewee import *
from backend.defaults import default_books, default_users, default_reviews

db = SqliteDatabase('app.db')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    firstname = TextField()
    lastname = TextField()
    password = TextField()
    email = TextField(unique=True)

    country = TextField()
    age = IntegerField()
    gender = TextField()


class Book(BaseModel):
    author = TextField()
    name = TextField(unique=True)
    description = TextField()
    genre = CharField()
    release = DateField()
    isbn = TextField(unique=True)
    publisher = TextField()


# TODO
class Review(BaseModel):
    author = ForeignKeyField(User, backref='reviews')
    book = ForeignKeyField(Book, backref='reviews')
    text = TextField()
    rating = IntegerField()
    date = DateField()


def create_tables():
    with db:
        db.create_tables([User, Review, Book])


def fill_defaults():
    for user in default_users:
        User.get_or_create(**user, defaults=user)

    for book in default_books:
        Book.get_or_create(**book, defaults=book)

    for review in default_reviews:
        Review.get_or_create(**review, defaults={
            **review,
            "author": User.select().order_by(fn.Random()).limit(1).get().id,
            "book": Book.select().order_by(fn.Random()).limit(1).get().id
        })


create_tables()
