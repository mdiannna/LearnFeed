# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField,  SubmitField, PasswordField, IntegerField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from models import Item, Hashtag
# from wtforms import Form
from wtforms_components import DateTimeField, SelectField
from werkzeug.datastructures import MultiDict


class FeedForm(Form):
	tema = TextField('Tema:')
	disciplina = TextField('Disciplina:')
	poza = TextField('Link poza:')
	text = TextAreaField('Text:')
	# de modificat
	hashtag = TextField('Hashtag: (la moment 1:)')
	submit = SubmitField('OK')

class LoginForm(Form):
	username = TextField('Username:')
	password = PasswordField('Password:')
	submit = SubmitField('OK')


# class RegisterForm(Form):
# 	key = TextField('Key:')
# 	username = TextField('Username:')
# 	password = PasswordField('Password:')
# 	firstname = TextField('First name:')
# 	lastname = TextField('Last name:')
# 	tel = TextField('Tel. nr:')
# 	submit = SubmitField('OK')
