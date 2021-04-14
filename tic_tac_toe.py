from tkinter import *
from tkinter import messagebox

GAME_TITLE = "Tic-Tac-Toe"
MESSAGE_X_WINS = "Congratulations! X Wins"
MESSAGE_O_WINS = "Congratulations! O Wins"
MESSAGE_DRAW = "It's a DRAW!"

root = Tk()
root.title(GAME_TITLE)

clicked = True
count = 0


def disable_all_buttons():
    """Disable all buttons when the game ends"""
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


def make_buttons_red():
    """Makes the buttons red when draw"""
    b1.config(bg="red")
    b2.config(bg="red")
    b3.config(bg="red")
    b4.config(bg="red")
    b5.config(bg="red")
    b6.config(bg="red")
    b7.config(bg="red")
    b8.config(bg="red")
    b9.config(bg="red")


def make_buttons_green(button_one, button_two, button_three):
    """Makes the buttons green when win"""
    button_one.config(bg="green")
    button_two.config(bg="green")
    button_three.config(bg="green")


def show_win_message(sign):
    messagebox.showinfo(GAME_TITLE, MESSAGE_X_WINS if sign == "X" else MESSAGE_O_WINS)


def check_if_won(sign):
    """Check who wins the game"""
    global winner
    winner = False

    # Rows check
    if b1["text"] == sign and b2["text"] == sign and b3["text"] == sign:
        winner = True
        make_buttons_green(b1, b2, b3)
        show_win_message(sign)
        disable_all_buttons()
    elif b4["text"] == sign and b5["text"] == sign and b6["text"] == sign:
        winner = True
        make_buttons_green(b4, b5, b6)
        show_win_message(sign)
        disable_all_buttons()
    elif b7["text"] == sign and b8["text"] == sign and b9["text"] == sign:
        winner = True
        make_buttons_green(b7, b8, b9)
        show_win_message(sign)
        disable_all_buttons()
    # Columns check
    elif b1["text"] == sign and b4["text"] == sign and b7["text"] == sign:
        winner = True
        make_buttons_green(b1, b4, b7)
        show_win_message(sign)
        disable_all_buttons()
    elif b2["text"] == sign and b5["text"] == sign and b8["text"] == sign:
        winner = True
        make_buttons_green(b2, b5, b8)
        show_win_message(sign)
        disable_all_buttons()
    elif b3["text"] == sign and b6["text"] == sign and b9["text"] == sign:
        winner = True
        make_buttons_green(b3, b6, b9)
        show_win_message(sign)
        disable_all_buttons()
    # Diagonals check
    elif b1["text"] == sign and b5["text"] == sign and b9["text"] == sign:
        winner = True
        make_buttons_green(b1, b5, b9)
        show_win_message(sign)
        disable_all_buttons()
    elif b3["text"] == sign and b5["text"] == sign and b7["text"] == sign:
        winner = True
        make_buttons_green(b3, b5, b7)
        show_win_message(sign)
        disable_all_buttons()

    # Check if draw
    if count == 9 and winner is False:
        make_buttons_red()
        messagebox.showinfo(GAME_TITLE, MESSAGE_DRAW)
        disable_all_buttons()


def button_click(button):
    global clicked, count
    if button["text"] == " " and clicked is True:
        button["text"] = "X"
        clicked = False
        count += 1
        check_if_won(button["text"])
    elif button["text"] == " " and clicked is False:
        button["text"] = "O"
        clicked = True
        count += 1
        check_if_won(button["text"])
    else:
        button.config(bg="red")
        messagebox.showerror("Tic-Tac-Toe", "The box is already filled!\nPick another box!")
        button.config(bg="SystemButtonFace")


# Starts the game again
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0

    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: button_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: button_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: button_click(b3))
    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: button_click(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: button_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: button_click(b6))
    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: button_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: button_click(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: button_click(b9))
    # Grid the buttons
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


my_menu = Menu(root)
root.config(menu=my_menu)

options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="New Game", command=reset)

reset()
root.mainloop()