from peewee import (Model, CharField, SqliteDatabase, IntegrityError, TextField)

DATABASE = SqliteDatabase("course_registration.db")


class Classes(Model):
    title = CharField(max_length=200, unique=True)
    description = TextField()
    class Meta:
        database = DATABASE