from flask import render_template, url_for ,request ,redirect,session
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
        givinformation = models.Admin.get_admin(username)
        if models.Admin.is_user(username , hash_pass):
            
            session['admin'] = givinformation[0]
            session['admin_is_log'] = True
            return redirect(url_for('adminpageindex'))
            
        else:
           message = 'incorrect username or password'
           
           return render_template("adminpagelogin.html",message=message)
    else:
        return render_template("adminpagelogin.html")
    
@app.route('/adminpageindex' , methods = ['GET' , 'POST'])
def adminpageindex():
    if 'admin_is_log' in session and session['admin_is_log']:
        adminloggin = session['admin']
        return render_template('adminpage/starter.html',admin = adminloggin)
    else:
        return redirect(url_for('adminlog'))
    