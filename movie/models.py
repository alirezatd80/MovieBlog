import mysql.connector
import hashlib

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password
    

class Admin:
    def __init__(self,username,password,photo_url) :
        self.username = username
        self.password = hash_password(password)
        self.photo_url = photo_url
    
    def add(self ):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1111",
            database="moviebank"
        )
        query = f"INSERT INTO `moviebank`.`admin` (`username`, `password`, `photo_url`) VALUES ('{self.username}', '{self.password}', '{self.photo_url}');"
        
        order = connection.cursor()
    
        order.execute(query)
        connection.commit()
        print("add success")
        order.close()
        connection.close()
    
    def del_user(self):
        connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1111",
        database = "moviebank")

        query = f"DELETE FROM moviebank.admin WHERE username='{self.username}'"

        order = connection.cursor()
        order.execute(query)
        connection.commit()
        print("del success")
        order.close()
        connection.close()
    
    def edit_admin(self,newpassword ):
        connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1111",
        database = "moviebank")
        hash_newpassword = hash_password(newpassword)
        query = f"UPDATE moviebank.admin SET password = '{hash_newpassword}' WHERE username = '{self.username}'"

        order = connection.cursor()
        order.execute(query)
        connection.commit()
        print("edit success")
        order.close()
        connection.close()    

    def getall()->list:
        admins = []
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1111",
            database="moviebank"
        )
        query = f"SELECT * FROM moviebank.admin;"
        
        order = connection.cursor()
    
        order.execute(query)
        admins = order.fetchall()
        
        order.close()
        connection.close()
        return admins
    
    def get_admin(username):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1111",
            database="moviebank"
        )
        query = f"SELECT * FROM moviebank.admin where username = '{username}';"
        
        order = connection.cursor()
    
        order.execute(query)
        admin = order.fetchall()
        
        order.close()
        connection.close()
        return admin
    
    def is_user(username , password) -> bool: 
        usernames = [] 
        adminlist = Admin.getall()
        for i in adminlist:
            usernames.append(i[1])
        if username in usernames:
            test = Admin.get_admin(username)
            user = test[0]
            if password == user[2]:
                return True
            else:
                return False
            
        else:
            return False
    def NumberAdmin()->int:
        admins = Admin.getall()
        return len(admins)
    
        

            
class Movie:
    def __init__(self,name , country,time:0,rate,year,gener,summery,photo_url,adminid) :
        self.name = name
        self.country = country
        self.time = time
        self.rate = rate
        self.year = year
        self.gener = gener
        self.summery = summery
        self.photo_url = photo_url
        self.adminid = adminid
        
    def addmovie(self):
         connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1111",
            database="moviebank"
        )
         
         query = "INSERT INTO movies (name, country, time , rate, year, gener, summery , photo_url , adminid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
         values = (f"{self.name}", f"{self.country}", f"{self.time} " , f"{self.rate} " , f"{self.year} " ,f"{self.gener} " ,f"{self.summery} " ,f"{self.photo_url} " ,f"{self.adminid} ")
         
         order = connection.cursor()
    
         order.execute(query,values)
         connection.commit()
         print("add success")
         order.close()
         connection.close()
        
    def delmovie(self):
        connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1111",
        database = "moviebank")

        query = f"DELETE FROM moviebank.movies WHERE name='{self.name}'"

        order = connection.cursor()
        order.execute(query)
        connection.commit()
        print("del success")
        order.close()
        connection.close()    
    
    def editemovie(self,newname , newcountry,newtime,newrate,newyear,newgener,newsummery,newphoto_url ):
        connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1111",
        database = "moviebank")

        query = f"UPDATE moviebank.movies SET name = '{newname}', country = '{newcountry}',time = '{newtime}',rate = '{newrate}',year = '{newyear}',gener = '{newgener}',summery = '{newsummery}',photo_url = '{newphoto_url}' WHERE name = '{self.name}'"

        order = connection.cursor()
        order.execute(query)
        connection.commit()
        print("edit success")
        order.close()
        connection.close() 
        
    
    def get_all_movies()->list:
        movies = []
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1111",
            database="moviebank"
        )
        query = f"SELECT * FROM moviebank.movies;"
        
        order = connection.cursor()
    
        order.execute(query)
        movies = order.fetchall()
        
        order.close()
        connection.close()
        return movies
    def GetMoviesbyID(adminid)-> list:
        movies = []
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1111",
            database="moviebank"
        )
        query = f"SELECT * FROM moviebank.movies where adminid ={adminid};"
        
        order = connection.cursor()
    
        order.execute(query)
        movies = order.fetchall()
        
        order.close()
        connection.close()
        return movies
    def GetMoviesbyname(name):
        
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1111",
            database="moviebank"
        )
        query = f"SELECT * FROM moviebank.movies where name = '{name}';"
        
        order = connection.cursor()
    
        order.execute(query)
        movie = order.fetchall()
        
        order.close()
        connection.close()
        return movie
    def delmoviebyname(name):
        movieselect = Movie.GetMoviesbyname(name)
        movie = movieselect[0]
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1111",
            database="moviebank"
        )
        query = f"DELETE FROM `moviebank`.`movies` WHERE (`id` = {movie[0]}) and (`adminid` = {movie[9]});"
        
        order = connection.cursor()
        order.execute(query)
        
        connection.commit()
        order.close()
        connection.close()
        
        
    def GetMovieByTag(tag):
        movies = Movie.get_all_movies()
        listresult = []
        for i in movies:
            if tag in i[6]:
                listresult.append(i)
        return listresult
        
            
        
        
class Comment:
    def __init__(self,name , email , phone , message):
        self.name = name
        self.email = email
        self.phone = phone
        self.message = message
    
    def addcomment(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1111",
            database="moviebank"
        )
         
        query = "INSERT INTO comment (name, email, phone , message) VALUES (%s, %s, %s, %s)"
        values = (f"{self.name}", f"{self.email}", f"{self.phone} " , f"{self.message} ")
         
        order = connection.cursor()
    
        order.execute(query,values)
        connection.commit()
        print("add success")
        order.close()
        connection.close()
    def get_all_comment()->list:
        comments = []
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1111",
            database="moviebank"
        )
        query = f"SELECT * FROM moviebank.comment;"
        
        order = connection.cursor()
    
        order.execute(query)
        comments = order.fetchall()
        
        order.close()
        connection.close()
        return comments
        
        

admin = Admin('alireza','1111',"../static/adminpagemain/dist/img/alirezaadminphoto.jpg")
admin2 = Admin('reza','12345678',"../static/adminpagemain/dist/img/rezaadmin.jpg")
admin3 = Admin('ali','11111111',"../static/adminpagemain/dist/img/aliadmin.jpg")






