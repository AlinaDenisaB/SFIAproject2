from flask import Flask, request
from application import app
import requests
import random

@app.route('/passGen2', methods=['GET', 'POST'])
def passGen2():
    specialChar = requests.get('http://51.104.244.89:5007/specialChar').text
    numGen = requests.get('http://51.104.244.89:5005/numGen').text
    letGen = requests.get('http://51.104.244.89:5006/letGen').text
    var = specialChar+numGen+letGen
    return ''.join(random.sample(var, len(var)))
