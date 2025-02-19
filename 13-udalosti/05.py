import tkinter as tk
canvas = tk.Canvas()
canvas.pack()

def klik(event):
    canvas.create_line(100,200,event.x,event.y)

canvas.bind("<ButtonPress>",klik)

tk.mainloop()