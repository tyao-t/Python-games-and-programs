import tkinter as tk
from card import Card

class graphicsDisplay:
    def __init__(self):
        pass

isCardSelected = False
selectedCard = 0

def selectCard(num):
    global isCardSelected, selectedCard
    isCardSelected = True
    selectedCard = num

def play_cards(num):
    global hand, buttons
    print("You played: ", end='')
    print(hand[num].full_name)
    hand.remove(hand[num])
    blitHand()

def confirm():
    if isCardSelected:
        play_cards(selectedCard)

def cancel():
    global isCardSelected
    isCardSelected = False;

root = tk.Tk()
HEIGHT = 500
WIDTH = 600

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='bg.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

button_confirm = tk.Button(root, text = "Confirm", command=confirm)
button_confirm.place(relx=0.45, rely=0.45, relwidth = 0.1, relheight=0.1)
button_cancel = tk.Button(root, text = "Cancel", command=cancel)
button_cancel.place(relx=0.65, rely=0.65, relwidth = 0.1, relheight=0.1)
hand = [Card("ATT"), Card("DOD")]
buttons = []
count = 0
def blitHand():
    global buttons
    isCardSelected = False
    for i in range(len(buttons)):
        buttons[i].place_forget()
    buttons = []
    for i in range(len(hand)):
        global count
        button = tk.Button(root, text = hand[i].full_name, command=lambda x=i:selectCard(x))
        buttons.append(button)
    for i in range(len(buttons)):
        buttons[i].place(relx=0.35+i*0.15, rely=0.7, relwidth=0.1, relheight=0.1)

blitHand()
#frame = tk.Frame(root, bg="#80c1ff")
#frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

root.mainloop()
