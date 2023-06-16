from tkinter import *

# def bebra():
#     root.quit()
#     root_bebra = Tk()
#     root_bebra.title("Bebra")
#     root_bebra.geometry("500x400")
#     root_bebra.resizable(width=False, height=False)

#     label = Label(root_bebra, text="Бебра понюхана!", font="Arial, 26")
#     label.place(x=175, y=200)

root = Tk()
root.title("Bebra")
root.geometry("500x400")
root.resizable(width=False, height=False)

button = Button(root, text="Понюхать Бебру", width=20, height=5, background="BLACK", fg="WHITE")
button.place(x=175, y=200)

# button.bind(bebra())

root.mainloop()