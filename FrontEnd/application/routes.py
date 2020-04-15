from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.forms import Generator
from application.models import Passwords
import requests

@app.route('/', methods=['GET', 'POST'])
def frontend():
    generator=Generator()
    genPassword = str(requests.get('http://passwordgenerator:5000').text)
    return render_template("frontend.html", title='Password Generator', form1=generator, genPassword=genPassword)

