#PYHTON PRACTICE


#VARIABLES


x=1
y="Ayush"
print(x)
print(y)


#MULTIPLE VARIABLES


x,y,z = "Ayush","Ayush1","Ayush2"
print(x,y,z)


#GLOBAL VARIABLES


a="Ayush"

def myfunc():
    a="Ayush1"
    print("Python is "+a)

    myfunc()
    print("Python is"+a)


#DATATYPES


#Text Str 
#Numeric int,float 12,2.5
#sequence list,tuple
#boolean bool


#CASTING


x=int(1) #output=1   
x=int(2.8) #output=2  
x=int("3") #output=3


#STRINGS


txt="Ayush in game name is Reflexgod"
print(txt)


#BOOLEAN


a=200
b=33
if b>a:
    print("b is greater than than a")
else:
     print("a is greater than than b")


#OPERATOR


# +	    Addition	    x + y	
# -	    Subtraction	    x - y	
# *	    Multiplication	x * y	
# /	    Division	    x / y	
# %	    Modulus	        x % y	
# **	    Exponentiation	x ** y	
# //	    Floor division	x // y


#LISTS


thislist=["Ayush","33clutch","reflexgod"]
print(thislist)
    
#changelist
thislist.insert(2,"crusher")
print(thislist)

#additem
thislist.append("Orange")
print(thislist)

tropical=["mango","apple"]
thislist.extend(tropical)
print(thislist)

#remove
thislist.remove("banana")
print(thislist)

#sortlist
thislist.sort()
print(thislist)

#joinlist
list3=thislist + tropical
print(list3)


#TUPLE


thistuple=("Ayush","33clutch","reflexgod","Ramesh")
print(thistuple)

#Slicing
tuple2=thistuple[1:3]
tuple3=thistuple[:2] #Blank represents 0 here

#jointuple
tuple2=("bgmi","pubg")
tuple3=thistuple  + tuple2
print(tuple3)

#count
#number of time elements repeated


#SETS


thisset={"apple","banana","cherry"}
print(thisset)

#accessset
thisset={"apple","banana","cherry"}
for x in thisset:
 print(x)

#add
thisset.add("orange")
print(thisset)

#remove
thisset.remove("banana")
thisset.pop() #Delete last item
print(thisset)

#join
set1={"a","b","c"}
set2={1,2,3}
set3=set1.union(set2)
print(set3)

#update
#intersaction
#difference


#DICTIONARY


thisdict={
    "brand":"Ford", #key:value
    "model":"Mustang",
    "year":2023,
}
print(thisdict)

#remove
thisdict.pop("model")
print(thisdict)

#Nested Dictionary
myfamily = {
  "child1" : {
    "name" : "Ayush",
    "year" : 2002
  },
  "child2" : {
    "name" : "Aayush",
    "year" : 2001
  },
  "child3" : {
    "name" : "Parshwa",
    "year" : 2003
  }
}
print(myfamily)


#IF...ELSE


a = 200
b = 33
if b > a:
  print("b is greater than a")

#print("a") if a>b else print("b")

elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


#WHILE LOOP


i = 1
while i < 6:
  print(i)
  if i == 3:
    break   #breakstatement
  i =i + 1


#FOR LOOP


#continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


#FUNCTION


def my_function(fname):
  print(fname + " Patel")

my_function("Ayush")
my_function("Clutch")
my_function("Reflexgod")

#args
def my_function(*x):
  print("My Name is " + x[2])

my_function("Ayush", "Clutch", "Reflexgod")

#kwargs
def my_function(**x):
  print("My Last Name is " + x["lname"])

my_function(fname = "Soni", lname = "Patel")

#ReturnValues
def ans(x):
  return 5 * x

print(ans(3))
print(ans(5))
print(ans(9))


#RECURSION FUNCTION


def recursion(k):
  if(k > 0):
    result = k + recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
recursion(6)

#Factorial by recursion
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(3))
print(factorial(4))
print(factorial(5))


#FIBONACCI


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage
n_terms = 10
for i in range(n_terms):
    print(fibonacci(i))


#ARRAY


#LAMBDA


