from tkinter import *

def xinlabel(event):
    global xin
    s = Label(xin, text = "我爱Python")
    s.pack()

xin = Tk()
b1 = Button(xin, text = "星哥")
b1.bind("<Button-1>", xinlabel)
b1.pack()
xin.mainloop()
