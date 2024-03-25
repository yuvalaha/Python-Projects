from tkinter import *
SMALL_FONT = ("Ariel", 12, "bold")
ENTRY_BACKGROUND = "#36454F"
FG = "red"

class Entrys:
    
    # creating the converters entrys
    def __init__(self, root):
        self.k_h_entry = Entry(root,font=SMALL_FONT, background=ENTRY_BACKGROUND, fg=FG)
        self.k_h_entry.grid(row=2, column=3, pady=20)
        self.m_s_entry = Entry(root,font=SMALL_FONT, background=ENTRY_BACKGROUND, fg=FG)
        self.m_s_entry.grid(row=3, column=3, pady=20)
        self.sec_entry = Entry(root,font=SMALL_FONT, background=ENTRY_BACKGROUND, fg=FG)
        self.sec_entry.grid(row=4, column=3, pady=20)
        self.hours_entry = Entry(root,font=SMALL_FONT, background=ENTRY_BACKGROUND, fg=FG)
        self.hours_entry.grid(row=5, column=3, pady=20)
        self.celsius_entry = Entry(root,font=SMALL_FONT, background=ENTRY_BACKGROUND, fg=FG)
        self.celsius_entry.grid(row=6, column=3, pady=20)
        self.fahrenheit_entry = Entry(root,font=SMALL_FONT, background=ENTRY_BACKGROUND, fg=FG)
        self.fahrenheit_entry.grid(row=7, column=3, pady=20)
        self.kelvin_entry = Entry(root,font=SMALL_FONT, background=ENTRY_BACKGROUND, fg=FG)
        self.kelvin_entry.grid(row=8, column=3, pady=20)
        self.celsius_k_entry = Entry(root,font=SMALL_FONT, background=ENTRY_BACKGROUND, fg=FG)
        self.celsius_k_entry.grid(row=9, column=3, pady=20)
    
    # getting the values of the entrys that the user entered
    def get_data(self):
        data = {
            "k_h_value": self.k_h_entry.get(),
            "m_s_value": self.m_s_entry.get(),
            "sec_to_hours_value": self.sec_entry.get(),
            "hours_to_sec_value": self.hours_entry.get(),
            "cels_to_fahr_value": self.celsius_entry.get(),
            "fahr_to_cels_value": self.fahrenheit_entry.get(),
            "kelvin_to_cels_value": self.kelvin_entry.get(),
            "cels_to_kelvin_value": self.celsius_k_entry.get(),
            
                    
        }
        
        return data