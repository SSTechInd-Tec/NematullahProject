from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import FileUploadField
from np import app, db, Contacts, Messages, Gallery, Magazine, Certificates, Publications, AnnualReport, Rfp, Regions, Admins, News, Events, ProjectsReport
from flask import Blueprint, flash, redirect, render_template, url_for, request
from .forms import LoginForm
from np import bcrypt
from flask_login import login_user, logout_user, current_user
from flask_admin.menu import MenuLink
from flask_wtf.file import FileRequired, FileAllowed

admin_b = Blueprint("admin_b", __name__)


@admin_b.route("/admin/login", methods=["POST", "GET"])
def login_admin():
    form = LoginForm()
    if form.validate_on_submit():
        user = Admins.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.passwd, form.password.data):
            flash("Successfully Login", "success")
            login_user(user)
            return redirect("/admin")
        else:
            flash("Unsuccessfully Login! Try Again", "danger")
    return render_template("admin/login.html", form=form)


@admin_b.route("/admin/logout")
def admin_logout():
    logout_user()
    return redirect(url_for("admin_b.login_admin"))


class MyAdminView(AdminIndexView):
    @expose("/")
    def index(self):
        return self.render("admin/index.html")

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("admin_b.login_admin"))


class BaseView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("admin_b.login_admin"))

    list_template = "admin/list_view.html"
    create_template = "admin/create_view.html"
    edit_template = "admin/edit_view.html"


class AnnualView(BaseView):
    form_overrides = {
        'link1': FileUploadField,
        'link2': FileUploadField,
    }

    form_args = {
        'link1': {'base_path': f'{app.root_path}/static/pdfs/annual_report'},
        'link2': {'base_path': f'{app.root_path}/static/pdfs/annual_report'}
    }

    def on_model_change(self, form, model, is_created):
        if type(form.link1.data) != str or type(form.link1.data) == 'NoneType':
            model.link1 = form.link1.data.filename
        else:
            model.link1 = model.link1

        if type(form.link2.data) == 'NoneType':
            model.link2 = form.link2.data.filename
        else:
            model.link2 = model.link2


class MagazineView(BaseView):
    form_overrides = {
        'link1': FileUploadField,
    }

    form_args = {'link1': {'base_path': f'{app.root_path}/static/pdfs/magazine'}}

    def on_model_change(self, form, model, is_created):
        if type(form.link1.data) != str or type(form.link1.data) == 'NoneType':
            model.link1 = form.link1.data.filename
        else:
            model.link1 = model.link1


class GalleryView(BaseView):
    form_overrides = {
        'img': FileUploadField,
    }

    form_args = {'img': {'base_path': f'{app.root_path}/static/gallery'}}

    def on_model_change(self, form, model, is_created):
        if type(form.img.data) != str or type(form.img.data) == 'NoneType':
            model.img = form.img.data.filename
        else:
            model.img = model.img


class PublicationsView(BaseView):
    form_overrides = {
        'link1': FileUploadField,
        'img': FileUploadField,
    }

    form_args = {
        'link1': {'base_path': f'{app.root_path}/static/pdfs/publications/pdfs', 'validators': [FileRequired()]},
        'img': {'base_path': f'{app.root_path}/static/pdfs/publications/imgs', 'validators': [FileRequired()]}
    }

    def on_model_change(self, form, model, is_created):
        if type(form.link1.data) != str or type(form.link1.data) == 'NoneType':
            model.link1 = form.link1.data.filename
        else:
            model.link1 = model.link1

        if type(form.img.data) == 'NoneType':
            model.img = form.img.data.filename
        else:
            model.img = model.img


class CertificatesView(BaseView):
    form_overrides = {
        'img': FileUploadField,
    }

    form_args = {'img': {'base_path': f'{app.root_path}/static/certificates'}}

    def on_model_change(self, form, model, is_created):
        if type(form.img.data) != str or type(form.img.data) == 'NoneType':
            model.img = form.img.data.filename
        else:
            model.img = model.img


