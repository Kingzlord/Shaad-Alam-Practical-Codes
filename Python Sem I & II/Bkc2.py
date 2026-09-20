import tkinter as tk

root = tk.Tk()
root.title("Drawing Shapes")
root.geometry("1000x800")

canvas = tk.Canvas(root, width=1000, height=800, bg="black")
canvas.pack()

# Left circle
canvas.create_oval(60, 120, 140, 200, outline="darkgray", fill="lightgray", width=2) #[left, right, top, bottom]

# Right circle
canvas.create_oval(160, 120, 240, 200, outline="darkgray", fill="lightgray", width=2)

# Center stick
canvas.create_oval(140, 20, 160, 10, outline="darkgray", fill="lightgray", width=2)


# Top circle (cap / head)
# canvas.create_oval(125, 0,175, 80, outline="darkgray", fill="lightgray", width=2)

# Base
# canvas.create_line(80, 200, 220, 200, fill="white", width=6)

tk.mainloop()
