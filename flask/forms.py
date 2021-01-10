from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class EnterDataForm(FlaskForm):

    tags = StringField('Keywords', validators=[Length(min=0, max=100)])
    
    picture = FileField('Enter Item Image', validators=[FileAllowed(['jpg', 'png'])])
    
    submit = SubmitField('Update')
