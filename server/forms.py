from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, Email


class LoginForm(FlaskForm):
    name = StringField('name', validators=[InputRequired("Name required.")])
    email = EmailField('Email address', [InputRequired("Email required."), Email("Invalid email entered.")])
    password = PasswordField("password", validators=[Length(min=8, message=('Your password must be atleast 8 characters long.'))])
    retype_password = PasswordField("retype_password", validators=[Length(min=8, message=('Your password is too short.')), EqualTo('password', "Passwords don't match.")])

    # recaptcha = RecaptchaField()
    submit = SubmitField("Submit") 

