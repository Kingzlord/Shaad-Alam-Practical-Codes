import math as m
'''
print(m.ceil(5.25))
print(m.cos(0))
print(m.degrees(3.142))
x = (4,5)
y = (4,5.5)
print(m.dist(x,y))
print(m.exp(0))
print(m.fabs(-91))
print(m.factorial(5))
print(m.floor(2.5))
print(m.fmod(5,2))
print(m.gcd(4,8,16))
print(m.isclose(0,0))
x = float("nan")
print(m.isfinite(x))
print(m.isnan(x))
print(m.log(1))
print(m.radians(180))
print(m.pow(5,2))
print(m.sin(m.radians(90)))
print(m.sqrt(25))
print(m.tan(m.radians(90)))
print(m.tanh(m.radians(90)))
'''

import random as r
'''
# r.seed(10)
# state = r.getstate()

# print(r.random())
# r.setstate(state)
# print(r.random())

# print(r.getstate())
print(r.choice([4,5,6,7]))
print(r.choices([4,5,6,71,45],k=3))
print(r.randrange(20,50,2))
print(r.randint(5,89))
print(r.random())
li = [4,5,6,71,45]
r.shuffle(li)
print(li)
print(r.sample(li,k=3))
'''

import datetime as dt
# print(dt.datetime.now().strftime("%a"))
# print(dt.datetime.now().strftime("%A"))
# print(dt.datetime.now().strftime("%w"))
# print(dt.datetime.now().strftime("%W"))
# print(dt.datetime.now().strftime("%d"))
# print(dt.datetime.now().strftime("%D"))
# print(dt.datetime.now().strftime("%b"))
# print(dt.datetime.now().strftime("%B"))
# print(dt.datetime.now().strftime("%x"))
# print(dt.datetime.now().strftime("%X"))
# print(dt.datetime.now().strftime("%m"))
# print(dt.datetime.now().strftime("%y"))
# print(dt.datetime.now().strftime("%Y"))
# print(dt.datetime.now().strftime("%p"))
# print(dt.datetime.now().strftime("%z")) #timezone
# print(dt.datetime.now().strftime("%c"))
# print(dt.datetime.now().strftime("%C"))
# print(dt.datetime.now().strftime("%u"))

import calendar as cal
# print(cal.month(2026,3))
# print(cal.calendar(2016))

import re
s1 = "hello how are you mfs 2026 !@#$%^&*()"
# print(re.split(r"\s",s1))
# print(re.split(r"[a-d]",s1))
# print(re.findall(r"\d",s1)) #decimals
# print(re.findall(r"\D",s1)) # no decimals
# print(re.findall(r"\s",s1)) #spaces
# print(re.findall(r"\S",s1)) #no spaces
# print(re.findall(r"\w",s1)) # letters and numerics
# print(re.findall(r"\W",s1)) # nein letters and numerics
# print(re.findall(r"\bm",s1))
# print(re.sub(r"\s","fuck",s1))
# print(re.search(r"a",s1))
# print(re.findall(r"hello",s1))

# Prac 9
'''
file = open("file.txt","w+")
file.write("hello how are you\nNice\nhere is another line")
print(file.mode)

file.close()
file = open("file.txt","r")
print(file.read()) 
print(file.mode)
print("Is file closed?:",file.closed)
file.close()
print("Is file closed?:",file.closed)
from os import path
import time
path_file = r"D:\My folder\Study\Python\rev\file.txt"
print(path.exists(path_file))
print(path.isfile(path_file))
print(path.getsize(path_file))
accesstime = path.getatime(path_file)
print(accesstime)
localtime = time.ctime(accesstime)
print(localtime)
# print(path.)
'''

# Prac 10
# Tkinter
# import tkinter as tk
'''
root = tk.Tk()
root.title("Shapes")
root.geometry("1000x800")

canvas = tk.Canvas(root,width=1000,height=800,bg="white")
canvas.pack()

# cirlce
canvas.create_oval(50,50,150,150,outline="darkgray",fill="pink")
# line
canvas.create_line(50,250,300,250,fill="black",width=3)
# oval
canvas.create_oval(200,50,350,150,outline="grey",fill="red",width=1)
# rectanlge
canvas.create_rectangle(200,450,550,600,fill="blue",outline="black",width="5")
# square
canvas.create_rectangle(500,300,600,200,fill="green",outline="brown",width=6)
# trianlge
canvas.create_polygon(600,199,550,150,500,199,outline="gray",fill="beige")
# polygon             x1,y1, x2,y2,  x3,y3,x4,y4,  x5,y5
canvas.create_polygon(450,150,500,150,530,200,500,250,420,200,outline="black",width=2)
canvas.create_polygon(
    200, 100, #hello
    300, 180,
    260, 300,
    140, 300,
    100, 180,
    fill="skyblue"
)
tk.mainloop()
'''

