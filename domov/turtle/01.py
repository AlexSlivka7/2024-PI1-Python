import turtle
t = turtle.Turtle()

def stvorec(dlzka):
    for i in range(4):
        t.fd(dlzka)
        t.rt(90)
stvorec(100)

t.lt(70)
t.fd(80)

stvorec(50)


turtle.mainloop()