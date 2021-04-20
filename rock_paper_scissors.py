from random import *
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x400")
root.resizable(0, 0)
root.title("Rock-Paper-Scissors")
root.config(bg="seashell3")

Label(root, text="Rock-Paper-Scissors", font="helvetica 20 bold", bg="seashell2").pack()

user_take = StringVar()
Label(root, text="Choose your destiny!", font="helvetica 20 bold", bg="seashell2").place(x=60, y=70)
Entry(root, font="arial 15", textvariable=user_take, bg="antiquewhite2").place(x=90, y=130)

computer_pick = randint(1, 3)
if computer_pick == 1:
    computer_pick = "rock"
elif computer_pick == 2:
    computer_pick = "paper"
else:
    computer_pick = "scissors"

result = StringVar()


def play():
    user_pick = user_take.get()
    if user_pick == computer_pick:
        result.set("Tie! You both select the same")
    elif user_pick in ("rock", "Rock") and computer_pick == "paper":
        result.set("You lose!")
    elif user_pick in ("rock", "Rock") and computer_pick == "scissors":
        result.set("You win!")
    elif user_pick in ("paper", "Paper") and computer_pick == "rock":
        result.set("You win!")
    elif user_pick in ("paper", "Paper") and computer_pick == "scissors":
        result.set("You lose!")
    elif user_pick in ("scissors", "Scissors") and computer_pick == "rock":
        result.set("You lose!")
    elif user_pick in ("scissors", "Scissors") and computer_pick == "paper":
        result.set("You win!")
    else:
        messagebox.showerror("Rock-Paper-Scissors", "Please select rock, paper or scissors!")
        reset()


def reset():
    result.set("")
    user_take.set("")


Entry(root, font='arial 10 bold', textvariable=result, bg='antiquewhite2', width=50, ).place(x=25, y=250)
Button(root, font='arial 13 bold', text='PLAY', padx=5, bg='seashell4', command=play).place(x=150, y=190)
Button(root, font='arial 13 bold', text='RESET', padx=5, bg='seashell4', command=reset).place(x=140, y=310)

root.mainloop()
