#Srdiečko
text = input("Zadaj text: ")
dlzka = int(input("Zadaj dĺžku: "))
velkost = int(input("Zadaj velkost textu: "))
import tkinter
canvas = tkinter.Canvas(width=1000, height=1000)
canvas.pack()
x = 20
y = 20
canvas.create_oval(x,y, x+dlzka, y+dlzka,fill="red",outline="red")
canvas.create_oval(x+dlzka - x, y, x+dlzka*2 - x, y + dlzka  ,fill="red",outline="red")
canvas.create_polygon(x + 2 , y+dlzka/2 + y   ,x + dlzka * 2 -x ,y + dlzka/2 + y,    x +dlzka - 5 ,y + dlzka * 2 ,fill="red")
canvas.create_text(x+dlzka,y+dlzka, text=text,font=('Helvetica', velkost, 'bold'))

tkinter.mainloop()