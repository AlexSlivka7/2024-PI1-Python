import tkinter
canvas = tkinter.Canvas(width=600,height=600)
canvas.pack()

def y_(x, y):
    canvas.create_rectangle(x, y, x + 10, y + 10 ,fill="black" , outline="white")
    canvas.create_rectangle(x, y + 10, x + 10, y + 20 ,fill="black" , outline="white")
    canvas.create_rectangle(x + 10, y + 20, x + 20, y + 30 ,fill="black" , outline="white")
    canvas.create_rectangle(x + 20, y + 30, x + 30, y + 40 ,fill="black" , outline="white")
    canvas.create_rectangle(x + 20, y + 40, x + 30, y + 50 ,fill="black" , outline="white")
    canvas.create_rectangle(x + 20, y + 50, x + 30, y + 60 ,fill="black" , outline="white")
    canvas.create_rectangle(x + 20, y + 60, x + 30, y + 70 ,fill="black" , outline="white")
    canvas.create_rectangle(x + 30, y + 20, x + 40, y + 30 ,fill="black" , outline="white")
    canvas.create_rectangle(x + 40, y + 10, x + 50, y + 20 ,fill="black" , outline="white")
    canvas.create_rectangle(x + 40, y , x + 50, y + 10 ,fill="black" , outline="white")

def riadok_y(x , y ,pocet):
    for i in range(pocet):
       y_(x , y)
       x +=60

def riadky_y(x, y, pocet_riadkov, pocet_stĺpcov):
    for i in range(pocet_riadkov):
        riadok_y(x, y , pocet_stĺpcov)
        y +=90 

y_(10,10)
riadok_y(10,100,3)
riadky_y(10,190,2,4)

tkinter.mainloop()