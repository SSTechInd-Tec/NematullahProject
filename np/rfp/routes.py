from flask import Blueprint, render_template, url_for
from np import Rfp


rfp_b = Blueprint("rfps", __name__)


@rfp_b.route("/rfps", methods=['GET', 'POST'])
def rfps():
    data = Rfp.query.all()
    return render_template("rfp/rfp.html", title="RFPs", data=data)
