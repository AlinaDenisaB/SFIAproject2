from flask import Flask, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os
from os import getenv


app= Flask(__name__)
bcrypt = Bcrypt(app)


#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://"+os.getenv("USERNAME")+":"+os.getenv("PASSWORD")+"@"+os.getenv("MYSQL_URL")+"/"+os.getenv("MYSQL_DB")
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)

from application import routes
