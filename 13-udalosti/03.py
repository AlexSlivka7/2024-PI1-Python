import tkinter as tk , random
canvas = tk.Canvas()
canvas.pack(side="left")

def vypis():
    
    x = random.randrange(50,330)
    y = random.randrange(20,240)
    canvas.create_text(x,y,
                       text=vstup.get(),
                       font=f"arial {velkost.get()}",
                       fill=farba.get())
                      
def zmaz():
    canvas.delete("all")

tlacidlo1 = tk.Button(text="Vypíš text",command=vypis).pack()
tlacidlo2 = tk.Button(text="zmaž plochu",command=zmaz).pack()

tk.Label(text="Zadaj text: ").pack()
vstup =tk.Entry(width=10)
vstup.pack()

tk.Label(text="Zadaj farbu: ").pack()
farba =tk.Entry(width=10)
farba.pack()

tk.Label(text="Zadaj veľkosť: ").pack()
velkost = tk.Scale(orient="horizontal",from_=10,to=40,length=75)
velkost.pack()



tk.mainloop()