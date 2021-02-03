# -*- conding: utf-8 -*-
import tkinter as tk
root = tk.Tk()
lb = tk.Label(text="M S ゴシック,　サイズ20, 太字でない,　斜体, 下線なし, 取消線あり", font=("M S ゴシック", 20,"normal", "italic", "normal", "overstrike"))
lb.pack()
root.mainloop()