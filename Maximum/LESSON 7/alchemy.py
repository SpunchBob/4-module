from tkinter import *
import random

root = Tk()
root.geometry("600x600")
root.title("alchemy")
root.resizable(height=False, width=False)

canvas = Canvas(width=600, height=600)
canvas.pack()
class Steam:
    image = PhotoImage(file = r'C:\Users\User\Desktop\Programming\Доп. материалы\aroma.png').subsample(4, 4)

class Water:
    image = PhotoImage(file = r'C:\Users\User\Desktop\Programming\Доп. материалы\water.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Fire):
            return Steam
        if isinstance(other, Ground):
            return Pottery
class Fire:
    image = PhotoImage(file = r'C:\Users\User\Desktop\Programming\Доп. материалы\fire.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam
class Wind:
    image = PhotoImage(file = r'C:\Users\User\Desktop\Programming\Доп. материалы\wind.png').subsample(4, 4)

    def __add__(self, other):
        if isinstance(other, Ground):
            return Dust
class Ground:
    image = PhotoImage(file = r'C:\Users\User\Desktop\Programming\Доп. материалы\ground.png').subsample(4, 4)

    def __add__(sefl, other):
        if isinstance(other, Water):
            return Pottery
        if isinstance(other, Wind):
            return Dust
class Pottery:
    image = PhotoImage(file = r'C:\Users\User\Desktop\Programming\Доп. материалы\pottery.png').subsample(4, 4)

class Dust:
    image = PhotoImage(file = r'C:\Users\User\Desktop\Programming\Доп. материалы\dust.png').subsample(4, 4)


elements = [Wind(), Fire(), Water(), Ground()]

for elem in elements:
    canvas.create_image(random.randint(50, 550), random.randint(50, 550), image=elem.image)

def move(event):
    images_ids = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)
    if len(images_ids) == 2:
        elem_id_1, elem_id_2 = images_ids[0], images_ids[1]
        elem_1 = elements[elem_id_1 - 1]
        elem_2 = elements[elem_id_2 - 1]
    
        new_elem = elem_1 + elem_2

        if new_elem not in elements:
            elements.append(new_elem)
            canvas.create_image(event.x, event.y, image=new_elem.image)

    canvas.coords(images_ids, event.x, event.y)
    print(images_ids)

root.bind("<B1-Motion>", move)

root.mainloop()