from peewee import (Model, CharField, SqliteDatabase, IntegrityError, TextField, IntegerField)

DATABASE = SqliteDatabase("course_registration.db")


class Studentclass(Model):
    student_id = IntegerField()
    classes_id = IntegerField()

    class Meta:
        database = DATABASE