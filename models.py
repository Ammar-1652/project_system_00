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
    national_id = db.Column(db.String(20),unique=True)
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
    national_id = db.Column(db.String(20),unique=True)
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
    national_id = db.Column(db.String(20),unique=True)
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


from relations import *
def get_student_by_id(id_):
    with app.app_context(id):
        student=Student.query.filter_by(id=id_).first()
    return student
def get_students_by_first_name(first_name_):
    with app.app_context():
        students=Student.query.filter_by(first_name=first_name_).all()
    return students

def get_students_by_middle_name(middle_name_):
    with app.app_context():
        students=Student.query.filter_by(middle_name=middle_name_).all()
    return students

def get_students_by_last_name(last_name_):
    with app.app_context():
        students=Student.query.filter_by(last_name=last_name_).all()
    return students

def get_student_by_contact_number(contact_number_):
    with app.app_context():
        student=Student.query.filter_by(contact_number=contact_number_).first()
    return student

def get_student_by_national_id(national_id_):
    with app.app_context():
        student=Student.query.filter_by(national_id_=national_id_).first()
    return student    

def get_student_by_email(email_):
    with app.app_context():
        student=Student.query.filter_by(email=email_).first()
    return student

def get_students_by_date_of_birth(date_of_birth_):
    with app.app_context():
        student=Student.query.filter_by(date_of_birth=date_of_birth_).first()
    return student
#====================================================================


#==================Professor====================================
def get_prof_by_id(id_):
    with app.app_context():
        prof=Professor.query.filter_by(id=id).first()
    return prof
def get_profs_by_first_name(first_name_):
    with app.app_context():
        profs=Professor.query.filter_by(first_name=first_name_).all()
    return profs

def get_profs_by_middle_name(middle_name_):
    with app.app_context():
        profs=Professor.query.filter_by(middle_name=middle_name_).all()
    return profs

def get_profs_by_last_name(last_name_):
    with app.app_context():
        profs=Professor.query.filter_by(last_name=last_name_).all()
    return profs

def get_prof_by_contact_number(contact_number_):
    with app.app_context():
        prof=Professor.query.filter_by(contact_number=contact_number_).first()
    return prof

def get_prof_by_national_id(national_id_):
    with app.app_context():
        prof=Professor.query.filter_by(national_id_=national_id_).first()
    return prof    

def get_prof_by_email(email_):
    with app.app_context():
        prof=Professor.query.filter_by(email=email_).first()
    return prof

def get_profs_by_date_of_birth(date_of_birth_):
    with app.app_context():
        prof=Professor.query.filter_by(date_of_birth=date_of_birth_).first()
    return prof

#====================================================================


#=======================Assistant=====================================

def get_asst_by_id(id_):
    with app.app_context():
        asst=Assistant.query.filter_by(id=id_).first()
        return asst
def get_assts_by_first_name(first_name_):
    with app.app_context():
        assts=Assistant.query.filter_by(first_name=first_name_).all()
    return assts

def get_assts_by_middle_name(middle_name_):
    with app.app_context():
        assts=Assistant.query.filter_by(middle_name=middle_name_).all()
    return assts

def get_assts_by_last_name(last_name_):
    with app.app_context():
        assts=Assistant.query.filter_by(last_name=last_name_).all()
    return assts

def get_asst_by_contact_number(contact_number_):
    with app.app_context():
        asst=Assistant.query.filter_by(contact_number=contact_number_).first()
    return asst

def get_asst_by_national_id(national_id_):
    with app.app_context():
        asst=Assistant.query.filter_by(national_id_=national_id_).first()
    return asst    

def get_asst_by_email(email_):
    with app.app_context():
        asst=Assistant.query.filter_by(email=email_).first()
    return asst

def get_assts_by_date_of_birth(date_of_birth_):
    with app.app_context():
        assts=Assistant.query.filter_by(date_of_birth=date_of_birth_).first()
    return assts

#==========================================================================================

#=============================course========================================

def get_course_by_id(id_):
    with app.app_context():
        course=Course.query.filter_by(id=id_).first()
    return course

def get_course_by_name(name_):
    with app.app_context():
        course=Course.query.filter_by(name=name_.upper()).first()
        return course
