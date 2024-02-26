from flask import Blueprint, render_template, url_for, redirect


stories_b = Blueprint("stories", __name__)


@stories_b.route("/stories/dreamed-hopefulness-gets-alive")
def st1():
    return render_template("stories/st1.html", title='Dreamed Hopefulness Gets Alive')


@stories_b.route("/stories/a-quick-drive-from-beggin-to-a-sustainable-livelihood")
def st2():
    return render_template("stories/st2.html", title='A Quick Drive From Begging To A Sustainable Livelihood')


@stories_b.route("/stories/using-clean-water-saves-lives")
def st3():
    return render_template("stories/st3.html", title='Using Clean Water Saves Lives')


@stories_b.route("/stories/i-see-my-life-green-now")
def st4():
    return render_template("stories/st4.html", title='I See My Life Green Now')


@stories_b.route("/stories/sakeena-36-years-old-saghreq-district")
def st5():
    return render_template("stories/st5.html", title='Sakeena 36 Years Old Saghreq District')

@stories_b.route("/stories/wajidullah-14-years-old-waziristan")
def st6():
    return render_template("stories/st6.html", title='Wajidullah 14 Years Old Waziristan')


@stories_b.route("/stories/the-life-rejuvenated")
def st7():
    return render_template("stories/st7.html", title='The Life Rejuvenated')


@stories_b.route("/stories/coar-under-the-financial-support-of-unicef")
def st8():
    return render_template("stories/st8.html", title='Coar Under The Financial Support of UNICEF')
