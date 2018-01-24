from tkinter import *

xin = Tk()
Label(xin, text = "账号: ").grid(row = 0, sticky = W)
Entry(xin).grid(row = 0, column = 1, sticky = E)

Label(xin, text = "密码: ").grid(row = 1, sticky = W)
Entry(xin).grid(row = 1, column = 1, sticky = E)

Button(xin, text = "登录").grid(row = 2, column = 1, sticky = E)

xin.resizable(width=False, height=False)
xin.mainloop()
