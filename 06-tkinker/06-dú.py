import tkinter

canvas = tkinter.Canvas()
canvas.pack()
#A:
canvas.create_rectangle(30,10,40,20,fill="black")
canvas.create_rectangle(42,10,52,20,fill="black")
canvas.create_rectangle(54,10,64,20,fill="black")

canvas.create_rectangle(18,18,28,28,fill="black")
canvas.create_rectangle(18,28,28,38,fill="black")
canvas.create_rectangle(18,38,28,48,fill="black")
canvas.create_rectangle(18,48,28,58,fill="black")
canvas.create_rectangle(18,58,28,68,fill="black")
canvas.create_rectangle(18,68,28,78,fill="black")

canvas.create_rectangle(60,20,70,30,fill="black")
canvas.create_rectangle(60,30,70,40,fill="black")
canvas.create_rectangle(60,40,70,50,fill="black")
canvas.create_rectangle(60,50,70,60,fill="black")
canvas.create_rectangle(60,60,70,70,fill="black")
canvas.create_rectangle(60,70,70,80,fill="black")

canvas.create_rectangle(30,40,40,50,fill="black")
canvas.create_rectangle(40,40,50,50,fill="black")
canvas.create_rectangle(50,40,60,50,fill="black")

#S:
canvas.create_rectangle(90,10,100,20,fill="black")
canvas.create_rectangle(100,10,110,20,fill="black")
canvas.create_rectangle(110,10,120,20,fill="black")
canvas.create_rectangle(120,10,130,20,fill="black")

canvas.create_rectangle(80,20,90,30,fill="black")
canvas.create_rectangle(80,30,90,40,fill="black")

canvas.create_rectangle(90,10,100,20,fill="black")
canvas.create_rectangle(100,10,110,20,fill="black")
canvas.create_rectangle(110,10,120,20,fill="black")



tkinter.mainloop()