from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed


class SignInForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class NewPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=5, max=30, message='Title length must be '
                                                                                           'between 5 and 30 '
                                                                                           'characters')])
    leadimg = FileField('Lead Image', validators=[
        FileAllowed(['jpg', 'png'], 'Images only!'),
        FileRequired()
    ])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Create!')
