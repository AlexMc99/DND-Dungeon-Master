from tkinter import *
from PIL import ImageTk, Image
import itertools
import random

root = Tk()
root.geometry("1200x819")

image = Image.open("C:\\Users\\bhkal\\Desktop\DND\dnd_table.jpg")
background_image = ImageTk.PhotoImage(image)
background_label = Label(root, image = background_image)
background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

dice_label = Label(root, text = '', font = ('Helvetica', 260))

def roll_dice():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    print(f'{random.choice(dice)} {random.choice(dice)}')
    dice_label.configure(text = f'{random.choice(dice)} {random.choice(dice)}')
    dice_label.pack()

button = Button(root, text = 'Roll Dice', command = roll_dice)
button.pack()

root.mainloop()
