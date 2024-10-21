import tkinter.messagebox
def show():
    tkinter.messagebox.showinfo("Alert Message...","Are you sure")
window=tkinter.Tk()
window.geometry("500x400")
b1=tkinter.Button(window,text="OK",command=show)
b1.place(x=250,y=200)
window.mainloop()
