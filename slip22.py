import time
from tkinter import *
window=Tk()
window.title("Digital Clock")
window.geometry("350x200")
window.resizable(1,1)
l1=Label(window,font=("arial",20,'bold'),bg="pink",fg="white",bd=10)
l1.grid(row=0,column=1)
def digitalClock():
    text_input=time.strftime("%H:%M:%S")
    l1.config(text=text_input)
    l1.after(200,digitalClock)
digitalClock()
window.mainloop()
