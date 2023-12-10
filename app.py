# app.py
from flask import Flask, render_template, request, redirect
import sqlite3
from oop import (
    Student,
    Professor,
    Professor_asst,
)  # Assuming you have a class Professor in oop module

app = Flask(__name__)
DATABASE = "database.db"

import sqlite3

DATABASE = "All_Tables.db"

def create_tables():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            middle_name TEXT,
            last_name TEXT NOT NULL,
            contact_number TEXT NOT NULL,
            national_id TEXT NOT NULL,
            email TEXT NOT NULL,
            date_of_birth TEXT NOT NULL,
            gender TEXT NOT NULL,
            class_level TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """
    )
    connection.commit()
    connection.close()


def create_table2():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS profs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            middle_name TEXT,
            last_name TEXT NOT NULL,
            contact_number TEXT NOT NULL,
            national_id TEXT NOT NULL,
            email TEXT NOT NULL,
            date_of_birth TEXT NOT NULL,
            gender TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """
    )
    connection.commit()
    connection.close()


def create_table3():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS assistant (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            middle_name TEXT,
            last_name TEXT NOT NULL,
            contact_number TEXT NOT NULL,
            national_id TEXT NOT NULL,
            email TEXT NOT NULL,
            date_of_birth TEXT NOT NULL,
            gender TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """
    )
    connection.commit()
    connection.close()


def create_table_courses():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    # Example table creation
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY,
>>>>>>> ad2277672680321862d6ca200e19d9c55c091d8d
            course_name TEXT,
            instructor_id INTEGER,
            start_date DATE,
            end_date DATE,
            FOREIGN KEY (instructor_id) REFERENCES profs(id)
        )
    ''')

    # Enrollments table (to link students with courses)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS enrollments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES students(id),
            FOREIGN KEY (course_id) REFERENCES courses(id)
        )
    ''')

    # AssistantAssignments table (to link assistants with courses)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS assistant_assignments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            assistant_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY (assistant_id) REFERENCES assistant(id),
            FOREIGN KEY (course_id) REFERENCES courses(id)
        )
    """
    )

    connection.commit()
    connection.close()



create_table2()
create_table3()
create_table_courses()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/log_in")
# ... (previous code)

# ... (previous code)


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # Check if the user exists in the students table
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM students WHERE email=? AND password=?", (email, password)
        )
        student = cursor.fetchone()
        connection.close()

        # If not found in students table, check professors table
        if not student:
            connection = sqlite3.connect(DATABASE)
            cursor = connection.cursor()
            cursor.execute(
                "SELECT * FROM profs WHERE email=? AND password=?", (email, password)
            )
            professor = cursor.fetchone()
            connection.close()

            # If not found in professors table, check assistant table
            if not professor:
                connection = sqlite3.connect(DATABASE)
                cursor = connection.cursor()
                cursor.execute(
                    "SELECT * FROM assistant WHERE email=? AND password=?",
                    (email, password),
                )
                assistant = cursor.fetchone()
                connection.close()

                # If not found in any table, invalid login
                if not assistant:
                    return "Invalid email or password"

                # Return welcome message for assistant
                return render_template("dashboard.html")
            else:
                # Return welcome message for professor
                return "Welcome professor "
        else:
            # Return welcome message for student
            return "Welcome student "

    return render_template("log_in.html")


# ... (remaining code)


@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")


@app.route("/sign_up_for_students", methods=["GET", "POST"])
def sign_up_for_students():
    s = Student()

    if request.method == 'POST':

        s.data =Student(request.form) 

        s.data =request.form 
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute()
            '''
            INSERT INTO students (
                first_name, middle_name, last_name,
                contact_number, national_id, email,
                date_of_birth, gender, class_level, password
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

        ''', (
            s.data['first-name'],
            s.data['middle-name'],
            s.data['last-name'],
            s.data['contact-number'],
            s.data['national-id'],
            s.data['email'],
            s.data['date-of-birth'],
            s.data['gender'],
            s.data['class_level'],
            s.data['password']
        ))
>>>>>>> 545422943b3f7047cb92ba27f79cf6e12fa5018f
        connection.commit()
        connection.close()
    return render_template("sign_up_for_students.html")


@app.route("/sign_up_for_ass_prof", methods=["GET", "POST"])
def sign_up_for_ass_prof():
    a = Professor_asst()
    if request.method == "POST":
        a.data = request.form
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO assistant (
                first_name, middle_name, last_name,
                contact_number, national_id, email,
                date_of_birth, gender, password
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                a.data["first-name"],
                a.data["middle-name"],
                a.data["last-name"],
                a.data["contact-number"],
                a.data["national-id"],
                a.data["email"],
                a.data["date-of-birth"],
                a.data["gender"],
                a.data["password"],
            ),
        )
        connection.commit()
        connection.close()
    return render_template("sign_up_for_ass_prof.html")


@app.route("/sign_up_for_prof", methods=["GET", "POST"])
def sign_up_for_prof():
    p = Professor()
    if request.method == "POST":
        p.data = request.form
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO profs (
                first_name, middle_name, last_name,
                contact_number, national_id, email,
                date_of_birth, gender, password
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                p.data["first-name"],
                p.data["middle-name"],
                p.data["last-name"],
                p.data["contact-number"],
                p.data["national-id"],
                p.data["email"],
                p.data["date-of-birth"],
                p.data["gender"],
                p.data["password"],
            ),
        )
        connection.commit()
        connection.close()
    return render_template("sign_up_for_prof.html")


@app.route("/dashboard")
def dashboard():
    # Fetch data from the students table
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM students')
    students_data = cursor.fetchall()
    connection.close()

    # Fetch data from the profs table
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM profs')
    professors_data = cursor.fetchall()
    connection.close()

    # Fetch data from the assistant table
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM assistant')
    assistants_data = cursor.fetchall()
    connection.close()

    # Create dictionaries for each type of user
    students = [{'id': student[0], 'first_name': student[1], 'last_name': student[3], 'email': student[5]} for student in students_data]
    professors = [{'id': professor[0], 'first_name': professor[1], 'last_name': professor[3], 'email': professor[5]} for professor in professors_data]
    assistants = [{'id': assistant[0], 'first_name': assistant[1], 'last_name': assistant[3], 'email': assistant[5]} for assistant in assistants_data]

    return render_template("dashboard.html", students=students, professors=professors, assistants=assistants)

    


@app.route("/student_dashboard")
def student_dashboard():
    return render_template("student_dashboard.html")


@app.route("/student_dashboard/assignment_for_student")
def assignment_for_student():
    return render_template("assignment_for_student.html")


@app.route("/student_dashboard/courses_for_student")
def courses_for_student():
    return render_template("courses_for_student.html")


@app.route("/student_dashboard/timetable_for_student")
def timetable_for_student():
    return render_template("timetable_for_student.html")


if __name__ == "__main__":
    app.run(debug=True)
