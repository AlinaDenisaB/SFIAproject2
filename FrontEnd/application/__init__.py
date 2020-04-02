from flask import Flask, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
from os import getenv


app= Flask(__name__)
bcrypt = Bcrypt(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://alina:password@http://db:3306/db"
#SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from application import routes
