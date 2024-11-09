#Srdiečko

import tkinter
canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

canvas.create_oval(99,50,260,200,fill="red",outline="red")
canvas.create_oval(249,50,401,200,fill="red",outline="red")
canvas.create_polygon(100,145,400,145,250,400,fill="red")


tkinter.mainloop()