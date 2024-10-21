from tkinter import *
from datetime import date
window=Tk()
window.geometry("400x500")
window.title("Age Calculator")
def calculateAge():
    today=date.today()
    birthDate=date(int(yearEntry.get()),int(monthEntry.get()),int(dayEntry.get()))
    age=today.year-birthDate.year-((today.month,today.day)<(birthDate.month,birthDate.day))
    Label(text=f"{nameValue.get()} your age is {age}").grid(row=6,column=1)
Label(text="Name").grid(row=1,column=0,padx=90)
Label(text="Year").grid(row=2,column=0)
Label(text="Month").grid(row=3,column=0)
Label(text="Day").grid(row=4,column=0)

nameValue=StringVar()
yearValue=StringVar()
monthValue=StringVar()
dayValue=StringVar()

nameEntry=Entry(window,textvariable=nameValue)
yearEntry=Entry(window,textvariable=yearValue)
monthEntry=Entry(window,textvariable=monthValue)
dayEntry=Entry(window,textvariable=dayValue)

nameEntry.grid(row=1,column=1,pady=10)
yearEntry.grid(row=2,column=1,pady=10)
monthEntry.grid(row=3,column=1,pady=10)
dayEntry.grid(row=4,column=1,pady=10)

computeButton=Button(text="Calculate Age",command=calculateAge)
computeButton.grid(row=5,column=1,pady=10)
window.mainloop()
