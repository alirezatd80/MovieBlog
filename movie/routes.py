from flask import render_template, url_for ,request ,redirect
from movie import app
from movie import models

@app.route('/')
def mainpage():
    return render_template("app-landing.html")

@app.route('/Movies')
def mainmovies():
    return render_template("movies.html")

@app.route('/mavoiepage')
def moviepage():
    return render_template("singlemoviepage.html")

@app.route('/adminlog' , methods = ['GET' , 'POST'])
def adminlog():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('pass')
        if models.Admin.is_user(username , password):
            adminlogging = models.Admin.get_admin(username)
            return redirect(url_for('adminpageindex'))
            
        else:
           return render_template("adminpagelogin.html")
    else:
        return render_template("adminpagelogin.html")
    
@app.route('/xopnsjha' , methods = ['GET' , 'POST'])
def adminpageindex():
    return render_template('adminpage/starter.html')
    