from flask import Blueprint, render_template, url_for, redirect
from np import News, Events, ProjectsReport


news_b = Blueprint("news_", __name__)


def trim(text):
    d = []
    for i in range(1, 201):
        d.append(text[i])

    return "".join(d)


def inc(i):
    return i+1


def dec(i):
    return i-1

@news_b.route("/newses", methods=['GET', 'POST'])
def news():
    data = News.query.limit(8).all()
    data2 = Events.query.limit(3).all()
    data3 = ProjectsReport.query.all()
    return render_template("news/news.html", title="News and Events", data=data,
                           data2=data2, data3=data3, trim=trim)


@news_b.route("/newses/page/<int:nid>", methods=['GET', 'POST'])
def news_page(nid):
    data = News.query.get(nid)
    last_id = News.query.order_by(News.id.desc()).first().id
    return render_template("news/page.html", title="News and Events",
                           data=data, inc=inc, dec=dec, last_id=last_id)


@news_b.route("/newses/all", methods=['GET', 'POST'])
def all_news():
    data = News.query.all()
    return render_template("news/all-news.html", title="News and Events", data=data, trim=trim)


@news_b.route("/events/page/<int:nid>", methods=['GET', 'POST'])
def events_page(nid):
    data = Events.query.get(nid)
    last_id = Events.query.order_by(Events.id.desc()).first().id
    return render_template("news/events.html", title="News and Events",
                           data=data, inc=inc, dec=dec, last_id=last_id)

@news_b.route("/events/all", methods=['GET', 'POST'])
def all_events():
    data = Events.query.all()
    return render_template("news/all-events.html", title="News and Events", data=data, trim=trim)


@news_b.route("/report/page/<int:nid>", methods=['GET', 'POST'])
def reports_page(nid):
    data = ProjectsReport.query.get(nid)
    last_id = ProjectsReport.query.order_by(ProjectsReport.id.desc()).first().id
    return render_template("news/reports.html", title="News and Events",
                           data=data, inc=inc, dec=dec, last_id=last_id)


@news_b.route("/reports/all", methods=['GET', 'POST'])
def all_reports():
    data = ProjectsReport.query.all()
    return render_template("news/all-reports.html", title="News and Events", data=data, trim=trim)

