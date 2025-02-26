import tkinter

def cervena(event):
    x, y = event.x, event.y
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red")

def modra(event):
    x, y = event.x, event.y
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="blue")

def zmaz(delete):
    canvas.delete("all")



canvas = tkinter.Canvas()
canvas.pack(side="left")
canvas.bind('<B1-Motion>', cervena)
canvas.bind("<B3-Motion>",modra)
canvas.bind("<ButtonPress-2>",zmaz)


tkinter.mainloop()