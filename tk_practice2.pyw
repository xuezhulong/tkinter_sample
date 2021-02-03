import tkinter as tk
import time
from tkinter import messagebox

def msg_info():
    label["text"] = str(messagebox.showinfo("error","8文字以上を入力してください"))
def msg_ok():
    label["text"] = str(messagebox.showinfo("success","登録成功"))

def login():
    en_val1 = strvar1.get()
    en_val2 = strvar2.get()
    if len(en_val1)>= 8 and len(en_val2)>= 8:
        msg_ok()
        strvar1.set("")
        strvar2.set("")
        lb_time = tk.Label(text=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),font=("MS ゴシック      ", 20,"bold", "italic","normal","normal"))
        lb.pack()
    else:
        msg_info()

root = tk.Tk()
root.geometry("400x300+450+350")
text1 = tk.Label(text="student ID", font=("MS ゴシック", 20))
text2 = tk.Label(text="password", font=("MS ゴシック      ", 20))
bt = tk.Button(text="確定",command=login)
strvar1 = tk.StringVar()
en1 = tk.Entry(textvariable=strvar1)
strvar2 = tk.StringVar()
en2 = tk.Entry(textvariable=strvar2)
label = tk.Label()
[widget.pack() for widget in (text1, en1, text2, en2, bt)]
root.mainloop()