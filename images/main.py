from tkinter import *
import time 

def close():
    global running
    running = False

def walls():
    global speed_x, speed_y, coords

    x1, y1, x2, y2 = coords
    
    if x2 >= 400:
        speed_x = -1
    
    if x1 <= 0:
        speed_x = 1

    if y2 >= 400:
        speed_y = -1

    if y1 <= 0:
        speed_y = 1
    

root_width = 400
root_height = 500

root = Tk()
root.title("IMAGES")
root.config(width=root_width, height=root_height)
root.resizable(width=False, height=False)
root.protocol("VM_DELETE_WINDOW", close)

canvas = Canvas(root, width=400, height=400)
canvas.pack()

x = root_height / 2
y = root_width / 2
r = 20
speed_x = 1
speed_y = 1

simple_object = canvas.create_oval(x - r, y - r, x + r, y + r, fill="RED", outline="BLACK", width=3)

def particle():
    global coords
    x1, y1, x2, y2 = coords
    oval_particle = canvas.create_oval(x1, y1, x2, y2, fill="RED", outline="BLACK", width=2)
    
    return oval_particle


running = True
while running:
    canvas.move(simple_object, speed_x, speed_y)
    coords = canvas.coords(simple_object)
    print(coords)
    walls()
    particle()
    root.update()
    time.sleep(0.01)

root.destroy()
