#################
#### imports ####
#################
from flask import render_template, Blueprint, url_for, redirect, flash, request
from project.models import Job
from project.job.forms import AddJobForm, DeleteJobForm
# from project.job.helpers import blah
from project.job.dao import JobDAO


################
#### config ####
################

job_blueprint = Blueprint('job', __name__, )
job_dao = JobDAO()


################
#### routes ####
################


@job_blueprint.route('/job/add/<int:event_id>', methods=['GET', 'POST'])
def add(event_id):
    form = AddJobForm(request.form)

    if form.validate_on_submit():
        try:

            job = Job(name=form.name.data,
                      hour=form.hour.data,
                      minute=form.minute.data,
                      second=form.second.data,
                      event_id=event_id)

            if form.weekday.data is True:
                job.day_of_week = 'mon,tue,wed,thu,fri'

            job_dao.create_job(job)
            flash('Job added.', 'success')
            return redirect(url_for("job.view", event_id=event_id))

        except Exception as e:
            flash('Job add fail {}'.format(e), 'danger')
            print(e)
            return render_template('job/add.html', form=form)

    return render_template('job/add.html', form=form)


@job_blueprint.route('/job/view/<int:event_id>')
def view(event_id):
    form = DeleteJobForm()
    jobs = job_dao.get_jobs_by_kwargs(event_id=event_id)
    return render_template('job/view.html', jobs=jobs, event_id=event_id, form=form)


@job_blueprint.route('/job/delete', methods=['POST'])
def delete():

    form = DeleteJobForm()
    job_object = job_dao.get_job_by_id(form.id.data)

    if job_object:
        job_dao.delete_job(job_object)
        flash('The Job was deleted.', 'success')
    else:
        flash('Job id not found, it may have already been deleted', 'danger')

    return redirect(url_for('job.view', event_id=job_object.event_id))
