# -*- conding: utf-8 -*-
# tk21.pyw

import tkinter as tk
root = tk.Tk()
strvar = tk.StringVar()
en = tk.Entry(textvariable=strvar)
strvar.set("Hello World")
en.pack()
root.mainloop()