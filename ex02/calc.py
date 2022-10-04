import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    tkm.showinfo(num,f"{num}のボタンがクリックされました")

root = tk.Tk()
root.title("おためしか")
root.geometry("300x500")


r, c = 0, 1
for i, num in enumerate(range(9, -1, -1), 1):
    btn = tk.Button(root, text=num, font=("Times New Roman", 30), width=4, height=2)
    btn.bind("<1>", button_click)
    btn.grid(row=r, column=c)
    if i%3 == 0:
       r += 1
       c = 0
    c += 1
    


root.mainloop()

