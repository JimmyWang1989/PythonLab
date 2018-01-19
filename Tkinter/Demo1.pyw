from tkinter import *

root = Tk()
root.wm_title("辛星tkinter教程")
w1 = Label(root, text = "跟着星哥一起学tkinter", background = "green")
w2 = Label(root, text = "我爱python,因为它简洁", background = "red")
w3 = Label(root, text = "开创梦想,从现在做起", background = "yellow")
w1.pack()
w2.pack()
w3.pack()
root.mainloop()
