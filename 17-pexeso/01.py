import tkinter as tk ,random

root =tk.Tk()
root.title("pexeso")

grid_size = 4
num_pairs = (grid_size **2) // 2

card_values = list(range(1, num_pairs + 1)) * 2
random.shuffle(card_values)

flipped_cards = []
flipped_buttons = []
matched_cards = []

def flip_card(i, j):
    if(i,j) in matched_cards or (i,j) in flipped_cards:
        return
    
    button = buttons[i][j]
    button.config(text=str(card_values[i * grid_size + j]), state = "disabled")

    flipped_cards.append((i,j))
    flipped_buttons.append(button)
    
    if len(flipped_cards) == 2:
        check_match()

def check_match():
    if card_values[flipped_cards[0][0] * grid_size + flipped_cards[0][1]] == \
       card_values[flipped_cards[1][0] * grid_size + flipped_cards[1][1]]:
        matched_cards.extend([flipped_cards[0], flipped_cards[1]])
        reset_flipped_cards(True)
    else:
        root.after(500, reset_flipped_cards, False)

def reset_flipped_cards(is_match):
    for button in flipped_buttons:
        if not is_match:
            button.config(text="", state="normal")
    flipped_cards.clear()
    flipped_buttons.clear()

buttons = []
for i in range(grid_size):
    row = []
    for j in range(grid_size):
        button  = tk.Button(root,text="", width=10 , height=4,
                            command=lambda i=i, j=j: flip_card(i,j))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

root.mainloop()
