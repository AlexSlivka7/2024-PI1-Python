import turtle
t = turtle.Turtle()
turtle.delay(0)

def kvet(d, farby):
    def obluk(d):
        for i in range(9):
            t.fd(d)
            t.rt(10)
    
    def lupen(d):
        for i in range(2):
            obluk(d)
            t.rt(90)


    for f in (farby):
        t.fillcolor(f)
        t.begin_fill()
        lupen(d)
        t.end_fill()
        t.rt(360 / len(farby))


kvet(20,["red", "yellow" , "magenta" , "green" , "orange" , "cyan"])

turtle.mainloop()