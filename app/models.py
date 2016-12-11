from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin
from app import db



class UserData(db.Model, UserMixin):
	__tablename__ = "confidential"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(255))
	password = db.Column(db.String(255))
	# firstname = db.Column(db.String(255))
	# lastname = db.Column(db.String(255))
	# tel = db.Column(db.String(300))
	
	def set_password(self, password):
		self.parola = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.pw_hash, password)

	def is_active(self):
		return True

class Item(db.Model):
	__tablename__ = "item"
	id = db.Column(db.Integer, primary_key=True)
	tema = db.Column(db.String(255))
	# de facut liste de selectare
	disciplina = db.Column(db.String(255))
	poza = db.Column(db.String(255))
	text = db.Column(db.Text) 
	# numar curs/ nume lectie - lista de selectare

class Hashtag(db.Model):
	__tablename__ = "hashtag"
	id = db.Column(db.Integer, primary_key=True)
	nume = db.Column(db.String(255))
	item_id = db.Integer, db.ForeignKey('item.id')
