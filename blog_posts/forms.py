from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, ValidationError
from flask_wtf.file import FileField, FileRequired, FileAllowed
from admin_backend.models import User


class SignInForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

    def validate_data(self):
        user = User.query.filter(self.email.data == User.email)\
                     .filter(self.password.data == User.password)\
                     .first()
        if user is not None:
            return user
        else:
            raise ValidationError('This combination of user and password is not valid')


class NewPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=5, max=60, message='Title length must be '
                                                                                           'between 5 and 60 '
                                                                                           'characters')])
    leadimg = FileField('Lead Image', validators=[
        FileAllowed(['jpg', 'png'], 'Images only!'),
        FileRequired()
    ])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Create!')
