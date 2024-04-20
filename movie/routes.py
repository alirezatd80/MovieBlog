from flask import render_template
from movie import app

@app.route('/')
def mainpage():
    return render_template("app-landing.html")