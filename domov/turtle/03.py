import turtle,random
t = turtle.Turtle()
turtle.delay(0)

def dom(d):
    def stvorec(dlzka):
        for i in range(4):
            t.fd(dlzka)
            t.rt(90)
    def trojuholnik(dlzka):
        for i in range(3):
            t.fd(dlzka)
            t.rt(120)
    t.pencolor("blue")
    stvorec(d)
    t.lt(60)
    t.pencolor("red")
    trojuholnik(d)
    t.rt(60)

def posun():
    t.pu()
    t.setposition(random.randint(-150,150),random.randint(-100,100))
    t.seth(random.randint(-30,30))
    t.pd()

t.pensize(5)
for i in range(20):
    posun()
    dom(30)

turtle.mainloop()