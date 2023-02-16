from tkinter import *
root=Tk()
root.title("Counter")
root.geometry("750x500")
root.configure(bg='#FFEFDB')
lb=Label(root,font="times_roman 40 bold ",fg="blue",text="COUNTER",bg="#FFEFDB")
c=0
l=Label(root,font="times_roman 250 bold",fg="red",text=c,bg="#FFEFDB")
def counting():
    global c
    c += 1
    l.config(text=c)
    l.pack()
def exit():
    root.destroy()
def decrem():
    global c
    c -= 1
    l.config(text=c)
    l.pack()
def reset():
    global c
    c=0
    l.config(text=c)
    l.pack()
lb.pack()
b=Button(root,font="times_roman 10 bold",text="INCREMENT",command=counting,bg="grey",width=15)
b.place(x=330,y=80)
b1=Button(root,font="times_roman 10 bold",text="EXIT",command=exit,bg="grey",width=15)
b1.place(x=330,y=385)
b2=Button(root,font="times_roman 10 bold",text="DECREMENT",command=decrem,bg="grey",width=15)
b2.place(x=160,y=80)
b3=Button(root,font="times_roman 10 bold",text="RESET",command=reset,bg="grey",width=15)
b3.place(x=500,y=80)
root.mainloop()