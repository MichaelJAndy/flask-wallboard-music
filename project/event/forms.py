from flask_wtf import Form
from wtforms import StringField, IntegerField, HiddenField
from wtforms.validators import DataRequired, InputRequired, NumberRange, Regexp

__author__ = 'mandreacchio'


class EventForm(Form):

    id = HiddenField()
    name = StringField('Event Name', validators=[DataRequired()])
    play_length = IntegerField('Song Length ms', validators=[InputRequired()])
