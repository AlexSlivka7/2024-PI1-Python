import turtle
dlzka = int(input("Zadaj dlzku stvorca: "))
t = turtle.Turtle()
turtle.delay(0)

def A(dlzka):

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


    def stplec(dlzka):
        for i in range(6):
        
            t.rt(90)
            t.fd(dlzka)
            t.lt(90)
            stvorec(dlzka)
    stplec(dlzka)

    t.penup()
    t.fd(-4*dlzka)
    t.lt(90)
    t.fd(6*dlzka)
    t.rt(90)
    t.pendown()

    stplec(dlzka)

    t.penup()
    t.lt(90)
    t.fd(3*dlzka)
    t.rt(90)
    t.fd(dlzka)
    t.pendown()
    riadok(dlzka)

A(dlzka)


turtle.mainloop()