def myfunc(n):
 return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


double=lambda x:x*2
print(double(2))


# MAP


def cube(x):
   return x*x*x

l=[1,2,3,4]
newl=list(map(cube,l))
# newl=list(map(lambda x:x*x*x,l))
print(newl)


#FILTER


def filter_fun(a):
 return a>3

newnewl=list(filter(filter_fun,newl))
print(newnewl)


# REDUCE


from functools import reduce
l1=[1,2,3,4]
sum=reduce(lambda x,y: x+y,l1)
print(sum)


#CLASS


#init
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Ayush", 21)

print(p1.name)
print(p1.age)

#str
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"Name={self.name} Age={self.age}"

p1 = Person("Ayush", 21)

print(p1)

# object method
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Ayush", 21)
p1.myfunc()


#INHERITANCE


#ParentClass
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("Ayush", "Patel")
x.printname()

#ChildClass
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass
x = Student("Ayush", "Patel")
x.printname()

#Super..
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Ayush", "Patel")
x.printname()


#ITERATOR


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a =self.a + 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#StopIterator
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a = self.a + 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)


#POLYMORPHISM


#ClassPolymorphism
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()

#InheritanceClassPolymorphism
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()


#GLOBAL


#Global represents a static value assigned to the variable
#Eg: global x
#    x=300


# MODULE


from mymodule import greeting  
greeting("Ayush")

from KBC import display_question
from KBC import kbc_game
print("Welcome to the KBC Game!")
kbc_game()

from mymodule import mybio
a = mybio
print(a)

from mymodule import add
from mymodule import sub
print(add(1,2))
print(sub(1,2))

# import pandas
# pandas.read_csv()

import math
result=math.sqrt(9)*math.pi
print(result)

print(dir(math))

#if __name__=="__main__" in Module
from mymodule import welcome
a = welcome
print(a)

#RE-NAMING A MODULE
#.
#.
#.


#DATETIME


#%a	Weekday, short version	Wed	
#%A	Weekday, full version	Wednesday	
#%w	Weekday as a number 0-6, 0 is Sunday	3	
#%d	Day of month 01-31	31	
#%b	Month name, short version	Dec	
#%B	Month name, full version	December	
#%m	Month as a number 01-12	12	
#%y	Year, short version, without century	18	
#%Y	Year, full version	2018	
#%H	Hour 00-23	17	
#%I	Hour 00-12	05	
#%p	AM/PM	PM	
#%M	Minute 00-59	41	
#%S	Second 00-59	08	
#%f	Microsecond 000000-999999	548513	
#%z	UTC offset	+0100	
#%Z	Timezone	CST	
#%j	Day number of year 001-366	365	
#%U	Week number of year, Sunday as the first day of week, 00-53	52	
#%W	Week number of year, Monday as the first day of week, 00-53	52	
#%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
#%C	Century	20	
#%x	Local version of date	12/31/18	
#%X	Local version of time	17:41:00	
#%%	A % character	%	
#%G	ISO 8601 year	2018	
#%u	ISO 8601 weekday (1-7)	1	
#%V	ISO 8601 weeknumber (01-53)	01

import datetime
x=datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

import time
t=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
hour=int(input("Enter hour: "))
print(hour)
if(hour>=0 and hour<12):
    print("Good Morning Sir!")
elif(hour>=12 and hour<17):
    print("Good Afternoon Sir!")
elif(hour>=17 and hour<0):
    print("Good Night Sir!")


#MATH


import math
x=math.cbrt(64)
y=math.sqrt(64)
z=pow(4,3)
a=math.ceil(1.8)
b=math.floor(1.8)
c=math.pi
d=min(5,10,25)
e=max(5,10,25)
print(x)
print(y)
print(z)
print(a)
print(b)
print(c)
print(d)
print(e)


#JSON


import json
x='{"name":"Ayush","age":21}'
y=json.loads(x)
y=json.dumps(x)
print(y)

