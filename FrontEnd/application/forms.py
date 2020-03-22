from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileAllowed
from wtforms import Form, StringField, SubmitField, FloatField, IntegerField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class CategoryForm(FlaskForm):
    categoryName=StringField('CategoryName',
        validators=[
            DataRequired(),
            Length(min=2, max=100)
        ]
    )
    submit=SubmitField('Add category!')

class ProductForm(FlaskForm):
    productName=StringField('ProductName',
        validators=[
            DataRequired(),
            Length(min=2, max=100)
        ]
    )
    productInfo=StringField('ProductInfo',
        validators=[
            DataRequired(),
            Length(min=2, max=1000)
        ]
    )
    productIMG=FileField('ProductIMG',
        validators=[
            FileAllowed(['jpg','png'])
        ]
    )
    productPrice=FloatField('ProductPrice',
        validators=[
            DataRequired()
        ]
    )
    submit=SubmitField('Add product!')

class UpdateProducts(FlaskForm):
    productName=StringField('ProductName',
        validators=[
            DataRequired(),
            Length(min=2, max=100)
        ]
    )
    productPrice=FloatField('ProductPrice',
        validators=[
            DataRequired()
        ]
    )
    submit=SubmitField('Update product!')

class DeleteProduct(FlaskForm):
    productName=StringField('ProductName',
        validators=[
            DataRequired(),
            Length(min=2, max=100)
        ]
    )
    submit=SubmitField('Delete product!')

class Register(FlaskForm):
    email=StringField('Email', 
        validators=[
            DataRequired(),
            Length(min=2, max=100)
        ]
    )
    password=StringField('Password',
        validators=[
            DataRequired(),
            Length(min=6, max=100)
        ]   
    )
    confirmPassword=StringField('Confirm password',
        validators=[
            DataRequired(),
            Length(min=6, max=100)
        ]
    )
    submit=SubmitField("Register")
