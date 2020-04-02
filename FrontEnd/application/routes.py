from flask import render_template
from application import app, db, bcrypt
from application.forms import Generator
import requests

@app.route('/', methods=['GET', 'POST'])
@app.route('/frontend', methods=['GET','POST'])
def frontend():
    generator=Generator()
    genPassword = str(requests.get('http://51.104.244.89:5004/passGen').text)

    return render_template("frontend.html", title='Password Generator', form1=generator, genPassword=genPassword)
