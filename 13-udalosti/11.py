import tkinter

def klik(event):
    x, y = event.x, event.y
    canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill='red')

def tahaj(event):
    x, y = event.x, event.y
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='blue')

def zmaz(jozo):
    canvas.delete("all")

canvas = tkinter.Canvas()
canvas.pack()
canvas.bind('<B3-Motion>', klik)
canvas.bind('<B1-Motion>', tahaj)
canvas.bind("<ButtonPress-2>",zmaz)


tkinter.mainloop()