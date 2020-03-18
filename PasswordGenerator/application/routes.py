from flask import Flask, request
from application import app
import requests
import random

@app.route('/passGen', methods=['GET', 'POST'])
def passGen():
    specialChar = requests.get('http://specialchargen:5003/specialChar').text
    numGen = requests.get('http://randnumsgen:5001/numGen').text
    letGen = requests.get('http://randletgen:5002/letGen').text
    var = specialChar+numGen+letGen
    return ''.join(random.sample(var, len(var)))
