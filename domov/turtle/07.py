import turtle
t = turtle.Turtle()
turtle.delay(0)

t.lt(30)
for i in range(3,300,3):
    t.fd(i)
    t.rt(90)

turtle.mainloop()