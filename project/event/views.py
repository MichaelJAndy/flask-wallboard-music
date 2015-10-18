__author__ = 'mandreacchio'


#################
#### imports ####
#################
from flask import render_template, Blueprint, url_for, redirect, flash, request
from project.models import Event
from project.event.forms import AddEventForm
# from project.event.helpers import blah
from project.event.dao import EventDAO

################
#### config ####
################

event_blueprint = Blueprint('event', __name__,)
event_dao = EventDAO()

################
#### routes ####
################


@event_blueprint.route('/event/add', methods=['GET', 'POST'])
def add():
    form = AddEventForm(request.form)

    if form.validate_on_submit():
        event = Event(name=form.name.data)
        event_dao.create_event(event)
        flash('Event added.', 'success')
        return redirect(url_for("main.home"))

    return render_template('event/add.html', form=form)


@event_blueprint.route('/event/view')
def view():

    events = event_dao.get_events()
    return render_template('event/view.html', events=events)

