from flask import Flask, request
from application import app
import requests
import random

letters='abcdefghijklmnopqrstuvwxyz'

@app.route('/letGen')
def letGen():
    return ''.join(random.choice(letters) for i in range(16))
