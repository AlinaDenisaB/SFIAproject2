from flask_wtf import FlaskForm, RecaptchaField
from wtforms import Form, SubmitField
import wtforms.validators

class Generator(FlaskForm):
    genPassword = SubmitField('Generate password')

    def validate_password(self, genPassword):
        password=Passwords.query.filter_by(password=password.data).first()

        if password:
            raise ValidationError('Password already exists!')
