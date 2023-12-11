from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

student_course = db.Table("student_course",
    db.Column("student_id", db.Integer, db.ForeignKey("student.id"), primary_key=True),
    db.Column("course_id", db.Integer, db.ForeignKey("course.id"), primary_key=True)
)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    middle_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    contact_number = db.Column(db.String(15))
    national_id = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True)
    date_of_birth = db.Column(db.String(10))
    gender = db.Column(db.String(10))
    class_level = db.Column(db.String(10))
    password = db.Column(db.String(100))
    courses = db.relationship("Course", secondary=student_course, backref="students")

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    middle_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    contact_number = db.Column(db.String(15))
    national_id = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True)
    date_of_birth = db.Column(db.String(10))
    gender = db.Column(db.String(10))
    password = db.Column(db.String(100))
    courses = db.relationship("Course", backref="professor")

class Assistant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    middle_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    contact_number = db.Column(db.String(15))
    national_id = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True)
    date_of_birth = db.Column(db.String(10))
    gender = db.Column(db.String(10))
    password = db.Column(db.String(100))
    labs = db.relationship("Course", backref="assistant")

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    hours = db.Column(db.Integer)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'))
    assistant_id = db.Column(db.Integer, db.ForeignKey('assistant.id'))

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
