from tkinter import *
import time

def close():
    global running
    running = False

class Polygone():

    def __init__(self):
        ...

root_width = 500
root_height = 400

root = Tk()
root.title("POLY")
root.config(width=root_width, height=root_height)
root.resizable(width=False, height=False)
root.protocol("VM_DELETE_WINDOW", close)

canvas = Canvas(width=root_width, height=root_height)
canvas.pack()

running = True()
while running:

    root.update()
    time.sleep(0.01)

root.destroy()
