from tkinter import *
from datetime import date
root=Tk()
root.title("Window")
root.geometry("400x500")
root.configure(background="blue")

l1=Label(text="Welcome", bg="blue",fg="white")
l1.pack()

inp=Entry()
inp.pack()

ttb=Text(height=3)
ttb.pack()

def a():
    name=inp.get()
    global Message
    Message="Welcome to my Applicatoin \n Today's date is: "
    greet = "Hello"+name+"\n"
    ttb.insert(END,greet)
    ttb.insert(END,Message)
    ttb.insert(END, date.today())
    
btn=Button(text="Click", command=a)
btn.pack()
    

root.mainloop()