import turtle
pocet = int(input("Zadaj počet štvorcov: "))
dlzka = int(input("Zadaj dlžku štvorca: "))
pocet_riadkov = int(input("Zadaj pocet riadkov: "))
screen =turtle.Screen()
screen.setup(width=800,height=800)
t = turtle.Turtle()
t.pos()
(0,0)
t.heading()
(0,0)
t.penup()
top_leftx = -screen.window_width()// 2

top_left_y = screen.window_height() // 2
t.goto(top_leftx,top_left_y)
t.pendown()

def stvorec(dlzka):
    for i in range(4):
     t.forward(dlzka)
     t.right(90)

def riadok_stvorcov(dlzka,pocet_riadkov):
    for i in range(pocet):
     stvorec(dlzka)
     t.fd(dlzka)
riadok_stvorcov(dlzka,3)



   
   


turtle.mainloop()