# project/main/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint
from project.event.dao import EventDAO
from project.event.forms import DeleteEventForm

################
#### config ####
################

main_blueprint = Blueprint('main', __name__,)
event_dao = EventDAO()

################
#### routes ####
################


@main_blueprint.route('/')
def home():
    events = event_dao.get_events()
    form = DeleteEventForm()
    return render_template('main/home.html', events=events, form=form)


@main_blueprint.route("/about/")
def about():
    return render_template("main/about.html")
