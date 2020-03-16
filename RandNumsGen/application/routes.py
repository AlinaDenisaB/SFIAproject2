from flask import Flask, request
from application import app
import requests
import random

numbers = '0123456789'

@app.route('numGen', methods=['POST'])
def numGen():
	response_value = ''.join(random.choice(numbers) for i in range(6))
	return {"Random number":response_value}
