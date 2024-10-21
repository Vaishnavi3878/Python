from tkinter import *
def change1():
    window.config(bg="pink")
def change2():
    window.config(bg="yellow")
def change3():
    window.config(bg="red")
def change4():
    window.config(bg="orange")
def change5():
    window.config(bg="cyan")
window=Tk()
window.geometry("500x400")
menubar=Menu(window)
color=Menu(menubar)
color.add_command(label="Pink",command=change1)
color.add_command(label="Yellow",command=change2)
color.add_command(label="Red",command=change3)
color.add_command(label="Orange",command=change4)
color.add_command(label="Cyan",command=change5)
menubar.add_cascade(label="Color",menu=color)
window.config(menu=menubar)
window.mainloop()
