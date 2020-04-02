from flask_wtf import FlaskForm, RecaptchaField
from wtforms import Form, SubmitField

class Generator(FlaskForm):
    genPassword = SubmitField('Generate password')
