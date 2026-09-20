import tkinter as tk

##Window
root = tk.Tk()
root.title("Drawing Shapes")
root.geometry("1000x800")

##Canvas(root, width, heigth, bg color)
canvas = tk.Canvas(root,width=1000,height=800,bg="black")
canvas.pack()

'''Creating shapes'''
##Oval(x1,y1,x2,y2, outline, fill, width)
canvas.create_oval(50, 50, 150, 100, outline = "darkgray", fill = "lightgray",width=2)

##Line(x1,y1,x2,y2,..... , fill, width)
canvas.create_line(0, 400,300,400, fill = "green",width=3)

##Circle by using oval (x1,y1,x1+r,y1+r, outline, fill, width)
canvas.create_oval(500, 350, 600, 450, outline = "White", fill = "cyan",width=2)

##Square by using rectanle(x1,y1,x2,y2, outline, fill, width)
canvas.create_rectangle(60,180,120,240,outline="Blue",fill="purple",width=1)

##Triangle using polygon(x1,y1,x2,y2,x3,y3, outline, fill, width)
canvas.create_polygon(200,200,250,150,300,200,outline="orange", fill="gray",width=6)

##Polygon(x1,y1,x2,y2.....,outline,fill,width)
canvas.create_polygon(400,150,450,130,500,150,500,200,450,220,400,200,
                      outline="brown", fill = "lightgreen",width=3)

canvas.create_oval(550,50,650,150, outline="blue",fill="white",width=2)
canvas.create_rectangle(600, 250, 800,350, outline="red",fill="yellow",width=2)
canvas.create_polygon(700,400,450,500,600,650,700,750,outline="orange",fill="red",width=6)
tk.mainloop()
