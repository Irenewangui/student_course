from peewee import (Model, CharField, SqliteDatabase, IntegrityError, TextField)

DATABASE = SqliteDatabase("course_registration.db")


class Student(Model):
    name = CharField(max_length=200)
    age = CharField(max_length=200)
    email = CharField(max_length=200, unique=True)

    class Meta:
        database = DATABASE