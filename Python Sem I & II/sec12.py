from tkinter import *
root=Tk()
root.title("GYM Registeration Form")
root.geometry("800x800")
root.resizable(False,False)
root.configure(bg="lightpink")
frame=Frame(root, width=800, height=800, bg="lightpink")
frame.place(x = 0, y = 0)

#Header
LabHeader = Label(root, text="IFit GYM Registeration", font=("Arial", 20,"bold"),
           anchor = "center", bg="lightpink")
LabHeader.place(x=250,y=10)

#Main Area
LabName = Label(root, text="Name:", font=("Georgia", 16),
           anchor = "center", bg="lightpink", fg="darkred")
LabName.place(x=5,y=50)

EntName = Entry(root,bd=4,relief=RAISED,width=40)
EntName.place(x=95,y=50)

LabAdd = Label(root, text="Address:", font=("Georgia", 16),
           anchor = "center", bg="lightpink", fg="darkred")
LabAdd.place(x=5,y=85)

EntAdd = Entry(root,bd=4,relief=RAISED,width=40)
EntAdd.place(x=95,y=85)

LabGen = Label(root, text="Gender:", font=("Georgia", 16),
           anchor = "center", bg="lightpink", fg="darkred")
LabGen.place(x=5,y=120)

RadGen1=Radiobutton(root,text="Male",value=0, font=("Bookman Old Style",12))
RadGen1.place(x=95, y=120)
RadGen2=Radiobutton(root,text="Female",value=1, font=("Bookman Old Style",12))
RadGen2.place(x=175, y=120)

LabDob = Label(root, text="Dob:", font=("Georgia", 16),
           anchor = "center", bg="lightpink", fg="darkred")
LabDob.place(x=5,y=155)

SpinDay = Spinbox(root, from_=1, to=31, width=4)
SpinDay.place(x=95, y=162)

SpinMonth = Spinbox(root, from_=1, to=12, width=4)
SpinMonth.place(x=145, y=162)

SpinYear = Spinbox(root, from_=1960, to=2025, width=6)
SpinYear.place(x=195, y=162)

LabFac = Label(root, text="Facilities Available:", font=("Georgia", 16,"italic"),
           anchor = "center", bg="lightpink", fg="darkred")
LabFac.place(x=5,y=190)

LisFac=Listbox(root,height=6,width=30, font=("Bookman Old Style",10,))
LisFac.insert(0,"Cardio Equipment")
LisFac.insert(1,"Strength Training Equipment")
LisFac.insert(2,"Nutrition & Diet Consultation")
LisFac.insert(3,"Personal Training")
LisFac.insert(4,"Yoga & Stretching Zone")
LisFac.insert(5,"Shower & Steam Facility")
LisFac.insert(6,"Locker & Changing Room")
LisFac.place(x=5,y=215)

LabFac = Label(root, text="Health/Medical Conditions:", font=("Georgia", 14,),
           anchor = "center", bg="lightpink", fg="darkred")
LabFac.place(x=5,y=340)

CheDia=Checkbutton(root,text="Diabetes", font=("Arial",10))
CheDia.place(x=250,y=343)

CheAst=Checkbutton(root,text="Asthma", font=("Arial",10))
CheAst.place(x=340,y=343)

CheHeart=Checkbutton(root,text="Heart Condition", font=("Arial",10))
CheHeart.place(x=425,y=343)

CheJoint=Checkbutton(root,text="Joint Pain", font=("Arial",10))
CheJoint.place(x=555,y=343)

CheNone=Checkbutton(root,text="None", font=("Arial",10))
CheNone.place(x=650,y=343)

LabTime = Label(root, text="Training Time:", font=("Georgia", 14,),
              anchor = "center", bg="lightpink", fg="darkred")
LabTime.place(x=5,y=378)

DropString1 = StringVar()
DropString1.set("Select Preferred Training Time")
times = [
    "Morning (5:00 AM – 9:00 AM)",
    "Late Morning (9:00 AM – 12:00 PM)",
    "Afternoon (12:00 PM – 4:00 PM)",
    "Evening (4:00 PM – 8:00 PM)",
    "Night (8:00 PM – 11:00 PM)",
    ]

DropTime = OptionMenu(root,DropString1 ,*times)
DropTime.config(font=("Bookman Old Style",14,),bg="white",fg="darkred")
DropTime.place(x=145,y=378)

LabTime = Label(root, text="Training Level:", font=("Georgia", 14,),
              anchor = "center", bg="lightpink", fg="darkred")
LabTime.place(x=5,y=425)

DropString2 = StringVar()
DropString2.set("Select Training Level")
train = [
    "Beginner",
    "Intermediate",
    "Advanced",
    ]

DropTrain = OptionMenu(root,DropString2 ,*train)
DropTrain.config(font=("Bookman Old Style",14,),bg="white",fg="darkred")
DropTrain.place(x=145,y=425)

CheTC=Checkbutton(root,text="I have read and agreed to iFit's Terms and Conditions", font=("Bookman Old Style",14),bg="lightpink")
CheTC.place(x=5,y=480)

SubButton=Button(frame, text='Register', bg='white', font=('arial',18),width=15,fg="darkred",bd=5,relief=RAISED)
SubButton.place(x=275,y=600)
root.mainloop()