print(json.dumps({"name": "Ayush", "age": 21}))
print(json.dumps(["Ayush", "Clutch"]))
print(json.dumps(("Ayush", "Clutch")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


# REGULAREXPRESSION


#search :It see the string and check whether the word is there or not
#split	:Returns a list where the string has been split at each match
#sub	  :Replaces one or many matches with a string
#[]	A set of characters	"[a-m]"	
#\	Signals a special sequence (can also be used to escape special characters)	"\d"	
#.	Any character (except newline character)	"he..o"	
#^	Starts with	"^hello"	
#$	Ends with	"planet$"	
#*	Zero or more occurrences	"he.*o"	
#+	One or more occurrences	"he.+o"	
#?	Zero or one occurrences	"he.?o"	
#{}	Exactly the specified number of occurrences	"he.{2}o"	
#|	Either or	"falls|stays"


import re
txt="The rain in Spain"
x=re.search("^The.*Spain$",txt)

if x:
    print("YES! We have a match!")
else:
    print("No match!")

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


#PiP


import camelcase
c=camelcase.CamelCase()
txt="Ayush"
print(c.hump(txt))


#EXCEPTION HANDLING


#Single Exception
#Example1
x=10
try:
    print(x)
except:
    print("An exception occured")

#Example2
a=input("Enter the number: ")
print(f"Multiplication table of {a} is:")
try:
 for i in range(1,11):
    print(f"{int(a)}X{i}={int(a)*i}")

except Exception as e:
 print("Invalid Input!")

#ManyException
#Example1
x=10
try:
    print(x)
except NameError:   #If try block raise the error
    print("Variable x is not defined")
except:             #For other errors
    print("Something else went wrong")

#Example2
try:
    num = int(input("Enter an integer: "))
    a=[6,3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("Index Error")        

#Else
try:
    print("Ayush")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")     

#Finally
#The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
    print("Ayush")
except:
    print("Something went wrong")
finally:
    print("The try except is finished")

#Raise Error
x=int(input("Enter the number: "))
if x<0:
    raise Exception("Sorry, no numbers below zero")

x = "Ayush"
if not type(x) is int:
  raise TypeError("Only integers are allowed")


#USERINPUT


#Multiplication Table
a=input("Enter the number: ")
print(f"Multiplication table of {a} is:")

for i in range(1,11):
    print(f"{int(a)}X{i}={int(a)*i}")
    
username=input("Enter username:")
print("Usrename is:"+username)


#STRING FORMATING


qua=3
no=23
price=49
myorder="I want {} pieces of item number {} for {:.2f} dollars"
myorder="I want {0} pieces of item number {1} for {2} dollars"
print(myorder.format(qua,no,price))


#DOCSTRING


def square(a):
#  '''Takes in a number n, returns the square of n'''
  print(a**2)
square(5)
print(square.__doc__)


#ENUMERATE


marks = [12,23,34,56,87,2]

#Before Enumerate
x=0
for mark in marks:
 print(mark)
if(x==3):
    print("Ayush")
    x = x+1

#After Enumerate
for x,mark in enumerate(marks):
 print(mark)
if(x==3):
    print("Ayush")
    x = x+1


#TASK BY NAVEEN


lst1=[[1,2,3,4,5,6]
      [7,8,9,10,11,12]]

lst2=[[13,14,15,16,17,18]
      [19,20,21,22,23,24]]

lst3=[[1,2,13,14,3,4]
      [15,16,5,6,17,18]]

lst4=[[7,8,19,20,9,10]
      [21,22,11,12,23,24]]


#MULTIPLE FILES IN FOLDER


import os

if(not os.path.exists("data")):
 os.mkdir("data")

for i in range(0,100):
    os.mkdir(f"data/Day{i+1}")

#More such commands can be known through os modules in python on google


# ACCESS MODIFIERS
    

class Employees:
   def __init__(self):
#       self.name="Ayush"
      self.__name="Ayush"
a=Employees()
#  print(a.name) #its a public 
#  print(a.__name) #"__" it is used to make the access modifier private
print(a._Employees__name) #it will again make the use of private to public
print(a.__dir__())


#DECORATERS


def greet(fx):
   def mfx(*args,**kwargs):
    print("Good Morning")
    fx(*args,**kwargs)
    print("Thanks for using this funcion")   
    return mfx()

@greet
def hello():
   print("Hello world")

def add(a,b):
  print(a+b)

hello()
greet(add)(1,2)   


#GETTER


class MyClass:
    def __init__(self,value):
        self._value=value

    def show (self):
        print(f"Value is {self._value}")    

    @property
    def ten_value(self):
        return 10*self._value

obj = MyClass(10)
print(obj.ten_value)
obj.show()


# INSTANCE VS CLASS VARIABLE


class Employee:
    companyName="Apple" #ClassVariable
    def __init__(self,name):
        self.name=name
        self.raiseamt=3 #InstanceVariable

    def showdetails(self):
        print(f"The Name of Empolyee is {self.name} from {self.companyName} is raised by {self.raiseamt}")    

emp1=Employee("Ayush")
emp1.showdetails()    


#CLASS METHODS


class Employee:
        company="Apple"
        def show(self):
            print(f"The name is {self.name} and company is {self.company}")

        def changeCompany(cls,newCompany):
                cls.company=newCompany
e1=Employee()
e1.name="Ayush"
e1.show()
e1.changeCompany("Telsa")
e1.show()


#CLASS METHODS AS ALTERNATIVE CONSTRUCTOR


class Employee:
 def __init__(self,name ,salary):
              self.name = name
              self.salary = salary

 @classmethod
 def Str(cls,string):
  return cls(string.split("-")[0],string.split("-")[1])

e1=Employee("Ayush",25000)
print(e1.name)
print(e1.salary)

string="Ayush-65000"
e2=Employee.Str(string)
print(e2.name)
print(e2.salary)


#METHOD OVERRIDING


class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def area(self):
        return self.x*self.y
        
class Circle(Shape):
              def __init__(self, r):
                    self.r=r
                    super().__init__(r,r)
              def area(self):
                    return 3.14*super().area()      
rec=Shape(3,5)
print(rec.area())

cir=Circle(5)
print(cir.area())


#OPERATOR OVERLOADIING


class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self,x):
        return Vector(self.i+x.i,self.j+x.j,self.k+x.k)
    
v1=Vector(3,5,6)
print(v1)

v2=Vector(1,3,5)
print(v2)

print(v1+v2)


#SINGLE INHERITANCE


class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def make_sound(self):
        print("Sound made by the Animal")

class Cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name, species="Cat")
        self.breed=breed
    def make_sound(self):
        print("Meoww")    

c=Cat("Cat","Doremon")
c.make_sound()

a=Animal("Dog","Shiro")
a.make_sound()


#MULTIPLE INHERITANCE


class Employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"The Name is {self.name}")    

