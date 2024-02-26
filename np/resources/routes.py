from flask import Blueprint, render_template, url_for, redirect
from np.models import AnnualReport, Magazine, Publications, Certificates, Gallery, db

resources_b = Blueprint("resources", __name__)


@resources_b.route("/resources/annual_report", methods=['GET', 'POST'])
def annual_report():
    data = AnnualReport.query.all()
    return render_template("resources/annual_report.html", title="Annual Report", data=data)


@resources_b.route("/resources/magazine", methods=['GET', 'POST'])
def magazine():
    data = Magazine.query.all()
    return render_template("resources/magazine.html", title="Payam-e-Inkashaf Magazine", data=data)


@resources_b.route("/resources/publications", methods=['GET', 'POST'])
def publications():
    data = Publications.query.all()
    return render_template("resources/publications.html", title="Publications", data=data)


@resources_b.route("/resources/certificates", methods=['GET', 'POST'])
def certificates():
    data = Certificates.query.all()
    return render_template("resources/certificates.html", title="Certificates", data=data)


@resources_b.route("/resources/gallery", methods=['GET', 'POST'])
def gallery():
    data1 = Gallery.query.filter_by(deparment='activity')
    data2 = Gallery.query.filter_by(deparment='WASH')
    data3 = Gallery.query.filter_by(deparment='agriculture')
    data4 = Gallery.query.filter_by(deparment='education')
    data5 = Gallery.query.filter_by(deparment='rural')
    data6 = Gallery.query.filter_by(deparment='engineering')
    data7 = Gallery.query.filter_by(deparment='training')
    return render_template("resources/gallery.html", title="Gallery", data1=data1, data2=data2, data3=data3
                           , data4=data4, data5=data5, data6=data6, data7=data7)