class RfpsView(BaseView):
    form_overrides = {
        'link1': FileUploadField,
        'link2': FileUploadField,
    }

    form_args = {
        'link1': {'base_path': f'{app.root_path}/static/pdfs/rfps'},
        'link2': {'base_path': f'{app.root_path}/static/pdfs/rfps'}
    }

    def on_model_change(self, form, model, is_created):
        if type(form.link1.data) != str or type(form.link1.data) == 'NoneType':
            model.link1 = form.link1.data.filename
        else:
            model.link1 = model.link1

        if type(form.link2.data) == 'NoneType':
            model.link2 = form.link2.data.filename
        else:
            model.link2 = model.link2


class RegionsView(BaseView):
    form_overrides = {
        'img': FileUploadField,
    }

    form_args = {'img': {'base_path': f'{app.root_path}/static/regions'}}

    def on_model_change(self, form, model, is_created):
        if type(form.img.data) != str or type(form.img.data) == 'NoneType':
            model.img = form.img.data.filename
        else:
            model.img = model.img


class AdminsView(BaseView):
    can_delete = False
    can_create = False

    def on_model_change(self, form, model, is_created):
        if form.passwd.data:
            model.passwd = bcrypt.generate_password_hash(form.passwd.data).decode()
        else:
            model.passwd = model.passwd


class NewsView(BaseView):
    form_overrides = {
        'img1': FileUploadField,
        'img2': FileUploadField,
        'img3': FileUploadField,
        'img4': FileUploadField,
        'img5': FileUploadField,
    }

    form_args = {
        'img1': {'base_path': f'{app.root_path}/static/news'},
        'img2': {'base_path': f'{app.root_path}/static/news'},
        'img3': {'base_path': f'{app.root_path}/static/news'},
        'img4': {'base_path': f'{app.root_path}/static/news'},
        'img5': {'base_path': f'{app.root_path}/static/news'},
    }

    def on_model_change(self, form, model, is_created):
        if type(form.img1.data) != str or type(form.img.data) == 'NoneType':
            model.img1 = form.img1.data.filename
        else:
            model.img1 = model.img1

        if type(form.img2.data) == 'NoneType':
            model.img2 = form.img2.data.filename
        else:
            model.img2 = model.img2

        if type(form.img3.data) == 'NoneType':
            model.img3 = form.img3.data.filename
        else:
            model.img3 = model.img3

        if type(form.img4.data) == 'NoneType':
            model.img4 = form.img4.data.filename
        else:
            model.img4 = model.img4

        if type(form.img5.data) == 'NoneType':
            model.img5 = form.img5.data.filename
        else:
            model.img5 = model.img5


class ProjectsReportView(BaseView):
    form_overrides = {
        'img1': FileUploadField,
    }

    form_args = {
        'img1': {'base_path': f'{app.root_path}/static/events'},
    }

    def on_model_change(self, form, model, is_created):
        if type(form.img1.data) != str or type(form.img.data) == 'NoneType':
            model.img1 = form.img1.data.filename
        else:
            model.img1 = model.img1


admin = Admin(app, template_mode="bootstrap4", name="COAR", index_view=MyAdminView())
admin.add_view(AnnualView(AnnualReport, db.session))
admin.add_view(MagazineView(Magazine, db.session))
admin.add_view(GalleryView(Gallery, db.session))
admin.add_view(PublicationsView(Publications, db.session))
admin.add_view(CertificatesView(Certificates, db.session))
admin.add_view(BaseView(Messages, db.session))
admin.add_view(BaseView(Contacts, db.session))
admin.add_view(RfpsView(Rfp, db.session))
admin.add_view(RegionsView(Regions, db.session))
admin.add_view(AdminsView(Admins, db.session))
admin.add_view(NewsView(News, db.session))
admin.add_view(BaseView(Events, db.session))
admin.add_view(ProjectsReportView(ProjectsReport, db.session))
admin.add_link(MenuLink(name="Website", category="", url="/"))
admin.add_link(MenuLink(name="Logout", category="", url="/admin/logout"))
