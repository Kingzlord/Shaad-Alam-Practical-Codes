##FONTS AND COLOURS
import tkinter as tk

#create the main window
root = tk.Tk()
root.title("Fonts and colour variations")
root.geometry("400x400")

#create a label with different font and styles and colors
#Arial
label1 = tk.Label(root, text="Arial Bold 20", font=("Arial", 20, "bold" ),
                  fg="blue", bg="cyan")
label1.pack(pady=10)

#Helvetica
label2 = tk.Label(root, text="Bookman Old Style 18",  font=("Bookman Old Style", 18),
                 fg="teal", bg="lightblue")
label2.pack(pady=15)

#Times New Roman    
label3 = tk.Label(root, text="Times New Roman 16",  font=("Times New Roman", 16, ),
                 fg="red", bg="lightgray")
label3.pack(pady=15)

#Courier New
label4 = tk.Label(root, text="Courier New 20",  font=("Courier New", 20 ),
                 fg="purple", bg="yellow")
label4.pack(pady=15)

#Cosmic Sans
label5 = tk.Label(root, text="Cosmic Sans MS 22",  font=("Cosmic Sans MS", 22, ),
                 fg="orange", bg="red")
label5.pack(pady=15)

#Georgia
label6 = tk.Label(root, text="Georgia Bold 24",  font=("Georgia", 24, "bold"),
                 fg="brown", bg="beige")
label6.pack(pady=15)

tk.mainloop()