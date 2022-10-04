import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo(num,f"{num}のボタンがクリックされました")
    entry.insert(tk.END, num) #練習5

def click_bth(event):
    tkm.showwarning("警告","まだやるかい？")

def click_btr(event):
    tkm.showinfo("イベント","私は一向に構わんッッ")

def click_point(event):
    btn = event.widget
    num = btn["text"]
    entry.insert(tk.END, num) 


def click_AC(event):
    entry.delete(0, tk.END) 


def click_equal(event):
    eqn = entry.get()
    result = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result) #練習7 

root = tk.Tk()
#root.title("おためしか")
root.geometry("500x650")

entry = tk.Entry(root, width=10, font=("Times New Roman", 40), justify="right")
entry.grid(row=0, column=0, columnspan=3) 


r, c = 1, 0
numbers = list(range(9, -1, -1))
operators = ["+","-","*","/","**"]
for i, num in enumerate(numbers+operators, 1): #練習６
    btn = tk.Button(root, text=num, font=("Times New Roman", 30), width=4, height=1)
    btn.bind("<1>", button_click)
    btn.grid(row=r, column=c)
    c += 1
    if i%3 == 0:
       r += 1
       c = 0
 #花山
btn = tk.Button(root, text=f"花山", font=("Times New Roman", 30), bg="#ff7f00", fg="black", width=4, height=1)
btn.bind("<1>", click_bth)
btn.grid(row=3, column=3)
　#烈
btn = tk.Button(root, text=f"烈", font=("Times New Roman", 30), bg="#ff7f00", fg="black", width=4, height=1)
btn.bind("<1>", click_btr)
btn.grid(row=4, column=3)

 #小数点
btn = tk.Button(root, text=f".", font=("Times New Roman", 30), bg="#ff7f00", fg="black", width=4, height=1)
btn.bind("<1>", click_point)
btn.grid(row=2, column=3)
 
 # ACボタン作成
btn = tk.Button(root, text=f"AC", font=("Times New Roman", 30), bg="#ff7f00", fg="black", width=4, height=1)
btn.bind("<1>", click_AC)
btn.grid(row=1, column=3)
   
    
btn = tk.Button(root, text=f"=", font=("Times New Roman", 30), bg="cyan", fg="black", width=4, height=1)
btn.bind("<1>", click_equal)
btn.grid(row=5, column=3)

root.mainloop()

