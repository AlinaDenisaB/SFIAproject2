from application import db

class Passwords(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password=db.Column(db.String(30), nullable=False)
