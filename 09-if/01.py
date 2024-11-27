import tkinter , random

pocet = int(input("Zadaj počet štvorčekov: "))
a = int(input("Zadaj šírku plátna: "))
b = int(input("Zadaj výšku plátna: "))

canvas = tkinter.Canvas(width=a,height=b)
canvas.pack()


for i in range(pocet):
    random_dlzka = random.randint(1,30)
    x = random.randint(3, a - random_dlzka - 3)
    y = random.randint(3, b - random_dlzka - 3)
    
    
    if random_dlzka <= 10:
        canvas.create_rectangle(x , y , x + random_dlzka, y + random_dlzka, fill="red" , width=0) # width určíme šírku okrajovej čiary
    
    elif 10 < random_dlzka <=20:
        canvas.create_rectangle(x , y , x + random_dlzka, y + random_dlzka, fill="green", width=0)
    
    else:
        canvas.create_rectangle(x , y , x + random_dlzka, y + random_dlzka, fill="blue", width=0)



tkinter.mainloop()