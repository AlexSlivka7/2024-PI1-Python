import tkinter as tk,random
canvas = tk.Canvas()
canvas.pack()

def vypis():
    text = "PYTHON"
    x = random.randrange(50,330)
    y = random.randrange(20,240)
    canvas.create_text(x,y,text=text,font="arial 20")

tlacidlo = tk.Button(text="vypíš text",command=vypis)
tlacidlo.pack()

tk.mainloop()
