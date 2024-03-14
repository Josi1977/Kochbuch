from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')
    
class RezeptForm(FlaskForm):
    rezeptname = StringField('Recipe name',validators=[DataRequired()])
    zutaten = TextAreaField('Ingridients' ,validators=[DataRequired()])
    kochanleitung = TextAreaField('Cooking instructions' ,validators=[DataRequired()])
    submit = SubmitField('add')