class Dancer:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f"The Dance is {self.dance}")

class DancerEmpolyee(Employee,Dancer):
# class DancerEmpolyee(Dancer,Employee):
    def __init__(self,dance,name):
        self.dance=dance
        self.name=name

o=DancerEmpolyee("Kathak","Ayush")
print(o.name)
print(o.dance)
o.show()


#MUTILEVEL INHERITANCE


class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name,species="Dog")
        self.breed=breed

    def show_details(self):
        Animal.show_details(self)

        print(f"Breed: {self.breed}")

class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self,name,breed="Golden Retriever")
        self.color=color

    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")

o=GoldenRetriever("Tommy","Black")
o.show_details()        


# HYBRID INHERITANCE


class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass


# HIERARCHICAL INHERITANCE


class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B):
    pass
# so on....


# WALRUS OPERATOR


# WITHOUT WALRUS
happy=True
print(happy)
print(happy:=False)

foods=list()
while True:
    food=input("What food do you like?:")

    if food=="quit":
        break
    foods.append(food)

# WITH WALRUS
foods=list()
while (food:=input("What food do you like?:"))!="quit":
 foods.append(food)


#GENERATOR
 

def mygenerator():
    for i in range(5):
       yield i

#yield statement returns a value from the generator 
#and suspends the execution of the function until the 
#next value is requested
       
gen = mygenerator()
# print(next(gen))
# print(next(gen))
# print(next(gen))

for j in gen:
    print(j)
