from flask import Flask, request
from application import app
import requests
import random

@app.route('/', methods=['GET', 'POST'])
def passGen():
    response = requests.get('http://specialchargen:5000')
    specialChar = response.text
    response = requests.get('http://randnumsgen:5000')
    numGen = response.text
    response = requests.get('http://randletgen:5000')
    letGen = response.text
    var = specialChar+numGen+letGen
    return ''.join(random.sample(var, len(var)))

