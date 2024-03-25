from tkinter import Label
BIG_FONT = ("Ariel", 30, "bold")
SMALL_FONT = ("Ariel", 14, "bold")
FG = "Dark blue"
FG_CONSTANTS = "red"
BG = "#007FFF"


class Labels:
    def __init__(self, root):

        # main label title
        self.main_label = Label(text="Physics Calculator", font=(
            "Ariel", 50, "bold"), bg="lightgreen", width=20, fg=FG)
        self.main_label.grid(row=0, column=0, columnspan=8, padx=750)

        # constant label title
        self.constant_label = Label(
            text="Constants", font=BIG_FONT, fg=FG,bg="#007FFF")
        self.constant_label.grid(row=1, column=0, padx=30, pady=20)

        # unit converter label title
        self.unit_converter = Label(
            text="Unit Converter", font=BIG_FONT, fg=FG,bg="#007FFF")
        self.unit_converter.grid(row=1, column=3, pady=20, padx=200)

        # k/h to m/s label
        self.m_s_label = Label(text="", font=SMALL_FONT,
                               background=BG, fg=FG_CONSTANTS, width=20)
        self.m_s_label.grid(row=2, column=4)

        # m/s to k/h label
        self.k_h_label = Label(text="", font=SMALL_FONT,
                               background=BG, fg=FG_CONSTANTS, width=20)
        self.k_h_label.grid(row=3, column=4)

        # hours to second label
        self.seconds_label = Label(
            text="", font=SMALL_FONT, background=BG, fg=FG_CONSTANTS)
        self.seconds_label.grid(row=4, column=4)

        # seconds to hours label
        self.hours = Label(text="", font=SMALL_FONT, background=BG, fg=FG_CONSTANTS)
        self.hours.grid(row=5, column=4)

        # celsius to fahrenheit label
        self.celsius = Label(text="", font=SMALL_FONT, background=BG, fg=FG_CONSTANTS)
        self.celsius.grid(row=6, column=4)

        # fahrenheit to celsius  label
        self.fahrenheit = Label(text="", font=SMALL_FONT, background=BG, fg=FG_CONSTANTS)
        self.fahrenheit.grid(row=7, column=4)

        # celsius to kelvin
        self.kelvin = Label(text="", font=SMALL_FONT, background=BG, fg=FG_CONSTANTS)
        self.kelvin.grid(row=8, column=4)

        # kelvin to celsius
        self.celsius_k = Label(text="", font=SMALL_FONT, background=BG, fg=FG_CONSTANTS)
        self.celsius_k.grid(row=9, column=4)

        # frequency to wavelength

        # wavelength to frequency
