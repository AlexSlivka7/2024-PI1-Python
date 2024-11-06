import tkinter

canvas = tkinter.Canvas()       # vytvorenie plátna a jeho priradenie do premennej canvas
canvas.pack()   #umiestnenie plátna do okna

canvas.create_text(100, 75 , text = "Ahoj")
#vypíše text "ahoj na pozícii x 100 y 100"
# súradnice zadávame vždy v poradí x,y
# x rastie nahor do prava 
# y rastie smerom dole

canvas.create_rectangle(50,50,150,100)
# vykreslenie štvorca resp. obdĺžníka
#prvé dve čísla určujú pozíciu začiatočného bodu
#dalšie dve určuju pozíciu koncového bodu

canvas.create_oval(50,50,150,100)
# vykreslenie kruhu (oválu)
#prvé dve čísla určujú pozíciu začiatočného bodu
#dalšie dve určuju pozíciu koncového bodu

tkinter.mainloop()  # aby zostalo okno otvorené aby sa nezavrelo