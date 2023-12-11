from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    BooleanField,
    IntegerField,
    SelectField,
    DateField,
)
from wtforms.validators import DataRequired, length, Email, EqualTo


class RegistrationForm(FlaskForm):
    fname = StringField(
        "First Name", validators=[DataRequired(), length(min=2, max=25)]
    )
    mname = StringField(
        "Middle Name", validators=[DataRequired(), length(min=2, max=25)]
    )
    lname = StringField("Last Name", validators=[DataRequired(), length(min=2, max=25)])
    username = StringField(
        "Username", validators=[DataRequired(), length(min=2, max=25)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    contact_number = StringField(
        "Contact Number",
        validators=[DataRequired(), length(max=11, min=11)],
    )
    national_id = StringField(
        "National ID", validators=[length(max=14, min=14), DataRequired()]
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
        ],
    )
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    gender = SelectField(
        "Gender",
        choices=[("male", "Male"), ("female", "Female")],
        validators=[DataRequired()],
    )
    level = SelectField(
        "Your Level", choices=[("level 1", "Level 1")], validators=[DataRequired()]
    )
    date_of_birth = DateField(
        "Date of Birth", validators=[DataRequired()], format=["%d-%m-%Y"]
    )
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
        ],
    )
    remember = BooleanField("Remember Me")
    submit = SubmitField("Log in")
