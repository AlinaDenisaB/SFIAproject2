from flask import Flask, request
from application import app
import requests
import random

specialChars='!?#@£%&'

@app.route('/specialChar2')
def specialChar2():
    return ''.join(random.choice(specialChars) for i in range(3))
