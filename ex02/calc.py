import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    #tkm.showinfo(num,f"{num}のボタンがクリックされました")
    entry.insert(tk.END, num) #練習5


def click_equal(event):
    eqn = entry.get()
    result = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result) #練習7 

root = tk.Tk()
#root.title("おためしか")
root.geometry("300x500")

entry = tk.Entry(root, width=10, font=("Times New Roman", 40), justify="right")
entry.grid(row=0, column=0, columnspan=3) 


r, c = 1, 0
numbers = list(range(9, -1, -1))
operators = ["+"]
for i, num in enumerate(numbers+operators, 1): #練習６
    btn = tk.Button(root, text=num, font=("Times New Roman", 30), width=4, height=2)
    btn.bind("<1>", button_click)
    btn.grid(row=r, column=c)
    c += 1
    if i%3 == 0:
       r += 1
       c = 0
    
    
btn = tk.Button(root, text=f"=", font=("Times New Roman", 30), width=4, height=2)
btn.bind("<1>", click_equal)
btn.grid(row=r, column=c)

root.mainloop()

