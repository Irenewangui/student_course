from models.classes import Classes
from models.student import Student
from models.student_class import Studentclass
from faker import Faker
from peewee import SqliteDatabase, IntegrityError

DATABASE = SqliteDatabase("course_registration.db")


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Classes, Student, Studentclass], safe=True)
    try:
        fake = Faker()
      
        for i in range(10):
            Student.create(
                name=fake.name(),
                email=fake.email(),
                age=20
            )
        
    except IntegrityError:
        pass
    try:
        Classes.create(
            title="Python",
            description="Learning the beautiful language"
        )
        Classes.create(
            title="Javascript",
            description="Language of the web"
        )
    except IntegrityError:
        pass

    DATABASE.close()