from flask_wtf import Form
from wtforms import StringField, IntegerField, BooleanField, HiddenField
from wtforms.validators import DataRequired, Optional, InputRequired, NumberRange, Regexp

__author__ = 'mandreacchio'


class JobForm(Form):

    job_id = IntegerField()
    name = StringField('Job Name', validators=[DataRequired()])
    hour = IntegerField('Hour', validators=[Optional()])
    minute = IntegerField('Minute', validators=[Optional()])
    second = IntegerField('Second', validators=[Optional()])
    weekdays_only = BooleanField('Weekdays only')



class DeleteJobForm(Form):
    id = HiddenField()
