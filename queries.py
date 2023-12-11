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
