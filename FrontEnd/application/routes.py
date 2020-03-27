from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.forms import CategoryForm, ProductForm, UpdateProducts, DeleteProduct, Generator, Generator2, Register
import flask_bcrypt
import os
import secrets
from werkzeug.utils import secure_filename
#from PIL import Image
import requests

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/products')
def products():
    products = db.Products.query.all()
    categories= db.Categories.query.all()
    loc_image= url_for('static', filename='productIMG/')
    return render_template("products.html", categories=categories, products=products, loc_image=loc_image)

@app.route('/cart')
def cart():

    return render_template("cart.html", title='Cart')

def save_img(form_picture):
    random_hex = secrets.token_hex(8)
    _name, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/productIMG', picture_fn)
    output_size=(300,250)
    i=Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    categoryForm=CategoryForm()
    if categoryForm.validate_on_submit():
        category=db.Categories(
                categoryName=categoryForm.categoryName.data
            )
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('products'))
    
    productForm=ProductForm()
    if productForm.validate_on_submit():
        if productForm.productIMG.data:
            FinalIMG=save_img(productForm.productIMG.data)
            db.Products.productIMG = FinalIMG

        product=db.Products(
                productName=productForm.productName.data, 
                productInfo=productForm.productInfo.data,
                productIMG=FinalIMG,
                productPrice=productForm.productPrice.data
        )
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('products'))
    
    updateProduct=UpdateProducts()
    if updateProduct.validate_on_submit():
        newPrice=db.Products.query.filter_by(productName=updateProduct.productName.data).update(dict(productPrice=updateProduct.productPrice.data))
        db.session.commit()
        return redirect(url_for('products'))

    deleteProduct=DeleteProduct()
    if deleteProduct.validate_on_submit():
        db.Products.query.filter_by(productName=deleteProduct.productName.data).delete()
        db.session.commit()
        return redirect(url_for('products'))

    return render_template('admin.html', form=categoryForm, form1=productForm, form2=updateProduct, form3=deleteProduct)

@app.route('/register', methods=['GET','POST'])
def register():
    generator=Generator()
    genPassword = str(requests.get('http://51.104.244.89:5004/passGen').text)
    
    generator2=Generator2()
    genPassword2 = str(requests.get('http://51.104.244.89:5008/passGen2').text)

    register=Register()
    if register.validate_on_submit():
        NewUser=db.Users(
                email=register.email.data,
                password = register.password.data,
                confirmPassword=register.confirmPassword.data
        )
        db.session.add(NewUser)
        db.session.commit()
        return redirect(url_for('cart'))

    return render_template("register.html", title='Register', form=register, form1=generator, form2=generator2, genPassword=genPassword, genPassword2=genPassword2)
