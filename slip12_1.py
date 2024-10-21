from tkinter import *
window=Tk()
window.geometry("500x400")
def show():
    l1.config(font=("Bell MT",50,"bold"),bg="pink",fg="red")
l1=Label(window,text="Hello World!")
l1.place(x=50,y=50)
b1=Button(window,text="Change font",command=show)
b1.place(x=50,y=150)
window.mainloop()
