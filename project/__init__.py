# project/__init__.py


#################
#### imports ####
#################

import os

from flask import Flask, render_template
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt
from flask.ext.debugtoolbar import DebugToolbarExtension
from flask.ext.restless import APIManager
from flask_bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy



################
#### config ####
################

app = Flask(__name__)

from datetime import datetime
print("App Loaded", datetime.now())


try:
    app.config.from_object(os.environ['APP_SETTINGS'])
except Exception as e:
    print("Variable APP_SETTINGS not set, defaulting to DevelopmentConfig")
    APP_SETTINGS = "project.config.DevelopmentConfig"
    app.config.from_object(APP_SETTINGS)


####################
#### extensions ####
####################

login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)
toolbar = DebugToolbarExtension(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

####################
#### Scheduler  ####
####################


from apscheduler.schedulers.background import BackgroundScheduler
scheduler = BackgroundScheduler()
scheduler.add_jobstore('sqlalchemy', url=app.config['SQLALCHEMY_DATABASE_URI'])


###################
### blueprints ####
###################

# from project.user.views import user_blueprint
# app.register_blueprint(user_blueprint)

from project.main.views import main_blueprint
from project.song.views import song_blueprint
from project.event.views import event_blueprint
from project.job.views import job_blueprint
app.register_blueprint(main_blueprint)
app.register_blueprint(song_blueprint)
app.register_blueprint(event_blueprint)
app.register_blueprint(job_blueprint)


###################
#### API ##########
###################

api_manager = APIManager(app, flask_sqlalchemy_db=db)
from project.api import api_blueprint
app.register_blueprint(api_blueprint)


###################
### flask-login ####
###################

# from project.models import User
#
# login_manager.login_view = "btn-primary"
# login_manager.login_message_category = 'danger'
#
#
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.filter(User.id == int(user_id)).first()


########################
#### error handlers ####
########################

@app.errorhandler(403)
def forbidden_page(error):
    return render_template("errors/403.html"), 403


@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"), 404


@app.errorhandler(500)
def server_error_page(error):
    return render_template("errors/500.html"), 500


scheduler.start()
