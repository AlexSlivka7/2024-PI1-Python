import tkinter

canvas = tkinter.Canvas(width=320 , height=320)  #nastavujem veĺkosť plátna     
canvas.pack() 

canvas.create_rectangle(10,10,110,110, fill="red")
canvas.create_text(60,60, text="Ahoj")

canvas.create_rectangle(110,110,210,210,fill="blue")
canvas.create_text(160,160,text="Ahoj")

canvas.create_rectangle(210,110,310,10,fill="green")
canvas.create_text(260,60,text="Ahoj")

canvas.create_rectangle(10,210,110,310,fill="deeppink2")
canvas.create_text(60,260,text="Ahoj")

canvas.create_rectangle(210,210,310,310,fill="gold")
canvas.create_text(260,260,text="Ahoj")

tkinter.mainloop()