from tkinter import *
from tkinter.filedialog import *
from lab1 import lab1

def GetPath(event):
    fd = askopenfile()
    path.delete(0, END)
    path.insert(0, fd.name)

def SaveFile(event):
    label_status.configure(text="Ожидайте...")
    flag = lab1(path.get())
    label_status.configure(text=flag)


root = Tk()
root.title("Лабораторная работа №1")

fr = Frame(root)


label_path = Label(fr, text="Путь:")
path = Entry(fr)

review = Button(fr, text="обзор")
review.bind("<Button-1>", GetPath)

btn = Button(root, text="Рассчитать")
btn.bind("<Button-1>", SaveFile)
canv = Canvas(root, width=300, height=5)
canv.create_line(0,3,300,3,width=2,fill="black")
label_status = Label(root, text="Программа готова")

fr.pack()
label_path.grid(row=1)
path.grid(row=1, column=1)
review.grid(row=1, column=2)
btn.pack()
canv.pack()
label_status.pack()

root.mainloop()