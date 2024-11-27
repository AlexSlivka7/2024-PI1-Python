import tkinter , random
canvas_width = int(input("Zadaj šírku plátna: "))
canvas_height = int(input("Zadaj výšku plátna: "))

canvas = tkinter.Canvas(width=canvas_width,height=canvas_height)
canvas.pack()

for i in range(1000):
    x = random.randint(3,canvas_width-13)
    y = random.randint(3,canvas_height-13)

    if canvas_width// 4 * 3 >= x >= canvas_width // 4 and canvas_height// 4 <= y <= canvas_height// 4 * 3:
        farba = "black" 
    else:
        if x <= canvas_width // 2:
            if y <= canvas_height // 2:
                farba = "blue"
            else:
                farba = "green"
        else:
            if y <= canvas_height //2:
                farba = "red"
            else:
                farba = "gold"

    canvas.create_oval(x , y, x+10, y+10, fill=farba , width=0)


tkinter.mainloop()