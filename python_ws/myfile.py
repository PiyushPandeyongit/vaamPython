#create file in python with name and extension
myFile=open("piyush.txt","w")
#write name and 
myFile.write('''My name is piyush pandey and email id : piyushpandey@gmailcom''')
#to close the file
myFile.close()

#Read the data from file
readFile=open("piyush.txt","r")
print(readFile.read())



# #Delete the file
# import os
# os.remove("Devansh.txt")



#Create stock api in json -> java script object notation
myStock=open("myStock.json","w")
#myStock.write("this is my stock api")    not a json data
# {} -> JsonObject  , []-> JsonArray
myStock.write('''{"name":"Piyush pandey"}''')
readStock=open("myStock.json","r")
print(readStock.read())


#read and write the data in xls, csv and json files.....
import os
os.remove("Devansh.txt")

