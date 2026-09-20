from tkinter import *
root=Tk()
root.title("GYM Registeration Form")
root.geometry("800x800")
root.resizable(False,False)
root.configure(bg="lightgrey")

l1 = Label(root, text="First Name:", font=("Arial", 12))
l1.grid(row=0, column=0)

e1 = Entry(root, bd=5,relief=RAISED)
e1.grid(row=0, column=1)

l2 = Label(root, text="Address:", font=("Arial", 12))
l2.grid(row=1, column=0)

e2 = Entry(root, bd=5,relief=RAISED)
e2.grid(row=1, column=1)

l3 = Label(root, text="Gender:", font=("Arial", 12))
l3.grid(row=2, column=0)

r=Radiobutton(root,text="Male",value=0, font=("Arial",14))
r.grid(row=2, column=1)
r1=Radiobutton(root,text="Female",value=1, font=("Arial",14))
r1.grid(row=2, column=2)

l4 = Label(root, text="Select Subjects:", font=("Arial", 12))
l4.grid(row=3, column=0)

c1=Checkbutton(root,text="Major I", font=("Arial",14))
c1.grid(row=3,column=1)

c2=Checkbutton(root,text="Major II", font=("Arial",14))
c2.grid(row=3,column=2)

c3=Checkbutton(root,text="SEC", font=("Arial",14))
c3.grid(row=3,column=3)

c4=Checkbutton(root,text="VSC", font=("Arial",14))
c4.grid(row=3,column=4)

l5 = Label(root, text="List:", font=("Arial", 12))
l5.grid(row=4, column=0)

list1=Listbox(root,height=3, font=("Arial",12))
list1.insert(0,"FYCS")
list1.insert(1,"SYCS")
list1.insert(2,"TYCS")
list1.grid(row=4,column=1)

l6 = Label(root, text="Day of the month:", font=("Arial", 12))
l6.grid(row=5, column=0)

s1=Spinbox(root,from_= 1, to = 30)
s1.grid(row=5,column=1)

l1 = Label(root, text="IFit GYM Registeration", font=("Arial", 20,"bold"),
           anchor = "center", bg="lightgrey")
l1.place(x=250,y=0)
root.mainloop()
