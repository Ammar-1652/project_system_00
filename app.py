from flask import Flask, render_template, request, redirect, url_for, session
from models import db, Student, Professor, Assistant, Course, Admin, student_course
from forms import LoginForm, RegistrationForm

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Tables.db"
app.config["SECRET_KEY"] = "your_secret_key"
db.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    form = LoginForm()
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # Check if the user exists in the students, professors, assistants, and admin tables
        student = Student.query.filter_by(email=email, password=password).first()
        professor = Professor.query.filter_by(email=email, password=password).first()
        assistant = Assistant.query.filter_by(email=email, password=password).first()
        admin = Admin.query.filter_by(username=email, password=password).first()

        if student:
            session["user_id"] = student.id
            return redirect(url_for("courses_for_student"))
        elif professor:
            # Redirect to professor dashboard
            return redirect("/professor_dashboard")

        elif assistant:
            # Redirect to assistant dashboard
            return redirect("/assistant_dashboard")

        elif admin and admin.isVerified:
            # Redirect to admin dashboard
            return redirect("/admin_dashboard")

        else:
            return "Invalid email or password"

    return render_template("log_in.html", form=form)


@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")


@app.route("/sign_up_for_students", methods=["GET", "POST"])
def sign_up_for_students():
    form = RegistrationForm()
    if request.method == "POST":
        s = Student(
            first_name=request.form["first-name"],
            middle_name=request.form["middle-name"],
            last_name=request.form["last-name"],
            contact_number=request.form["contact-number"],
            national_id=request.form["national-id"],
            email=request.form["email"],
            date_of_birth=request.form["date-of-birth"],
            gender=request.form["gender"],
            class_level=request.form["class_level"],
            password=request.form["password"],
        )
        db.session.add(s)
        db.session.commit()

    return render_template("sign_up_for_students.html", form=form)


@app.route("/sign_up_for_ass_prof", methods=["GET", "POST"])
def sign_up_for_ass_prof():
    if request.method == "POST":
        a = Assistant(
            first_name=request.form["first-name"],
            middle_name=request.form["middle-name"],
            last_name=request.form["last-name"],
            contact_number=request.form["contact-number"],
            national_id=request.form["national-id"],
            email=request.form["email"],
            date_of_birth=request.form["date-of-birth"],
            gender=request.form["gender"],
            password=request.form["password"],
        )
        db.session.add(a)
        db.session.commit()

    return render_template("sign_up_for_ass_prof.html")


@app.route("/sign_up_for_prof", methods=["GET", "POST"])
def sign_up_for_prof():
    form = RegistrationForm()
    if request.method == "POST":
        p = Professor(
            first_name=request.form["first-name"],
            middle_name=request.form["middle-name"],
            last_name=request.form["last-name"],
            contact_number=request.form["contact-number"],
            national_id=request.form["national-id"],
            email=request.form["email"],
            date_of_birth=request.form["date-of-birth"],
            gender=request.form["gender"],
            password=request.form["password"],
        )
        db.session.add(p)
        db.session.commit()

    return render_template("sign_up_for_prof.html", form=form)


@app.route("/dashboard", methods=["GET", "POST"])
def admin_dashboard():
    if request.method == "POST":
        # Handle enrollment creation when the form is submitted
        user_id = request.form["user_id"]
        user_type = request.form["user_type"]
        course_id = request.form["course_id"]

        if user_type == "student":
            user = Student.query.get(user_id)
        elif user_type == "professor":
            user = Professor.query.get(user_id)
        elif user_type == "assistant":
            user = Assistant.query.get(user_id)
        else:
            return "Invalid user type"

        if user is not None:
            course = Course.query.get(course_id)
            # Add the course to the user's courses relationship
            user.courses.append(course)
            db.session.commit()
        else:
            return "User not found"

    # Retrieve data for displaying on the admin dashboard
    students = Student.query.all()
    professors = Professor.query.all()
    assistants = Assistant.query.all()
    courses = Course.query.all()

    return render_template(
        "dashboard.html",
        students=students,
        professors=professors,
        assistants=assistants,
        courses=courses,
    )


@app.route("/student_dashboard")
def student_dashboard():
    # Add logic to display student-specific data
    return render_template("student_dashboard.html")


@app.route("/courses_for_student")
def courses_for_student():
    student_id = session.get("user_id")

    if student_id is not None:
        # Replace the following lines with your actual data retrieval logic
        student = Student.query.get(student_id)  # Replace with proper database query
        student_courses = (
            student.courses
        )  # Assuming the relationship is defined correctly
        return render_template(
            "courses_for_student.html", student=student, courses=student_courses
        )

    # Redirect to login if user is not logged in
    return redirect(url_for("log_in"))


@app.route("/timetable_for_student")
def timetable_for_student():
    # Your view logic here
    return render_template("timetable_for_student.html")


@app.route("/assignment_for_student")
def assignment_for_student():
    # Your view logic here
    return render_template("assignment_for_student.html")


@app.route("/professor_dashboard")
def professor_dashboard():
    # Add logic to display professor-specific data
    return render_template("professor_dashboard.html")


@app.route("/assistant_dashboard")
def assistant_dashboard():
    # Add logic to display assistant-specific data
    return render_template("ass_professor_dashboard.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
