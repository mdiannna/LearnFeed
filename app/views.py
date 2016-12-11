# -*- coding: utf-8 -*-
from app import app, db
from app import login_manager
from flask import render_template, request, redirect, url_for
from forms import FeedForm, LoginForm
from app.models import Item, Hashtag, UserData
from flask.ext.login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

import os
from werkzeug.utils import secure_filename

# encoding=utf8  
import sys  
import random

reload(sys)  
sys.setdefaultencoding('utf8')



@login_manager.user_loader
def load_user(userid):
	user = UserData.query.get(userid)
	return user


@app.route('/login', methods = ['POST', 'GET'])
def login():
	error = None
	form = LoginForm(request.form, csrf_enabled=True)
	# if form.validate_on_submit():
	if request.method == "POST":
		username = form.username.data
		password = form.password.data
	
		users = UserData.query.all()
		for user in users:
			if username == user.username:
				if check_password_hash(user.password, password):
					login_user(user)
					print 'logged in successfully'
					return redirect('/')
					break
		error = "login unsuccesful"
		print error

	return render_template("login.html", form = form, error=error)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/')
@login_required
def index():
	items = Item.query.all()
	random.shuffle(items)
	return render_template("index.html", items=items)

@app.route('/add_item', methods=['GET', 'POST'])
@login_required
def add_item():	
	form = FeedForm(request.form, csrf_enabled=True)


	if request.method == 'POST':
		f1 = request.files['file1']
		if not f1:
	   		error = '|Error! Please choose the FIRST file to upload'
	   		print error
	   		return render_template("add_item.html", form=form)

	   	elif not allowed_file(f1.filename):
	   		ALLOWED_EXTENSIONS = str(app.config['ALLOWED_EXTENSIONS']).replace("'", '').replace('set([', '').replace('])', '')
	   		error = error + "|Error! Wrong Extension of FIRST file. Allowed only: """ + ALLOWED_EXTENSIONS 	
	   		print error
	   		return render_template("add_item.html", form=form)

	   	   		
	   	elif f1 and allowed_file(f1.filename):
	   		f1.save(os.path.join(app.config['UPLOAD_FOLDER'], f1.filename))
			poza = "static/files/uploaded/" + f1.filename 
		
		tema = str(form.tema.data)
		disciplina = str(form.disciplina.data)
		if not f1:
			poza = str(form.poza.data)
		text = str(form.text.data)

		item = Item(tema=tema, disciplina=disciplina, poza=poza, text=text)
		db.session.add(item)
		db.session.commit()

		return redirect('/')

	return render_template("add_item.html", form=form)


def allowed_file(filename):
	ALLOWED_EXTENSIONS = app.config['ALLOWED_EXTENSIONS']
	return '.' in filename and \
		   filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
   if request.method == 'POST':
   	f = request.files['file']
   	if not allowed_file:
   		alert('Error! Please choose file to upload')
   	elif not f:
   		alert('Error! Please choose file')
   	if f and allowed_file(f.filename):
   		f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
   		# f.save(secure_filename(f.filename)):
   		return 'file uploaded successfully'
   	


