
a=open("myfile.txt","w") #to create or open a file
a.write("This is my first line to be written in the new file.\n") #to write in a file
a.close() #closing a file .once a file is open it must be closed


a=open("myfile.txt","r") # read command after writing in a file
temp=a.read() # storing in variable temp
print(temp)


a=open("myfile.txt","a") #append function to add more text in the end of first line
a.write("My name is Ali and I am learning file handling. ") # appending data
a.write("\nThis is my third line") # adding second line
a.close()


#reading the file after append
a=open("myfile.txt","r")
temp1=a.read()
print(temp1) # reads first 10 characters in the line
#temp1=a.readline() # reads only one line
temp1=a.readlines() #it treats the lines as list,reads all lines in the file
print(temp1)


a=open("myfile.txt","a") #open the file in append mode
a=open("myfile.txt","r") #open the file in read mode
a=open("myfile.txt","w") #open the file in write mode
a.close()
print("The mode is:",a.mode) # gives the mode of the file
print("The name of the file is:",a.name) # gives the name of the file
print("The file is closed:",a.closed) # checks if the file is closed or not

from os import path
import time
file_path=r"D:\My folder\Study\Python\myfile.txt"
print(path.exists(file_path))
print(path.isfile(file_path)) # use to check whether the specified path is an existing file or not
print(file_path)

print(path.getsize(file_path)) # use to check the size of the specified path
accesstime=(path.getatime(file_path))
print(accesstime)
localtime=time.ctime(accesstime)
print(localtime)
