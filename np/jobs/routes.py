from flask import Blueprint, render_template



job_b = Blueprint("job", __name__)




@job_b.route("/jobs/jobs")
def jobs_adver():
    return render_template("jobs/jobs_adver.html", title="Jobs")


@job_b.route("/jobs/jobs_application")
def jobs_application():
    return render_template("jobs/jobs_application.html", title="Jobs Application")

