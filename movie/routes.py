from flask import render_template, url_for
from movie import app

@app.route('/')
def mainpage():
    return render_template("app-landing.html")

@app.route('/Movies')
def mainmovies():
    return render_template("movies.html")