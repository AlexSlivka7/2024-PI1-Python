import turtle
t = turtle.Turtle()

def n_uholnik(n, d):
    t.fd(d)
    t.lt(360/n)

for n in range(3,16):
    n_uholnik(n,50)

turtle.mainloop()