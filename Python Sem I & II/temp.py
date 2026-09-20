from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Image")
root.geometry("700x600") 
root.configure(bg="white")

img = Image.open("Images/logo_++-removebg-preview.png")
img.resize((200,200))

photo = ImageTk.PhotoImage(img)

limg = Label(root,image=photo,bg="white")
limg.image = photo
limg.place(x=0,y=0)

root.mainloop()