import tkinter

def tahaj(event):
    x, y = event.x, event.y
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=farba.get())

def zmaz(delete):
    canvas.delete("all")

def red():
    farba = "red"


canvas = tkinter.Canvas()
canvas.pack(side="left")
farba = tkinter.Button(bg="red",command=red).pack()

canvas.bind('<B1-Motion>', tahaj)
canvas.bind("<ButtonPress-2>",zmaz)


tkinter.mainloop()