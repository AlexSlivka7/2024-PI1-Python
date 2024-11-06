import tkinter

canvas = tkinter.Canvas()
canvas.pack()
#A:
# horný riadok
canvas.create_rectangle(30,10,40,20,fill="black")
canvas.create_rectangle(42,10,52,20,fill="black")
canvas.create_rectangle(54,10,64,20,fill="black")
#ľavá noha
canvas.create_rectangle(18,18,28,28,fill="black")
canvas.create_rectangle(18,30,28,40,fill="black")
canvas.create_rectangle(18,42,28,52,fill="black")
canvas.create_rectangle(18,54,28,64,fill="black")
canvas.create_rectangle(18,66,28,76,fill="black")
canvas.create_rectangle(18,78,28,88,fill="black")
#pravá noha
canvas.create_rectangle(66,18,76,28,fill="black")
canvas.create_rectangle(66,30,76,40,fill="black")
canvas.create_rectangle(66,42,76,52,fill="black")
canvas.create_rectangle(66,54,76,64,fill="black")
canvas.create_rectangle(66,66,76,76,fill="black")
canvas.create_rectangle(66,78,76,88,fill="black")
#stred
canvas.create_rectangle(30,42,40,52,fill="black")
canvas.create_rectangle(42,42,52,52,fill="black")
canvas.create_rectangle(54,42,64,52,fill="black")

#S:
#horný riadok
canvas.create_rectangle(100,10,110,20,fill="black")
canvas.create_rectangle(112,10,122,20,fill="black")
canvas.create_rectangle(124,10,134,20,fill="black")
canvas.create_rectangle(136,10,146,20,fill="black")
#prechod ľavý
canvas.create_rectangle(88,20,98,30,fill="black")
canvas.create_rectangle(88,32,98,42,fill="black")
#stredný riadok
canvas.create_rectangle(100,44,110,54,fill="black")
canvas.create_rectangle(112,44,122,54,fill="black")
canvas.create_rectangle(124,44,134,54,fill="black")
#prechod pravý
canvas.create_rectangle(136,56,146,66,fill="black")
canvas.create_rectangle(136,68,146,78,fill="black")
#dolný riadok
canvas.create_rectangle(88,80,98,90,fill="black")
canvas.create_rectangle(100,80,110,90,fill="black")
canvas.create_rectangle(112,80,122,90,fill="black")
canvas.create_rectangle(124,80,134,90,fill="black")


tkinter.mainloop()