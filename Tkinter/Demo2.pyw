from tkinter import *

def xinlabel():
    global xin
    s = Label(xin, text = "我爱Python")
    s.pack()

xin = Tk()
b1 = Button(xin, text = "星哥", command = xinlabel)
b1.pack()
xin.mainloop()
