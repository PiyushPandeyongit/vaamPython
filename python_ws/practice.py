# friendname=[]
# friendname.append("piyush")
# friendname.append("rohit")
# friendname.append("aayush")
# for name in friendname:
#     print(name)
# # to add ajay in list after rohit
# friendname.insert(2,"ajay")
# for name in friendname:
#     print(name)
# print(type(friendname))
# a=90
# b=10
# a>b
import mysql.connector

#create database connection to mysql
connection = mysql.connector.connect(host = "localhost", 
                                     username = "root", 
                                     password = "piyushPanday90", 
                                     database = "event")

#to check the connection establish or not
if connection.is_connected():
    print("db is connected")
else:
    print("db not connected")

#to create user table in database
users = "create table if not exists users(fname text)"

#to pass the cursor handle sql query
mycursor = connection.cursor()

#to execute the sql query
mycursor.execute(users)
connection.commit()

#to insert fname in users table
insertName = "insert into users values ('{}')".format("piyush panday")
mycursor.execute(insertName)
connection.commit()
