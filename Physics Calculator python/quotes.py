import pandas
import random
from tkinter import Button, Label
from functools import partial

FONT = ("Ariel", 12, "bold")
SMALL_FONT = ("Ariel", 10, "bold")
FG= "brown"
BUTTON_COLOR = "Gold"
BG ="#007FFF"

class Quotes:
    def __init__(self, root):
        self.quote_label = Label(text="", font=FONT, width=80, fg=FG,background=BG)
        self.quote_label.grid(row=2, column=5, sticky="w")
        self.author_label = Label(text="", font=SMALL_FONT, width=20, fg=FG,background=BG)
        self.author_label.grid(row=3, column=5)
        self.data = pandas.read_csv("famous_quotes.csv")
        self.quote_button = Button(text="Scientific Quotes", font=("Ariel", 13, "bold"), command=partial(
            self.create_quote), width=30, background=BUTTON_COLOR)
        self.quote_button.grid(row=1, column=5)

    def create_quote(self):
        
        # taking random number and choose a quote and author
        self.rand_number = random.randint(0, 9)
        self.quote = self.data["Quotte"][self.rand_number]
        self.author = self.data["Author"][self.rand_number]
        
        # creating label of quotes and authors
        self.quote_label.config(text=self.quote)
        self.author_label.config(text=self.author)
