import tkinter as tk

canvas = tk.Canvas()
canvas.pack()

fbody = open("body.txt", "r")
for body in fbody:
    print(body)
    medzera = body.find(" ")
    x = int(body[:medzera])
    y = int(body[medzera+1:])
    print(x)
    print(y)
    canvas.create_oval(x-5 ,y-5 ,x+5 ,y+5)

tk.mainloop()