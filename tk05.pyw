import tkinter as tk
root = tk.Tk()
root.title('Widget')
root.geometry('350x150')
lb = tk.Label(text='Label-1')
bt = tk.Button(text='Button-1')
lb.pack()
bt.pack()
root.mainloop()