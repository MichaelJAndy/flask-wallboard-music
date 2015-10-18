from flask_wtf import Form
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Optional, InputRequired, NumberRange, Regexp
__author__ = 'mandreacchio'

# Removed this as there's no way to avoid doing this twice
# def check_youtube(form, field):
#     ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s', 'noplaylist': True, 'no_color': True})
#     try:
#         ydl.extract_info(field.data, process=False, download=False)
#     except Exception:
#         raise ValidationError("Invalid Youtube Video")


class AddJobForm(Form):

    job_id = IntegerField()
    name = StringField('Job Name', validators=[DataRequired()])
    # year=None, month=None, day=None, week=None, day_of_week=None, hour=None, minute=None,
    #      second=None, start_date=None, end_date=None, timezone=None
    hour = IntegerField('Hour', validators=[Optional()])
    minute = IntegerField('Minute', validators=[Optional()])
    second = IntegerField('Second', validators=[Optional()])
    weekday = BooleanField('Weekdays only')


