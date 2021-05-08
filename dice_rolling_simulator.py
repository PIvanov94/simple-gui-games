from tkinter import *
import Pillow
import random


root = Tk()
root.geometry("400x400")
root.title("Dice rolling")

BlankLine = Label(root, text="")
BlankLine.pack()

HeadingLabel = Label(root, text="Play the dice!")
fg = "light green"
bg = "dark green"
font = "Helvetica 16 bold italic"
HeadingLabel.pack()

dice = ["die1.png", "die2.png", "die3.png", "die4.png", "die5.png", "die6.png"]



root.mainloop()