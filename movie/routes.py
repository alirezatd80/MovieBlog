from flask import render_template, url_for ,request ,redirect
from movie import app
from movie import models
import hashlib

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
    message = 'hi'
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('pass')
        hash_pass = hashlib.sha256(password.encode()).hexdigest()
        if models.Admin.is_user(username , hash_pass):
            adminlogging = models.Admin.get_admin(username)
            return redirect(url_for('adminpageindex'))
            
        else:
           message = 'incorrect username or password'
           
           return render_template("adminpagelogin.html",message=message)
    
    
@app.route('/xopnsjha' , methods = ['GET' , 'POST'])
def adminpageindex():
    return render_template('adminpage/starter.html')
    