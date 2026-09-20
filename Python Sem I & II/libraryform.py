from tkinter import *
from PIL import Image, ImageTk

#Root
root = Tk()
root.title("GUI widgets")
root.state("zoomed")
root.configure(bg="white")
root.resizable(False, False)

#Logo
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(root.winfo_screenwidth())
print(root.winfo_screenheight())

canvas = Canvas(root, width=width, height=height, bg="white", highlightthickness=0)
canvas.pack(fill="both", expand=True)

img = Image.open("Images/logo_++-removebg-preview.png")
img = img.resize((200,200))

photo = ImageTk.PhotoImage(img)

#Image placement (Even image is getting placement but not you)
lImg = Label(root, image = photo, bg="white")
lImg.image = photo
lImg.place(x=300,y=-30)

##Canvas

# left-right border
canvas.create_rectangle(0,0,100,1000,fill="green",outline="green")
canvas.create_rectangle(1555,0,1420,1000,fill="green",outline="green")

#Form card
canvas.create_rectangle(420,180,1125,800,fill="lightgray")


# Header
Header = Label(root, text=("Royal College Library "),
               font=("Bookman Old Style",45,),bg="white",fg="black") #Label(root,text,font)
Header.place(x=450,y=21)

SubHeader = Label(root,text="Library Membership",
                  font=("Bookman Old Style",35,),bg="white",fg="black")
SubHeader.place(x=525,y=100)


## Personal Details
Id = Label(root, text=("Student's ID no.: "),font=("Bookman Old Style",14,),
           bg="lightgrey",fg="black")
Id.place(x=550,y=200)

IdEntry = Entry(root,border=2 ,relief="solid",font=("Arial",14,),bg="lightgrey",fg="black") #Entry(root, border[bd],relief means style,font)
IdEntry.place(x=765,y=200)

Name = Label(root, text=("Student's Full name.:"),font=("Bookman Old Style",14,),
           bg="lightgrey",fg="black")
Name.place(x=550,y=250)
Nametemp = Label(root,text="(as per ID card)",font=("Bookman Old Style",12,),
           bg="lightgrey",fg="black")
Nametemp.place(x=550,y=275)
NameEntry = Entry(root,border=2 ,relief="solid",font=("Arial",14,),bg="lightgrey",fg="black") #Entry(root, border[bd],relief means style,font)
NameEntry.place(x=765,y=250)

#Department
deptString = StringVar()
deptString.set("Select Department")
depts = [
    "Computer Science",
    "IT",
    "BMS & BAF",
    "ETC...",
    ]

Dept = Label(root, text=("Department:"),font=("Bookman Old Style",14,),
           bg="lightgrey",fg="black")
Dept.place(x=550,y=325)
DeptDrop = OptionMenu(root,deptString ,*depts)
DeptDrop.config(font=("Bookman Old Style",14,),bg="lightgrey",fg="white")
DeptDrop.place(x=765,y=325)

#Course
Course = Label(root,text="Year of Study:",font=("Bookman Old Style",14,),bg="lightgrey",fg="black")
Course.place(x=550,y=412)

CourseRadio1 = Radiobutton(root,text="First Year",value=1,font=("Bookman Old Style",14,),bg="lightgrey",fg="black")
CourseRadio2 = Radiobutton(root,text="Second Year",value=2,font=("Bookman Old Style",14,),bg="lightgrey",fg="black")
CourseRadio3 = Radiobutton(root,text="Third Year",value=3,font=("Bookman Old Style",14,),bg="lightgrey",fg="black")
CourseRadio1.place(x=765,y=375)
CourseRadio2.place(x=765,y=412)
CourseRadio3.place(x=765,y=449)

#Contact and email
Contact = Label(root,text="Contact Number:",font=("Bookman Old Style",14,),bg="lightgrey",fg="black")
Contact.place(x=550,y=499)
ContactEntry = Entry(root,border=2 ,relief="solid",font=("Arial",14,),bg="lightgrey",fg="black")
ContactEntry.place(x=765,y=499)

Email = Label(root,text="Email ID:",font=("Bookman Old Style",14,),bg="lightgrey",fg="black")
Email.place(x=550,y=549)
EmailEntry = Entry(root,border=2 ,relief="solid",font=("Arial",14,),bg="lightgrey",fg="black")
EmailEntry.place(x=765,y=549)

# Membership
Membership = Label(root,text="Membership Plan:",font=("Bookman Old Style",14,),bg="lightgrey",fg="black") 
Membership.place(x=550,y=608)

MembershipEntry = Listbox(root,height=2,font=("Bookman Old Style",14,),bg="white",fg="black",width=17)
MembershipEntry.insert(0,"Basic (6 months)")
MembershipEntry.insert(1,"Standard (12 months)")
MembershipEntry.place(x=765,y=599)

# Message 

Msg1 = Checkbutton(root, text=("I would like to receive weekly library updates and notifications"),
            font=("Bookman Old Style",10,),bg="lightgrey")  
Msg1.place(x=550,y=679)
Msg2 = Checkbutton(root, text=("I have read and agree to the library rules and regulations"),
            font=("Bookman Old Style",10,),bg="lightgrey")  
Msg2.place(x=550,y=699)


# star = Label(root,text="*",font=("Bookman Old Style",5,"bold"),bg="lightgrey",fg="red")
# star.place(x=569,y=698.1)



#Submit button
sub = Button(root,text="Proceed To Payment",font=("Bookman Old Style",14,),bg="lightgrey")
sub.place(x=675,y=749)


root.mainloop()