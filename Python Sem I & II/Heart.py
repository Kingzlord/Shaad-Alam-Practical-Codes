import tkinter as tk
import random
import math
import winsound

# ---------------- WINDOW ---------------- #
root = tk.Tk()
root.title("Valentine Proposal 💘")
root.attributes("-fullscreen", True)
root.configure(bg="black")

WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT,
                   bg="black", highlightthickness=0)
canvas.pack()

# ---------------- GRADIENT BACKGROUND ---------------- #
for i in range(0, HEIGHT, 2):
    color = "#%02x%02x%02x" % (20 + i//25, 0, 40 + i//20)
    canvas.create_line(0, i, WIDTH, i, fill=color)

# ---------------- NAME INPUT ---------------- #
name_var = tk.StringVar()

tk.Label(
    root,
    text="Enter Your Name 💌",
    font=("Comic Sans MS", 22, "bold"),
    bg="black",
    fg="white"
).place(relx=0.5, rely=0.15, anchor="center")

tk.Entry(
    root,
    textvariable=name_var,
    font=("Arial", 18),
    justify="center"
).place(relx=0.5, rely=0.22, anchor="center")

# ---------------- HEART ---------------- #
heart_size = 120
beat_dir = 1


def draw_heart(size):
    canvas.delete("heart")

    cx = WIDTH // 2
    cy = HEIGHT // 2 - 50

    pts = []

    for i in range(360):
        t = math.radians(i)
        x = 16 * math.sin(t) ** 3
        y = (13 * math.cos(t)
             - 5 * math.cos(2 * t)
             - 2 * math.cos(3 * t)
             - math.cos(4 * t))

        pts.append((cx + x * size/20,
                    cy - y * size/20))

    canvas.create_polygon(
        pts,
        fill="#ff1744",
        outline="#ff80ab",
        width=3,
        tags="heart"
    )


def animate_heart():
    global heart_size, beat_dir

    heart_size += beat_dir * 2
    if heart_size > 140 or heart_size < 110:
        beat_dir *= -1

    draw_heart(heart_size)
    root.after(70, animate_heart)


animate_heart()

# ---------------- YES ---------------- #
def say_yes():
    name = name_var.get().strip() or "My Love"

    winsound.Beep(800, 200)
    winsound.Beep(1000, 200)

    reply = tk.Toplevel(root)
    reply.attributes("-fullscreen", True)
    reply.configure(bg="#1a001a")

    tk.Label(
        reply,
        text=f"Now you're mine forever, {name} 😈💖",
        font=("Comic Sans MS", 36, "bold"),
        bg="#1a001a",
        fg="#ff66cc"
    ).pack(expand=True)


# ---------------- BUTTONS ---------------- #
tk.Label(
    root,
    text="Will You Be My Valentine? 💘",
    font=("Comic Sans MS", 40, "bold"),
    bg="black",
    fg="#ff4d88"
).place(relx=0.5, rely=0.35, anchor="center")

yes_btn = tk.Button(
    root, text="YES 💖",
    font=("Arial", 20, "bold"),
    bg="#ff1744", fg="white",
    width=12, height=2,
    command=say_yes
)
yes_btn.place(x=400, y=550, anchor="center")

# Start NO button at fixed safe position
no_btn = tk.Button(
    root, text="NO 🙈",
    font=("Arial", 20, "bold"),
    bg="#444", fg="white",
    width=12, height=2
)
no_btn.place(x=600, y=650)

# ---------------- ESCAPE PHYSICS ---------------- #
vx, vy = 0, 0


def move_no_button():
    global vx, vy

    # Ensure widget sizes are ready
    root.update_idletasks()

    mouse_x = root.winfo_pointerx() - root.winfo_rootx()
    mouse_y = root.winfo_pointery() - root.winfo_rooty()

    bx = no_btn.winfo_x()
    by = no_btn.winfo_y()
    bw = no_btn.winfo_width()
    bh = no_btn.winfo_height()

    cx = bx + bw/2
    cy = by + bh/2

    dx = cx - mouse_x
    dy = cy - mouse_y

    dist = (dx**2 + dy**2) ** 0.5
    danger = 150

    if dist < danger and dist != 0:
        vx += (dx/dist) * 1.8
        vy += (dy/dist) * 1.8

    vx *= 0.9
    vy *= 0.9

    bx += vx
    by += vy

    # Clamp inside screen
    bx = max(50, min(bx, WIDTH - bw - 50))
    by = max(200, min(by, HEIGHT - bh - 50))

    no_btn.place(x=bx, y=by)

    root.after(20, move_no_button)


# Start physics AFTER UI loads
root.after(500, move_no_button)

# ---------------- EXIT ---------------- #
root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()
