import tkinter as tk
def login():
    en_val1 = strvar1.get()
    en_val2 = strvar2.get()
    print("ID: "+en_val1)
    print("NAME: "+en_val2)
    strvar1.set("")
    strvar2.set("")
root = tk.Tk()
root.geometry("200x150")
text1 = tk.Label(text="student ID")
text2 = tk.Label(text="Name")
bt = tk.Button(text="Set",command=login)
strvar1 = tk.StringVar()
en1 = tk.Entry(textvariable=strvar1)
strvar2 = tk.StringVar()
en2 = tk.Entry(textvariable=strvar2)
[widget.pack() for widget in (text1, en1, text2, en2, bt)]
root.mainloop()