# Prac 11
# diff Fonts
'''
root = tk.Tk()
root.title("Fonts")
root.geometry("500x500") 

label1 = tk.Label(root,text="Arial Bold 20", font=(
        "Arial",
        20,
        "bold"
    ),
    fg="black", bg="cyan"
)
label1.pack(pady=10)
root.mainloop()
'''

# Prac 12
# creating a Form
'''

from tkinter import *
root = Tk()
root.title("this is a form")
root.geometry("1000x800")
root.resizable(False,False)
root.config(bg="white")

frame = Frame(root,width=1000,height=800,background="darkgray")
frame.pack()

hd = Label(root,text="Form ",font=(
        "Arial",
        30,
        "bold", 
        "underline"       
    ),
    fg="white",
    bg="darkgray"
)
hd.place(x=450,y=10)

lb1 = Label(root,text="Name: ",font=(
        "Arial",
        15,
        "bold",        
    ),
    fg="white",
    bg="darkgray"
)
lb1.place(x=50,y=55)

e = Entry(root,bd=4,relief="raised",width=40)
e.place(x=130,y=58)

rd1 = Radiobutton(root,text="Click here",value=0,font=(
        "Bookman Old Style",
        15
    ),
    bg="darkgray")
rd1.place(x=50,y=120)

rd2 = Radiobutton(root,text="Click me",value=1,font=(
        "Bookman Old Style",
        15
    ),
    bg="darkgray")
rd2.place(x=500,y=120)

rd3 = Radiobutton(root,text="Click  meee~~h!",value=2,font=(
        "Bookman Old Style",
        15
    ),
    bg="darkgray")
rd3.place(x=250,y=160)

sp = Spinbox(root,from_=0,to=255,width=20)
sp.place(x=55,y=250)

ls = Listbox(root,height=3,width=30,font=(
        "Bookman Old Style",
        15,
        "bold"
    )
)
ls.insert(0,"Ahh")
ls.insert(1,"ooh")
ls.insert(2,"oui maa")
ls.insert(3,"noooo~~~")
ls.place(x=55,y=300)

ch = Checkbutton(root,text="Want some dildo?",font=(
    "Bookman Old Style",
    15,
    "bold"
    ),
    fg="lightpink",
    bg="pink"
)
ch.place(x=55,y=450)

string = StringVar()
string.set("Hello we are here")
hello = [
    "Noob",
    "Pro",
    "Hacker",
    "Modi hai mumkin"
]

dp = OptionMenu(root,string,*hello)
dp.config(font=("Bookman Old Style",20,"bold"),bg="darkgray",
          fg="white")
dp.place(x=55, y=600)

bt = Button(root,text="Spank me 👋",bg="black",fg="white",font=(
    "Arial",
    20,
    "bold"    
))
bt.place(x=450,y=700)
root.mainloop()
'''

# Prac 14
# Client code
'''
import socket
c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "127.0.0.1"
port = 65499
c.connect((host,port))
c.send(b"I am doing some shits")
tm = c.recv(1024).decode()
print(f"MSG from server: {tm}")
c.close()
print("Server is raped and died")
'''
# Server
'''
import socket
sct = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "0.0.0.0"
port = 65499
sct.bind((host,port))
sct.listen(5)
print("Server started!!")
while True:
    clientsocket,address = sct.accept()
    print(f"Connect is made: {address}")
    data = clientsocket.recv(1024).decode()
    print(f"MSG recieved: {data}")
    clientsocket.send(b"Kya kr raha hai bhadwe")
    clientsocket.close()
    print("Server is shutting 😭")
'''

# Prac 16
'''
import mysql.connector as mysql
con = mysql.connect(
    host = "localhost",
    user = "root",
    password = "root"
)
cur=con.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS college_ex;")
con.database="college_ex"
print("database connected")


# create table
# table = '''
# CREATE TABLE IF NOT EXISTS students(
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         name VARCHAR(50),
#         age INT,
#         grade VARCHAR(5)        )
'''
cur.execute(table)
print("Table is created")

name = "Taabish"
age=19
grade="TYCS"

insert = "INSERT INTO STUDENTS(name,age,grade) VALUES(%s,%s,%s)"
cur.execute(insert,(name,age,grade))
con.commit()
print("Values inserted!!")

update = "UPDATE students SET grade=%s WHERE id=%s"
cur.execute(update,("TYCS",1))
con.commit()
print("Database Updated!!")

drop = "DROP TABLE IF EXISTS students;"

cur.execute(drop)
print("Students are killed")
con.close()
print("Connection close")
'''


