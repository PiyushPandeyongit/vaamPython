import mysql.connector

#create database connector to mysql
# dtabase connection set above 
connection=mysql.connector.connect(host="localhost",
                                  username="root",
                                  password="piyushPanday90",
                                  database="event")

# to check the connection establish or not
if connection.is_connected():
     print("db is connected")
else:
     print("db is not connected")     

#to create user table in database
users = "create table if not exists user(fname text)"
# to pass the curson handle sql query
# curssor works like pointer
mycursor=connection.cursor()

# to execute the sql query
mycursor.execute(users)
connection.commit()
# import mysql.connector

# # create databases connection to mysql
# connection = mysql.connector.connect(host = "localhost",
#                                      username = "root",
#                                      password = "piyushPanday90",
#                                      database = "event")

# # to check the connection establish or not
# if connection.is_connected():
#     print("db is connected")
# else:
#     print("db not connected")

# # to create user table in database
# users = "create table if not exists user(fname text)"

# #to pass the cursor handle sql query
# mycursor = connection.cursor()

# #to execute the sql query
# mycursor.execute(users)
# connection.commit()

# # to insert name in table
# insertName="insert into users value('{}','{}')".format('piyush')
# insertName = "insert into users  value('()', '()')".format('piyush'),
insertName = "insert into users values ('{}')".format("pawan sharma")
mycursor.execute(insertName)
connection.commit()