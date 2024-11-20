import tkinter
import random


pocet = int(input("Zadaj pocet stvrcov: "))
dlzka = int(input("Zadaj dlzku: "))
canvas = tkinter.Canvas(width=500,height=400)
canvas.pack()


for i in range(pocet):
    x = random.randint(3,500-dlzka-3)
    y = random.randint(3,400-dlzka-3)
    canvas.create_rectangle(x , y , x + dlzka , y + dlzka, fill=random.choice(["red" , "black" , "green" , "blue" , "pink" , "purple" , "yellow"]))

tkinter.mainloop()