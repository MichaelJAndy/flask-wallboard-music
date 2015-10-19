__author__ = 'mandreacchio'


#################
#### imports ####
#################
from flask import render_template, Blueprint, url_for, redirect, flash, request
from project.models import Event
from project.event.forms import EventForm
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
    form = EventForm(request.form)

    if form.validate_on_submit():
        event = Event(name=form.name.data,
                      play_length=form.play_length.data)
        event_dao.create_event(event)
        flash('Event added.', 'success')
        return redirect(url_for("main.home"))

    return render_template('event/add.html', form=form)


# @event_blueprint.route('/event/view')
# def view():
#
#     events = event_dao.get_events()
#     return render_template('event/view.html', events=events)


@event_blueprint.route('/event/edit/<int:event_id>', methods=['GET', 'POST'])
def edit(event_id):
    event = event_dao.get_event_by_id(event_id)
    form = EventForm(request.form, event)

    if form.validate_on_submit() and request.method == 'POST':
        form.populate_obj(event)
        event_dao.update_event(event)
        flash("Event Edited", 'success')
        return redirect(url_for("main.home"))

    return render_template('event/edit.html', form=form, event_id=event_id)


# def edit_profile(request):
#     user = request.current_user
#     form = ProfileForm(request.POST, user)
#     if request.method == 'POST' and form.validate():
#         form.populate_obj(user)
#         user.save()
#         redirect('edit_profile')
#     return render_response('edit_profile.html', form=form)