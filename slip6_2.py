from tkinter import *
window=Tk()
window.geometry("500x600")
def show_1():
    l1.config(font=('Gigi',20,"bold"))
    l1.config(bg="pink",fg="red")
def show_2():
    l1.config(font=('Helvetica bold',40))
    l1.config(bg="cyan",fg="red")
def show_3():
    l1.config(font=('Bell MT',30,"bold"))
    l1.config(bg="White",fg="blue")
def show_4():
    l1.config(font=('Arial',35,"bold"))
    l1.config(bg="grey",fg="black")
l1=Label(window,text="Hello World!")
l1.place(x=100,y=100)

Label(window,text="Select the Font Style").place(x=100,y=200)
b1=Checkbutton(window,text="Gigi-20-bold-bg:pink-fg:red",command=show_1)
b1.place(x=100,y=250)
b2=Checkbutton(window,text="Helvetica bold-40-bg:cyan-fg:red",command=show_2)
b2.place(x=100,y=300)
b3=Checkbutton(window,text="Bell MT-30-bold-bg:white-fg:blue",command=show_3)
b3.place(x=100,y=350)
b4=Checkbutton(window,text="Arial-20-bold-bg:grey-fg:black",command=show_4)
b4.place(x=100,y=400)
window.mainloop()
