from tkinter import *
from tkinter import messagebox
def show():
    n=int(t1.get())
    if val.get()==1:
        s=0
        for i in range(1,n):
            if n%i==0:
                s=s+i
        if s==n:
            messagebox.showinfo("Perfect Number","Number is Perfect Number")
        else:
            messagebox.showinfo("Perfect Number","Number is not Perfect Number")
    if val.get()==2:
        flag=0
        if n<2:
            flag=1
        else:
            for i in range(2,n):
                if n%i==0:
                    flag=1
                    break
        if flag==0:
            messagebox.showinfo("Prime Number","Number is Prime Number")
        else:
            messagebox.showinfo("Prime Number","Number is not Prime Number")
    if val.get()==3:
        s=0
        num=n
        while(n>0):
            d=n%10
            s=s+(d*d*d)
            n=n//10
        if num==s:
            messagebox.showinfo("Armstrong Number","Number is Armstrong Number")
        else:
            messagebox.showinfo("Armstrong Number","Number is not Armstrong Number")

window=Tk()
window.geometry("400x500")
val=IntVar()
l1=Label(window,text="Enter Number : ",fg="red")
t1=Entry(window,width="20",fg="blue")
r1=Radiobutton(window,text="Perfect",value=1,variable=val)
r2=Radiobutton(window,text="Prime",value=2,variable=val)
r3=Radiobutton(window,text="Armstrong",value=3,variable=val)
b1=Button(window,text="Check",command=show)
l1.grid(row=0,column=0)
t1.grid(row=0,column=1)
r1.grid(row=1,column=0)
r2.grid(row=1,column=1)
r3.grid(row=1,column=2)
b1.grid(row=2,column=0)
window.mainloop()


