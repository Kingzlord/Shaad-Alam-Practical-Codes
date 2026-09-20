#practical 16
#12-02-26
#pip install mysql-connector-python
#wap to work with database in python to A) create and connect to database b) creating and dropping tables
'''
import mysql.connector
connection=mysql.connector.connect(
    host="localhost",
    user="root",  #change if needed
    password="root", #change if needed
    charset="utf8")
cursor=connection.cursor()
print("Connected to MySQL server")
cursor.execute("CREATE DATABASE IF NOT EXISTS FYCS23")
print("Database 'FYCS23' created")
connection.database="FYCS23"
create_table="""
CREATE TABLE IF NOT EXISTS students (
   id INT PRIMARY KEY AUTO_INCREMENT,
   name VARCHAR(50),
   age INT,
       course VARCHAR(50))
   """
cursor.execute(create_table)
print("Table 'students' created")
#drop_table="DROP TABLE IF NOT EXISTS students"
#cursor.execute(drop_table)
#print("Table 'students' dropped")
connection.commit()
cursor.close()
connection.close()
print("MySQL connection closed")
'''

import mysql.connector
from mysql.connector import Error
# Connect and create database
def connect_db():
    try:
        con=mysql.connector.connect(
            host="localhost",
            user="root",
            password="root")
        cur=con.cursor()
        cur.execute("CREATE DATABASE IF NOT EXISTS example_db")
        con.database="example_db"
        print("Database connected")
        return con
    except Error as e:
        print("Connection error:",e)

#Create table
def create_table(con):
    cur=con.cursor()
    cur.execute("""
       CREATE TABLE IF NOT EXISTS students(id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(50),
       age INT,
       grade VARCHAR(5)
       )
       """)
    con.commit()
    print("Table created")
#Insert record
def insert_student(con,name,age,grade):
    cur=con.cursor()
    cur.execute(
        "INSERT INTO students(name,age,grade)VALUES(%s,%s,%s)",
        (name,age,grade)
        )
    con.commit()
    print("Student inserted")
    #Updated record
def update_grade(con,sid,new_grade):
    cur=con.cursor()
    cur.execute(
        "UPDATE students SET grade=%s WHERE id=%s",
        (new_grade,sid)
        )
    con.commit()
    print("Grade updated")
    #main
def main():
    con=connect_db()
    if con:
        create_table(con)
        insert_student(con,"Alice",20,"A")
        insert_student(con,"Bob",22,"B")
        insert_student(con,"Hello",29,"B")
        update_grade(con,1,"A+")
        con.close()
        print("Connection closed")
main()

