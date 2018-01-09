from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(Form):
    firstname = StringField('First name', validators=[DataRequired('Please enter your First name')])
    lastname = StringField('Last name', validators=[DataRequired('Please enter your Last name')])
    email = StringField('Email', validators=[DataRequired('Please enter your Email'), Email('Please enter a valid Email')])
    password = PasswordField('Password', validators=[DataRequired('Please enter your Password'),
                                                     Length(min=6, message="Password should be longer than 6 characters")])
    submit = SubmitField('Sign up')


class LoginForm(Form):
    email = StringField('Email',
                        validators=[DataRequired('Please enter your Email'), Email('Please enter a valid Email')])
    password = PasswordField('Password', validators=[DataRequired('Please enter your Password'),
                                                     Length(min=6,
                                                            message="Password should be longer than 6 characters")])
    submit = SubmitField('Sign in')