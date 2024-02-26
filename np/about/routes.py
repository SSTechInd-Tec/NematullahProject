from flask import Blueprint, render_template, url_for

about_b = Blueprint("about", __name__)


@about_b.route("/about/founder_msg")
def founder_msg():
    return render_template("about/founder_msg.html", title="Founder Message")


@about_b.route("/about/coar_at_glance")
def coar_at_glance():
    return render_template("about/coar-at-glance.html", title="COAR At Glance")


@about_b.route("/about/thematic_areas")
def thematic_areas():
    return render_template("about/thematic_areas.html", title="Thematic Areas")


@about_b.route("/about/code_of_contact")
def code_of_contact():
    return render_template("about/code_of_contact.html", title="Code of Contact")


@about_b.route("/about/organizational_chart")
def organizational_chart():
    return render_template("about/organizational_chart.html", title="Organizational Chart")


@about_b.route("/about/strategic_plan")
def strategic_plan():
    return render_template("about/strategic_plan.html", title="Strategic Plan")


@about_b.route("/about/policy_documents")
def policy_documents():
    return render_template("about/policy_documents.html", title="Policy Documents")


@about_b.route("/about/cluster_coordination")
def cluster_coordination():
    return render_template("about/cluster_coordination.html", title="Cluster Coordination")


@about_b.route("/about/donors")
def donors():
    return render_template("about/donors.html", title="Donors")
