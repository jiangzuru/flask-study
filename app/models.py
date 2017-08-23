from . import db

class User(db.Model):
	name = db.Column(db.String(32), primary_key=True)