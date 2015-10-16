from flask_wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, InputRequired, NumberRange, Regexp

__author__ = 'mandreacchio'


class AddEventForm(Form):

    event_id = IntegerField()
    name = StringField('Event Name', validators=[DataRequired()])
