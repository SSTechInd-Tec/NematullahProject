from np import db, app, login_manager
from flask_login import UserMixin


class Messages(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200))
    subject = db.Column(db.String(200), nullable=False)
    msg = db.Column(db.Text())


class Contacts(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    fake_id = db.Column(db.Integer())
    name = db.Column(db.String(200), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    mobile = db.Column(db.String(200))
    email = db.Column(db.String(200))
    email2 = db.Column(db.String(200))
    deparment = db.Column(db.String(30))


class AnnualReport(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    link1 = db.Column(db.String(200))
    link2 = db.Column(db.String(200))


class Magazine(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    link1 = db.Column(db.String(200))


class Publications(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    link1 = db.Column(db.String(200))
    img = db.Column(db.String(200))


class Certificates(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    img = db.Column(db.String(200))


class Gallery(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    img = db.Column(db.String(200))
    deparment = db.Column(db.String(30))
    extra = db.Column(db.String(30))



class Rfp(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.Text())
    year = db.Column(db.String(30))
    link1 = db.Column(db.String(200))
    link2 = db.Column(db.String(200))


class Regions(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50))
    regions = db.Column(db.Text())
    img = db.Column(db.String(200))


@login_manager.user_loader
def load_user(user_id):
    return Admins.query.get(user_id)


class Admins(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50))
    passwd = db.Column(db.Text())


class News(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.Text())
    text = db.Column(db.Text())
    date = db.Column(db.String(50))
    img1 = db.Column(db.Text())
    img2 = db.Column(db.Text())
    img3 = db.Column(db.Text())
    img4 = db.Column(db.Text())
    img5 = db.Column(db.Text())


class Events(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.Text())
    text = db.Column(db.Text())
    date = db.Column(db.String(50))
    author = db.Column(db.String(50))


class ProjectsReport(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.Text())
    text = db.Column(db.Text())
    date = db.Column(db.String(50))
    img1 = db.Column(db.Text())
