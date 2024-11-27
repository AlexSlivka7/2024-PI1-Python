import tkinter , random
canvas_width = int(input("Zadaj šírku plátna: "))
canvas_height = int(input("Zadaj výšku plátna: "))

canvas = tkinter.Canvas(width=canvas_width,height=canvas_height)
canvas.pack()

for i in range(1000):
    x = random.randint(3,canvas_width-13)
    y = random.randint(3,canvas_height-13)

if x > canvas_width//4 and y > canvas_height//3/4:
    farba = "black"
    





canvas.create_oval(x , y, x+10, y+10, fill=farba , width=0)


tkinter.mainloop()