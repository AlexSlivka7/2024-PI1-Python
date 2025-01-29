import turtle
dlzka = int(input("Zadaj dĺžku: "))
pocet = int(input("Zadaj počet domčekov: "))
pocet_riadkov = int(input("Zadaj počet riadkov: "))
t = turtle.Turtle()
turtle.delay(0)

turtle.screensize(canvwidth=500, canvheight=500)
t.pu()
t.seth(0.0)
t.setpos(-500+dlzka,500-dlzka*4)
t.pd()


def domček(dlzka):
    def stvorec(dlzka):
        t.fd(dlzka)
        t.lt(90)
        t.fd(dlzka)
        t.lt(90)
        t.fd(dlzka)
        t.lt(90)
        t.fd(dlzka)
        t.lt(90)
        
    t.fillcolor("red")
    t.begin_fill()
    stvorec(dlzka)
    t.end_fill()
    
    
    t.lt(90)
    t.fd(dlzka)

    def trojuholnik(dlzka):
        t.rt(30)
        t.fd(dlzka)
        t.rt(120)
        t.fd(dlzka)
    
    t.fillcolor("black")
    t.begin_fill()
    trojuholnik(dlzka)
    t.end_fill()

    t.rt(120)
    t.fd(dlzka)
    t.lt(90)
    t.fd(dlzka/4)
    t.lt(90)
    t.pu()
    t.fd(dlzka/4)
    t.pd()

    def okno(dlzka):
        for i in range(4):
            t.fd(dlzka/2)
            t.rt(90)
    t.fillcolor("white")
    t.begin_fill()
    okno(dlzka)
    t.end_fill()

    
    t.fd(dlzka/4)
    t.rt(90)
    t.fd(dlzka/2)
    t.lt(90)
    t.fd(dlzka/4)
    t.lt(90)
    t.fd(dlzka/4)
    t.lt(90)
    t.fd(dlzka/2)

    t.pu()
    t.lt(90)
    t.fd(dlzka/2)
    t.lt(90)
    t.fd(dlzka/2)
    t.fd(dlzka/4)

def riadok_domcekov(dlzka,pocet):
    for i in range(pocet):
        domček(dlzka)
        t.pu()
        t.fd(dlzka/2)
        t.pd()


def riadky_domcekov(dlzka,pocet,pocet_riadkov):
    for i in range(pocet_riadkov):
        riadok_domcekov(dlzka,pocet)
        t.pu()
        t.lt(180)
        t.fd(dlzka/2*pocet)
        t.fd(dlzka*pocet)
        t.lt(90)
        t.fd(dlzka*2)
        t.lt(90)
        t.pd()
        

riadky_domcekov(dlzka,pocet,pocet_riadkov)




turtle.mainloop()
