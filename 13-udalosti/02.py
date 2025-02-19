import tkinter as tk , random
canvas = tk.Canvas()
canvas.pack()

def vypis():
    text = "PYTHON"
    x = random.randrange(50,330)
    y = random.randrange(20,240)
    canvas.create_text(x,y,text=text,font="arial 20")

def zmaz():
    canvas.delete("all")

tlacidlo1 = tk.Button(text="Vypíš text",command=vypis).pack()
tlacidlo2 = tk.Button(text="zmaž plochu",command=zmaz).pack()

vstup =tk.Entry(width=10).pack()

tk.mainloop()