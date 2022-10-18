import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global mx, my
    global cx, cy
    if key == "Up":
        my -= 1
    if key == "Down":
        my += 1
    if key == "Left":
        mx -= 1
    if key == "Right":
        mx += 1
    if maze_lst[my][mx] !=1  :
        cx, cy = mx*100+50 ,my*100+50

    else:
        if key == "Up":
            my += 1
        if key == "Down":
            my -= 1
        if key == "Left":
            mx += 1
        if key == "Right":
            mx -= 1
    canv.coords("tori", cx, cy)

    if key == "x":
        my=6
        mx=13
        cx, cy = mx*100+50 ,my*100+50
    
    if my==7 and mx==13:
        tkm.showinfo("ゴール", f"おめっ!!")

    else:
        root.after(100,main_proc)



if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    maze_lst = mm.make_maze(15, 9)
    #print(maze_lst)
    mm.show_maze(canv, maze_lst)

    tori = tk.PhotoImage(file="fig/3.png")
    mx, my= 1, 1
    cx, cy = mx*100+50, my*100+50
    canv.create_image(cx, cy, image=tori, tag="tori")

    key = "" #現在押されているキー
    
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    
    main_proc()
  
    root.mainloop()