from tkinter import *

xin = Tk()
b1 = Button(xin, text = "星哥")
b1['width'] = 20
b1['height'] = 4
b1.pack()
b2 = Button(xin, text = "星哥你好")
b2['width'] = 20
b2['background'] = 'red'
b2['foreground'] = 'white'
b2.pack()
xin.mainloop()
