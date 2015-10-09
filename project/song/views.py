# project/song/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint, url_for, redirect, flash, request
from project import db
from project.models import Song
from project.song.forms import AddSongForm

################
#### config ####
################

song_blueprint = Blueprint('song', __name__,)

################
#### Helpers####
################


def get_songs():
    return db.session.query(Song).order_by(Song.requester.asc())


################
#### routes ####
################

@song_blueprint.route('/songs/add', methods=['GET', 'POST'])
def add():
    form = AddSongForm(request.form)
    if form.validate_on_submit():
        song = Song(
            url=form.url.data,
            requester=form.requester.data,
            delay=form.delay.data
        )
        db.session.add(song)
        db.session.commit()

        flash('Thank you for adding a song.', 'success')
        return redirect(url_for("song.add"))

    return render_template('songs/add.html', form=form)


@song_blueprint.route('/songs/view')
def view():

    return render_template('songs/view.html', songs=get_songs())






#
# @user_blueprint.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm(request.form)
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user and bcrypt.check_password_hash(
#                 user.password, request.form['password']):
#             login_user(user)
#             flash('You are logged in. Welcome!', 'success')
#             return redirect(url_for('user.members'))
#         else:
#             flash('Invalid email and/or password.', 'danger')
#             return render_template('user/login.html', form=form)
#     return render_template('user/login.html', title='Please Login', form=form)
#
#
# @user_blueprint.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash('You were logged out. Bye!', 'success')
#     return redirect(url_for('main.home'))
#
#
# @user_blueprint.route('/members')
# @login_required
# def members():
#     return render_template('user/members.html')
