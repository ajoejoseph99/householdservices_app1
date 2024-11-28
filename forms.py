from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Register')

class ServiceForm(FlaskForm):
    name = StringField('Service Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    base_price = FloatField('Base Price', validators=[DataRequired()])
    submit = SubmitField('Add Service')

class ServiceRequestForm(FlaskForm):
    remarks = TextAreaField('Remarks')
    submit = SubmitField('Submit Request')
