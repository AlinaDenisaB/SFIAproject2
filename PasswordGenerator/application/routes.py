from flask import Flask, request
from application import app
import requests
import random

@app.route('/passGen', methods=['GET', 'POST'])
def passGen():
    specialChar = requests.get('http://51.104.244.89:5003/specialChar').text
    numGen = requests.get('http://51.104.244.89:5001/numGen').text
    letGen = requests.get('http://51.104.244.89:5002/letGen').text
    var = specialChar+numGen+letGen
    return ''.join(random.sample(var, len(var)))
