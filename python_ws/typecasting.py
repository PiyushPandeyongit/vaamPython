'''#  typecating convert one data type to another data type
price =90.59
print(price)
print(type(price))

# convert to integer
payPrice=int(price)
print(payPrice)
print(type(payPrice))

# convert integer to string
amount=2599
stringAmount=str(amount)
print(stringAmount,"and data type is ",type(stringAmount))

# convert string into integer
# gender="male"
# genderintoInt=int(gender)
# conversion not possible because string don't habe ascii number 
# conversion of single character is p[ossible
# print(gender,"data type is",type(genderintoInt))

# to take input from user input() is replacement of  scanf()which we use in c
myName=input("enter your name")
# myAge=int(input("enter your age")) not run because string not add with int 
myAge=input("enter your age")
# print("MY NAME IS" , myName)
print("MY NAME IS " + myName +  myAge)
# input function has return type of string default data type
# print("MY NAME IS " + myName ,  myAge) 
  
  # find age 
currentYear=int(input("enter current year"))
birthYear=int(input("enter birth year"))
yourAge=currentYear-birthYear
print("yourage is", yourAge)
 
#  conversion of rupees in dollar
currencyinRupee=int(input("enter rupee:"))
yourcurrencyinDollar=currencyinRupee*83
print("conversion of rupees in dollar",yourcurrencyinDollar)'''

name="Piyush"
age=19
salary=19990.90
# show to pass the variable inside the print statement
# you have 3 ways to pass trhe variable in print statement
# print("My name is "+name"and salary"+salary+"and age"+age)
# it generate the type error ,reason string only concatenate with string not int
# solutin 1: replace + by ,when data type is notb string
# print("My name is "+ name+" and salary",salary,"and age ",age)
# solution 2: pass the variable in print statement in f()
# print(f"My name is (name) salary is (salary) and age(age)") 
# solution 3: typecast the data into string
salarystring=str(salary)
agestring=str(age)
print("My name is "+name+" and age is "+ agestring +" salary is "+ salarystring)
# To find the type of data we need to use type () function
print(type(name))
print(type(age))
print(type(salary ))

