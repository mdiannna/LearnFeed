from flask import Flask 
from flask.ext.bootstrap import Bootstrap 
from flask.ext.script import Manager 
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from settings import db_path


app = Flask(__name__)
app.secret_key = "secret"


UPLOAD_FOLDER = 'app/static/files/uploaded/'
# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'PNG', 'gif', 'png', 'PNG'])


# os.getenv('DATABASE_URL', 'sqlite:///app.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.config['DEBUG'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

login_manager = LoginManager()
login_manager.init_app(app)

Bootstrap(app)
from app import views