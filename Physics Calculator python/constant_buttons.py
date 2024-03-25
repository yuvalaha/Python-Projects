from tkinter import Button, Label
from functools import partial
FONT = ("Ariel", 14, "bold")
BUTTON_COLOR = "Gold"
BG = "#007FFF"
FG= "red"

class Constant_Buttons:
    def __init__(self, root):
        
        # creating labels and buttons of the constants
        
        # creating pi label and button
        self.pi_label = Label(root,fg=FG, text="", width=30, background=BG, font=FONT)
        self.pi_label.grid(row=3, column=1)
        self.pi_button = Button(text="π", font=FONT,
                                background=BUTTON_COLOR, command=partial(self.show_constant, self.pi_label, "3.14159"))
        self.pi_button.grid(row=3, column=0)

        # creating e label and button
        self.e_label = Label(root,fg=FG, text="", width=30, background=BG, font=FONT)
        self.e_label.grid(row=4, column=1)
        self.e_button = Button(text="e(exp)", font=FONT,
                               background=BUTTON_COLOR, command=partial(self.show_constant, self.e_label, "2.71828"))
        self.e_button.grid(row=4, column=0, pady=20)

        # creating g label and button
        self.g_label = Label(root,fg=FG, text="", width=30, background=BG, font=FONT)
        self.g_label.grid(row=5, column=1)
        self.g_button = Button(text="g", font=FONT,
                               background=BUTTON_COLOR, command=partial(self.show_constant, self.g_label, "9.81 m/s²"))
        self.g_button.grid(row=5, column=0, pady=20)

        # creating G label and button
        self.big_g_label = Label(root,fg=FG, text="", width=30, background=BG, font=FONT)
        self.big_g_label.grid(row=6, column=1)
        self.big_g_button = Button(text="G", font=FONT, background=BUTTON_COLOR, command=partial(
            self.show_constant, self.big_g_label, "6.674×10⁻¹¹ m³*kg⁻¹*s⁻²"))
        self.big_g_button.grid(row=6, column=0, pady=20)

        # creating h label and button
        self.h_label = Label(root,fg=FG, text="", width=30, background=BG, font=FONT)
        self.h_label.grid(row=7, column=1)
        self.h_button = Button(text="h(Planck)", font=FONT, background=BUTTON_COLOR, command=partial(
            self.show_constant, self.h_label, "6.62607015×10⁻³⁴ J*Hz⁻¹"))
        self.h_button.grid(row=7, column=0, pady=20)

        # creating hbar label and button
        self.h_bar_label = Label(root,fg=FG, text="", width=30, background=BG, font=FONT)
        self.h_bar_label.grid(row=8, column=1)
        self.h_bar_button = Button(text="ħ", font=FONT, background=BUTTON_COLOR, command=partial(
            self.show_constant, self.h_bar_label, "1.054571817×10⁻³⁴ J*s"))
        self.h_bar_button.grid(row=8, column=0, pady=20)

        # creating c speed of light label and button
        self.c_label = Label(root,fg=FG, text="", width=30, background=BG, font=FONT)
        self.c_label.grid(row=9, column=1)
        self.c_button = Button(text="c", font=FONT, background=BUTTON_COLOR, command=partial(
            self.show_constant, self.c_label, "299,792,458 m/s"))
        self.c_button.grid(row=9, column=0, pady=20)

        # creating μ₀ label and button
        self.μ_label = Label(root,fg=FG, text="", width=30, background=BG, font=FONT)
        self.μ_label.grid(row=10, column=1)
        self.μ_button = Button(text="μ₀", font=FONT, background=BUTTON_COLOR, command=partial(
            self.show_constant, self.μ_label, "1.25663706212*10⁻⁶ N/A²"))
        self.μ_button.grid(row=10, column=0, pady=20)

        # creating K(b) label and button
        self.k_label = Label(root,fg=FG, text="", width=30, background=BG, font=FONT)
        self.k_label.grid(row=11, column=1)
        self.k_button = Button(text="k", font=FONT, background=BUTTON_COLOR, command=partial(
            self.show_constant, self.k_label, "1.38*10⁻²³ J/K"))
        self.k_button.grid(row=11, column=0, pady=20)

        # creating e(electron) label and button
        self.electron_label = Label(root,fg=FG, text="", width=30, background=BG, font=FONT)
        self.electron_label.grid(row=12, column=1)
        self.electron_button = Button(text="electron charge", font=FONT, background=BUTTON_COLOR, command=partial(
            self.show_constant, self.electron_label, "1.60217663 × 10⁻¹⁹ c"))
        self.electron_button.grid(row=12, column=0, pady=20)

        # creating electron mass label and button
        self.electron_mass_label = Label(root,fg=FG, text="", width=30, background=BG, font=FONT)
        self.electron_mass_label.grid(row=13, column=1)
        self.electron_mass_button = Button(text="electron mass", font=FONT, background=BUTTON_COLOR, command=partial(
            self.show_constant, self.electron_mass_label, "9.1093837  × 10⁻³¹ kg"))
        self.electron_mass_button.grid(row=13, column=0, pady=20)
        
        
        # creating epsilon0 label and button
        self.epsilon0_label = Label(root,fg=FG, text="", width=30, background=BG, font=FONT)
        self.epsilon0_label.grid(row=14, column=1)
        self.electron_mass_button = Button(text="ε₀", font=FONT, background=BUTTON_COLOR, command=partial(
            self.show_constant, self.epsilon0_label, "8.854187  × 10⁻¹² F/m"))
        self.electron_mass_button.grid(row=14, column=0, pady=20)
        
        

    def show_constant(self, label, const):
        label.config(text=const)
