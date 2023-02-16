from tkinter import *
import random
root=Tk()
root.title("Rolling Dice")
root.geometry("800x800")
root.configure(bg='grey')
lb=Label(root,font="gungsuh 30 bold ",fg="purple",text="Dice Rolling",bg="grey")
l=Label(root,font="times_roman 300 bold",fg="red",text="",bg="grey")
l1=Label(root,font="times_roman 300 bold",fg="orange",text="",bg="grey")
def roll():
    d=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    x=l.configure(text=f'{random.choice(d)}')
    l.pack()
def roll1():
    d1=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    x=l1.configure(text=f'{random.choice(d1)}')
    l1.pack()
lb.pack()
b=Button(root,font="times_roman 20 bold",text="Roll Dice 1",command=roll,bg='pink',width=10)
b.place(x=50,y=400)
b1=Button(root,font="times_roman 20 bold",text="Roll Dice 2",command=roll1,bg='pink',width=10)
b1.place(x=600,y=400)
b3=Button(root,font="times_roman 20 bold",text="Roll Both Dice",command=lambda:[roll(),roll1()],bg='pink',width=12)
b3.place(x=300,y=80)
root.mainloop()