import turtle
t = turtle.Turtle()

def n_uholnik(n, d):
    for i in range(n):
        t.fd(d)
        t.lt(360/n)

for n in range(3,16):
    t.clear()
    n_uholnik(n,50)

turtle.mainloop()