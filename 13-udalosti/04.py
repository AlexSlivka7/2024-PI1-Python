import tkinter as tk
canvas = tk.Canvas()
canvas.pack()

def klik(event):
    x,y = event.x, event.y
    canvas.create_oval(x - 10,y - 10,x + 10, y +10, fill="red")

canvas.bind("<ButtonPress>",klik)

tk.mainloop()