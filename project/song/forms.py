from flask_wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, InputRequired, NumberRange, Regexp, ValidationError

__author__ = 'mandreacchio'

# Removed this as there's no way to avoid doing this twice
# def check_youtube(form, field):
#     ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s', 'noplaylist': True, 'no_color': True})
#     try:
#         ydl.extract_info(field.data, process=False, download=False)
#     except Exception:
#         raise ValidationError("Invalid Youtube Video")


class AddSongForm(Form):

    song_id = IntegerField()
    url = StringField('Youtube URL',
                      validators=[
                          DataRequired(),
                          Regexp(regex='https://www.youtube.com/.*', message=u'Invalid YouTube URL.'),
                          # check_youtube
                      ])
    requester = StringField('Requester Name', validators=[DataRequired()])
    delay = IntegerField('Song delay in seconds',
                         validators=[
                             InputRequired(message=u'Must enter delay'),
                             NumberRange(min=0, max=None, message=u'Must be minimum 0')],
                         default=0)
    # #     mode_id = db.Column(db.Integer, db.ForeignKey('mode.id'))




