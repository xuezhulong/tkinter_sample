# -*- conding: utf-8 -*-
# tk25.pyw

import tkinter as tk
def get_text():
    print(tx.get("1.5","3.4"))

root = tk.Tk()
tx = tk.Text(width=30, height=5)
bt = tk.Button(text="get Line1-Col6 to Line3-Col4",command=get_text)
[widget.pack() for widget in(tx, bt)]
root.mainloop()