import random , tkinter as tk
canvas = tk.Canvas(width=800, height=800)
canvas.pack()
ftvary = open("tvary.txt", "w")
tvary = ["o","r","l"]

def nahodná_farba():
    return f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}"

# for i in range(10):
#     print(random.choice(tvary) , random.randint(3,797),random.randint(3,797),random.randint(3,797),random.randint(3,797),nahodná_farba())

for i in range(10):
    print(random.choice(tvary) , random.randint(3,797),random.randint(3,797),random.randint(3,797),random.randint(3,797),nahodná_farba(),file=ftvary)

ftvary = open("tvary.txt", "r")
for i in range(10):
    riadok = ftvary.readline()
    tvar, xz, yz, xk, yk, farba = riadok.split()

    if tvar == "o":
        canvas.create_oval(xz,yz,xk,yk,fill=farba)
    
    if tvar == "r":
        canvas.create_rectangle(xz,yz,xk,yk,fill=farba)
    
    if tvar == "l":
        canvas.create_line(xz,yz,xk,yk,fill=farba)
    

ftvary.close()
tk.mainloop()