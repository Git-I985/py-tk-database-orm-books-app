from faker import Faker
import json
import random

fake = Faker()

Faker.seed(12)


def fake_book():
    return {
        "author": fake.name(),
        "name": fake.text(max_nb_chars=60),
        "description": fake.text(),
        "genre": fake.word(),
        "release": fake.date(),
        "isbn": fake.isbn10(),
        "publisher": fake.company(),
    }


def fake_user():
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "password": fake.password(),
        "email": fake.email(),
        "country": fake.country(),
        "age": fake.pyint(9, 100),
        "gender":  random.choice(["female", "male"]),
    }


def fake_reviews():
    return {
        "text": fake.text(),
        "rating": random.randint(1, 5),
        "date": fake.date(),
    }


default_books = [fake_book() for i in range(10)]
default_users = [fake_user() for i in range(10)]
default_reviews = [fake_reviews() for i in range(4)]
