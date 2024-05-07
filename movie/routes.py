from flask import render_template, url_for ,request ,redirect,session
from movie import app
from movie import models
import hashlib



    
@app.route('/',methods = ['POST' , 'GET'])
def mainpage():
    numberAdmin = models.Admin.NumberAdmin()
    numberMovie = len(models.Movie.get_all_movies())
    mov = session['movieday']
    movieday = mov[0]
    return render_template("app-landing.html",numberAdmin = numberAdmin,numberMovie = numberMovie,movieday=movieday)    
       
        
        
  
@app.route('/sendmessage',methods = ['POST' , 'GET'])
def sendmessage():
    if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            phone = request.form.get('phone_number')
            message = request.form.get('message')
            mess = models.Comment(name,email,phone,message)
            mess.addcomment()
    return redirect(url_for('mainpage'))
            
 

@app.route('/Movies')
def mainmovies():
    movies= models.Movie.get_all_movies()
    return render_template("movies.html",movies = movies)

@app.route('/mavoiepage')
def moviepage():
    return render_template("singlemoviepage.html")

@app.route('/adminlog' , methods = ['GET' , 'POST'])
def adminlog():
    if 'admin_is_log' in session and session['admin_is_log']:
        return redirect(url_for('adminpageindex'))
    else:
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
        comments = models.Comment.get_all_comment() 
        return render_template('adminpage/starter.html',admin = adminloggin,comments = comments)
    else:
        return redirect(url_for('adminlog'))
    
    
@app.route('/moviepage',methods = ['GET' , 'POST'])
def Movieadmin():
    adminloggin = session['admin']
    movies = models.Movie.GetMoviesbyID(adminloggin[0])
    return render_template('adminpage/movies.html',admin = adminloggin,movies = movies)   

@app.route('/addmovie',methods = ['GET' , 'POST'])
def addmovieadmin():
    adminloggin = session['admin']
    name = request.form.get('moviename')
    country = request.form.get('contry')
    time=request.form.get('time')
    year= request.form.get('year')
    gener = request.form.get('gener')
    imdb = request.form.get('imdb')
    summery = request.form.get('summery')
    picture = request.form.get('picture')
    url = f"../static/img/movies/{picture}"
    movie = models.Movie(name,country,time,imdb,year,gener,summery,url,adminloggin[0])
    movie.addmovie()
    return redirect(url_for('Movieadmin'))
        

@app.route('/addmoviepage',methods = ['GET' , 'POST'])
def addmoviepageadmin():
    adminloggin = session['admin']
    return render_template('adminpage/addmovie.html',admin = adminloggin)


@app.route('/logout')
def logout():
    session.pop('admin_is_log' , None)
    return redirect(url_for('mainpage'))

@app.route('/movieday' , methods = ['POST','GET'])
def movieday():
    moviename = request.form.get('moviename')
    movie  = models.Movie.GetMoviesbyname(moviename)
    session['movieday'] = movie
    return redirect(url_for('mainpage'))

@app.route('/deletemovie',methods=['GET'])
def deletemovie():
    movieName = request.args.get('movname')
    models.Movie.delmoviebyname(movieName)
    return redirect(url_for('Movieadmin'))
    
@app.route('/editmovie' ,methods=['POST','GET'] )  
def editMovie():
    adminloggin = session['admin']
    moviename = request.args.get('movname') 
    Contry = request.args.get('country') 
    Time = request.args.get('time') 
    imdb = request.args.get('imdb') 
    Year = request.args.get('year') 
    Gener = request.args.get('Gener') 
    summery = request.args.get('summery') 
    photourl= request.args.get('photourl') 
    movieedit = models.Movie.GetMoviesbyname(moviename)
    session['movieedit'] = movieedit[0]
    return render_template('adminpage/editpage.html',name = moviename ,Contry=Contry,Time=Time,imdb=imdb,Year=Year,Gener=Gener,summery=summery,photourl=photourl,admin = adminloggin )
    
    
@app.route('/submitedit' , methods=['POST','GET'] )  
def  submitedit():
    
    moviename = request.form.get('moviename') 
    Contry = request.form.get('contry') 
    Time = request.form.get('time') 
    year = request.form.get('year') 
    gener = request.form.get('gener') 
    imdb = request.form.get('imdb') 
    summery = request.form.get('summery') 
    photourl= request.form.get('picture')
    url = f"../static/img/movies/{photourl}"
    movieedit = session['movieedit']
    mov = models.Movie(movieedit[1],movieedit[2],movieedit[3],movieedit[4],movieedit[5],movieedit[6],movieedit[7],movieedit[8],movieedit[9])
    mov.editemovie(moviename,Contry,Time,year,gener,imdb,summery,url)
    return redirect(url_for('Movieadmin'))
    
    
@app.route('/moviesbytag/<tag>')   
def moviesbytag(tag):
    adminloggin = session['admin']
    movies = models.Movie.GetMovieByTag(tag)
    return render_template("movies.html",movies = movies)  