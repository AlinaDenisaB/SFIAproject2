from flask import Flask, request
from application import app
import requests
import random

numbers = '0123456789'

@app.route('/')
def numGen():
    return ''.join(random.choice(numbers) for i in range(5))
