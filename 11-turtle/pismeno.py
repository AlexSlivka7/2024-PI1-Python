import turtle
dlzka = 50
t = turtle.Turtle()
turtle.delay(0)

def stvorec(d):
    for i in range(4):
     t.fd(d)
     t.lt(90)


def riadok(dlzka):
    for i in range(3):
        stvorec(dlzka)
        t.penup()
        t.fd(dlzka)
        t.pendown()

riadok(dlzka)  

t.rt(90)
t.fd(dlzka)
t.lt(90)




for i in range(6):
   stvorec(dlzka)
   t.rt(90)
   t.fd(dlzka)
   t.left(90)
       
       

# t.penup()
# t.fd(dlzka*-4)
# t.pendown()
# for i in range(6):
#    stvorec(dlzka)
#    t.lt(90)
#    t.fd(dlzka)
#    t.rt(90)

# t.fd(dlzka)
# t.rt(90)
# t.fd(dlzka*3)
# t.lt(90)

# riadok(dlzka)


turtle.mainloop()