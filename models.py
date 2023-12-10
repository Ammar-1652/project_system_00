from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True )
    name = db.Column(db.String(100))
    hours = db.Column(db.Integer)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'))
    assistant_id = db.Column(db.Integer, db.ForeignKey('assistant.id'))
    student_id =db.Column(db.Integer,db.ForeignKey('student.id'))
    
    professor = db.relationship('Professor', backref=db.backref('courses', lazy=True))
    assistant = db.relationship('Assistant', backref=db.backref('courses', lazy=True))
    student   =db.relationship('Student',backref=db.backref('Courses',lazy=True))

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))

class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'))
    assistant_id = db.Column(db.Integer, db.ForeignKey('assistant.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

    student = db.relationship('Student', backref=db.backref('enrollments', lazy=True))
    professor = db.relationship('Professor', backref=db.backref('enrollments', lazy=True))
    assistant = db.relationship('Assistant', backref=db.backref('enrollments', lazy=True))
    course = db.relationship('Course', backref=db.backref('enrollments', lazy=True))