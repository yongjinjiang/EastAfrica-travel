from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    first_name = StringField('first name', validators=[DataRequired()])
    last_name= StringField('last name', validators=[DataRequired()])
    email= StringField('email', validators=[DataRequired()])
    cellphone= StringField('cell phone', validators=[DataRequired()])
    comment= StringField('leave your message:', validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm_lugha(FlaskForm):
    first_name = StringField('jina la kwanza', validators=[DataRequired()])
    last_name= StringField('jina la familia', validators=[DataRequired()])
    email= StringField('barua pepe', validators=[DataRequired()])
    cellphone= StringField('simu ya mkononi', validators=[DataRequired()])
    comment= StringField('shika ujumbe wako:')
    submit = SubmitField('kujiandikisha')