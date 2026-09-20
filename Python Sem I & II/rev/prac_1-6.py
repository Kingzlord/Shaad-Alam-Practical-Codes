#PRAC 2
#Single level inheritence
'''

class Animal:
    def eat(self):
        print("All animals eat")
    
class Dog(Animal):
    def bark(self):
        print("All dogs barks!!!")

dg = Dog()
dg.bark()
dg.eat()
'''

#Multi-level
'''
class GP:
    def gp(self):
        print("I am grandparent class")

class Pt(GP):
    def pt(self):
        print("I am parent class")

class Child(Pt):
    def cd(self):
        print("I am child class... save me from donal trump")

cd = Child()
cd.gp()
cd.pt()
cd.cd()
'''

#Multiple
'''
class fycs:
    def fp(self):
        print("Some students are in FYCS")

class sycs:
    def sp(self):
        print("Some students are in sycs")

class tycs:
    def tp(self):
        print("Some students are in tycs")

class csdp(fycs,sycs,tycs):
    def cp(self):
        print("All students are in CS DEPT")

cs = csdp()
cs.fp()
cs.sp()
cs.tp()
cs.cp()
'''

#Hierarchical 
'''
class vehicle:
    def vp(s):
        print("There are differnt types of vehicles based on wheels")

class twwhl(vehicle):
    def tp(s):
        print("Some vehicles have two wheels")

class thwl(vehicle):
    def thp(s):
        print("Some have threee wheels")

class fwhl(vehicle):
    def fp(s):
        print("And lastly some have four wheels")

tw = twwhl()
th = thwl()
fw = fwhl()

tw.vp()
tw.tp()
th.vp()
th.thp()
fw.vp()
fw.fp()
'''
# PRAC 3
# Operator Overloading
'''
a = 23
b = 11
c = 9.5
s1 = "hello"
s2 = "world"
print("Addition of two Integers: ",a+b)
print("Data type of addition:",type(a+b))
print("Addition of integer and float:",b+c)
print("Data type of addition:",type(b+c))
print("Concatenation of two strings: ",s1+s2)
print("Data type of concatenation ",type(s1+s2))
'''

# Method Overloading
'''
def overload(x=None,y=None,z=None):
    if x==None and y==None and z==None:
        print("No opertaion performed")
    elif x!=None and y==None and z==None:
        print("Only one var given",x)
    elif x!=None and y!=None and z==None:
        print("Addition of two given no.:",x+y)
    elif x!=None and y!=None and z!=None:
        print("Addition of all given nos.:",x+y+z)
    else:  
        print("Invalid")

overload()
overload(2)
overload(2,3)
overload(2,3,4)
overload('2','s','y')
'''

# Method Overriding
'''
class parent:
    def display(s):
        print("I am parent")

class child(parent):
    def display(s):
        print("I am child i override parent!")

cd = child()
cd.display()
'''

# Prac 4
# parameterized
'''
class Person:
    def __init__(self,name,age):
        self.name =  name
        self.age = age

p = Person("Shaad",31)
print("Name:",p.name)
print("Age:",p.age)
'''

# Default
'''
class Car:
    def __init__(self):
        self.comp = "BMBabblu"
        self.model = "Babble"
        self.ver = "69"

c = Car()
print(c.comp,c.model,c.ver)
'''

# Non-parameterized
'''
class Fruits:
    fav = "apple"
    def __init__(self):
        self.fav = "orange"

    def show(self):
        print(self.fav)

f = Fruits()
f.show()
print(f.fav)
print(Fruits.fav)
'''

# Prac 5
'''
from abc import ABC

class Car(ABC):
    def mileage(self):
        print("Gand maara")

class Tesla(Car):
    def mileage(self):
        print("Tesla has -500 mielage")

class Sizuka(Car):
    def mileage(self):
        print("Sizuka has doraemon mileage")

class BmBablu(Car):
    def mileage(self):
        print("Bmbalu has infinite mileage")

t=Tesla()
t.mileage()
s = Sizuka()
s.mileage()
b = BmBablu()
b.mileage()
'''

# Example 2
'''
from abc import ABC
class Shape(ABC):
    def area(self):
        pass
    def peri(self):
        pass

class Rect(Shape):
    def sides(self,l,b):
        self.length = l
        self.breadth = b
    
    def area(self):
        return self.length*self.breadth
    
    def peri(self):
        return (2*(self.length+self.breadth))
    
class Square (Shape):
    def sides(self,s):
        self.side = s

    def area(self):
        return self.side**2
    
    def peri(self):
        return 4*self.side
    
s = Square()
r = Rect()
r.sides(4,5)
s.sides(4)
print(r.area())
print(r.peri())
print(s.area())
print(s.area())
'''

# prac 6
'''
class emp:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        print("Employee created")

    def __del__(self):
        print("Employee",self.name, "has been killed!!")

e = emp("ali",44)
print("Name: ",e.name,"\nId:",e.id)
del e
'''




