from flask import Flask, request
from application import app
import requests
import random

@app.route('/passwordGenerator')
def passGen():
    specialChar = requests.get('http://localhost:5003/specialChar').text
    numGen = requests.get('http://localhost:5001/numGen').text
    letGen = requests.get('http://localhost:5002/letGen').text
    var = specialChar+numGen+letGen
    return ''.join(random.sample(var, len(var)))
