import tkinter
domček = tkinter.Canvas(width=500, height=500)
domček.pack()

#pozadie:
domček.create_rectangle(0,400,500,500,fill="lime")
domček.create_rectangle(0,0,500,400,fill="blue")

#domček:
domček.create_rectangle(200,200,400,400,fill="saddle brown") #dom
domček.create_rectangle(225,325,275,400,fill="brown4") #dvere
domček.create_rectangle(225,240,275,290,fill="cyan") #ľavé okno
domček.create_rectangle(325,240,375,290,fill="cyan") #pravé okno
domček.create_polygon(150,230,450,230,300,100,fill="red4") #strecha
domček.create_polygon(350,145,385,175,385,125,350,125,fill="grey23")#komín

#detaily:
    #oblak:
domček.create_oval(50,50,100,100,fill="white",outline="white")
domček.create_oval(80,35,130,85,fill="white",outline="white")
domček.create_oval(110,50,160,100,fill="white",outline="white")
domček.create_oval(140,35,190,85,fill="white",outline="white")
domček.create_oval(20,35,70,85,fill="white",outline="white")
    #dym:
domček.create_oval(355,90,380,115,fill="grey47",outline="grey47")
domček.create_oval(365,70,390,95,fill="grey47",outline="grey47")
domček.create_oval(355,50,380,75,fill="grey47",outline="grey47")
    #číslo domu
domček.create_text(350,350,text="638",font=60)


tkinter.mainloop()