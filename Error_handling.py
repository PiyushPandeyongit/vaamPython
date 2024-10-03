'''tab space is called indentation
try:
     error
exception :type of error
    print("......")
this above is used to b[pass error in big program'''
# print(x) #it is name error
try:
    print(x)
except NameError:
    print("Namerror ")

# y=1/0 it is an error

    
try:
    y=1/0
    print(y)
except ZeroDivisionError:
    print("zeroDivisonerror")

# a="Pawan"
# b=int(a)
# print(b)    
      
try:
    a="Pawan"
    b=int(a)
    print(b)   
except ValueError:
    print("valueError... string not typecast into integer")


import os
# os.remove("myfile.txt")   filenotfoundingerror

try:
    # put only whose line which generate error
    os.remove("myfile.txt")
except FileNotFoundError:
      print("filenotfounderror")    

myList=["Pawan","manan","kanak"]
# print(myList[4]) thios line generate error

try:
    print(myList[4])
except IndexError:
    print("Indexerror")    
          
# x=5
# try;
#     if x>5:
#     print(x)
#     else:
#     print(x)
# except IndentationError:    
#      print("indentationerror")   this error also not handle by try
# we can only handl;e thid manually

x="pawan"
y=4
c=x*y
print(c)   

x="pawan"
y=4
# c=x+y type error
# print(c)   

try:
    c=x+y
    print(c)
except TypeError:
    print("typeError")   
finally:
    print("it's always run") 

# finally : always run