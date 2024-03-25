from constant_buttons import Constant_Buttons
from labels import Labels
from converter import Button_Converter
from tkinter import *
from quotes import Quotes
FONT = ("Ariel", 18, "bold")
BG = "#007FFF"

window = Tk()
window.config(bg=BG)
window.title(string="Physics Calculator")
window.geometry('2540x1200')

calculator_labels = Labels(window)
calculator_constant_buttons = Constant_Buttons(window)
calculator_entrys = Button_Converter(window)
calculator_quoets = Quotes(window)

# canvas = Canvas(width=300, height=300)
# einstein_photo = PhotoImage(file="f_m_a.png")
# canvas.create_image(100, 100, image=einstein_photo)
# canvas.grid(row=10,column=4)

window.mainloop()


# To do list:
# 1. add more quotes
# 2. add two more features to the project
