from flask import Blueprint, render_template, url_for, redirect
from .forms import ContactsForm
from np.models import Contacts, Messages, db

contacts_b = Blueprint("contact", __name__)


@contacts_b.route("/contact", methods=['GET', 'POST'])
def contacts():
    form = ContactsForm()
    if form.validate_on_submit():
        msg = Messages(name=form.name.data, email=form.email.data, subject=form.subject.data, msg=form.msg.data)
        db.session.add(msg)
        db.session.commit()
        return redirect("/home")
    data1 = Contacts.query.filter_by(deparment='personal')
    data2 = Contacts.query.filter_by(deparment='REGIONAL')
    data3 = Contacts.query.filter_by(deparment='ENGINEERS')
    return render_template("contacts/contacts.html", title="Contact Us", form=form, data1=data1, data2=data2, data3=data3)
