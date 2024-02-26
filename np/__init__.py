from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config["SECRET_KEY"] = "c05df40200be288b6d6e04b7c2f08d94cd6a2bef291f6bd7e9d8a7cbdaec667c"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

bcrypt = Bcrypt(app)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
from .models import Contacts, Messages, Gallery, Magazine, Certificates, Publications, AnnualReport, Rfp, Regions, Admins, News, Events, ProjectsReport
from .admin import Admin, admin_b
from .home import home_b
from .about import about_b
from .jobs import job_b
from .contacts import contacts_b
from .resources import resources_b
from .stories import stories_b
from .rfp import rfp_b
from .news import news_b
app.register_blueprint(home_b)
app.register_blueprint(about_b)
app.register_blueprint(job_b)
app.register_blueprint(contacts_b)
app.register_blueprint(resources_b)
app.register_blueprint(stories_b)
app.register_blueprint(rfp_b)
app.register_blueprint(admin_b)
app.register_blueprint(news_b)



