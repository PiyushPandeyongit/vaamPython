#Class -> is collection of objects and functions...
# rules: 1st letter is in uppercase
class Piyush:
    print("My name is Piyush Panday.")
    age=18;
    email = "piyushpanday2006@gmail.com"

#object creation
piyush : Piyush = Piyush() 
print("My age is",piyush.age)



class Student:
    name = "piyush"
    email = "d@gmail.com"
    def findMyAge(this, cY, bY):      #this -> passes current class reference...
        ageInYear = cY-bY
        print(ageInYear)
    def Monthly_Pocket_Money(this,weekly_money):
        totalMoney = weekly_money*4
        print("My Pocket Money",totalMoney)
        #print("Monhly pocket money is",weekly_money*4)
stu : Student = Student()
stu.findMyAge(2024,2005)
#stu.Monthly_Pocket_Money(200)
stu.Monthly_Pocket_Money(int(input("Enter Weekly money: ")))



#Calculate the top speed of the car if each gear increase car speed by 50 km/h.
class Car:
    model= 2024
    gears= 7 
    first_gear=50
    
    def top_speed(this, gear):
        print("The top speed is :",50*gear)
car: Car = Car()
car.top_speed(int(input("Enter gear number (1-7) : ")))