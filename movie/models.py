import mysql.connector


class Admin:
    def __init__(self,username,password,photo_url) :
        self.username = username
        self.password = password
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

        query = f"UPDATE moviebank.admin SET password = '{newpassword}' WHERE username = '{self.username}'"

        order = connection.cursor()
        order.execute(query)
        connection.commit()
        print("edit success")
        order.close()
        connection.close()    

class Movie:
    def __init__(self,name , country,time,rate,year,gener,summery,photo_url,adminid) :
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
        
        



