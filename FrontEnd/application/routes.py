from flask import render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.forms import Generator
from application.models import Passwords
import requests

@app.route('/', methods=['GET', 'POST'])
@app.route('/frontend1', methods=['GET','POST'])
def frontend1():
    generator=Generator()
    genPassword = str(requests.get('http://51.104.244.89:5004/passGen1').text)
    return render_template("frontend1.html", title='Password Generator', form1=generator, genPassword=genPassword)

@app.route('/frontend2', methods=['GET','POST'])
def frontend2():
    generator=Generator()
    genPassword = str(requests.get('http://51.104.244.89:5004/passGen2').text)
    return render_template("frontend2.html", title='Password Generator', form1=generator, genPassword=genPassword)
