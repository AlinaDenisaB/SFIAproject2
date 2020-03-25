from flask import Flask, request
from application import app
import requests
import random

@app.route('/passGen', methods=['GET', 'POST'])
def passGen():
    specialChar = requests.get('http://specialchar-service:5003/specialChar').text
    numGen = requests.get('http://letters-service:5001/numGen').text
    letGen = requests.get('http://numbers-service:5002/letGen').text
    var = specialChar+numGen+letGen
    return ''.join(random.sample(var, len(var)))
