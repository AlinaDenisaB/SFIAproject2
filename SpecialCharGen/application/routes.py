from flask import Flask, request
from application import app
import requests
import random

specialChars='!?#@£%&'

@app.route('/')
def specialChar():
    return ''.join(random.choice(specialChars) for i in range(2))
