from entrys import Entrys
from labels import Labels
from tkinter import *
from functools import partial
FONT = "bold"
BUTTON_COLOR = "Gold"


class Button_Converter:
    def __init__(self, root):
        self.root = root
        self.labels = Labels(self.root)
        self.entrys = Entrys(self.root)
        kh_to_m_s = Button(root, background=BUTTON_COLOR, text="k/h to m/s",
                           command=partial(self.calculate, "kh_to_ms"), font=FONT)
        kh_to_m_s.grid(row=2, column=2, padx=15)
        kh_to_m_s = Button(root, background=BUTTON_COLOR, text="m/s to k/h ",
                           command=partial(self.calculate, "ms_to_kh"), font=FONT)
        kh_to_m_s.grid(row=3, column=2, padx=15)

        sec_to_hours = Button(root, background=BUTTON_COLOR, text="seconds to hours ",
                              command=partial(self.calculate, "sec_to_hours"), font=FONT)
        sec_to_hours.grid(row=4, column=2, padx=15)
        hours_to_sec = Button(root, background=BUTTON_COLOR, text="hours to seconds ",
                              command=partial(self.calculate, "hours_to_sec"), font=FONT)
        hours_to_sec.grid(row=5, column=2, padx=15)

        cels_to_fahr = Button(root, background=BUTTON_COLOR, text="celsius to fahrenheit ",
                              command=partial(self.calculate, "cels_to_fahr"), font=FONT)
        cels_to_fahr.grid(row=6, column=2, padx=15)
        fahr_to_cels = Button(root, background=BUTTON_COLOR, text="fahrenheit to celsius",
                              command=partial(self.calculate, "fahr_to_cels"), font=FONT)
        fahr_to_cels.grid(row=7, column=2, padx=15)

        kelvin_to_cels = Button(root, background=BUTTON_COLOR, text="kelvin to celsius ",
                                command=partial(self.calculate, "kelv_to_cels"), font=FONT)
        kelvin_to_cels.grid(row=8, column=2, padx=15)
        cels_to_kelvin = Button(root, background=BUTTON_COLOR, text="celsius to kelvin",
                                command=partial(self.calculate, "cels_to_kelv"), font=FONT)
        cels_to_kelvin.grid(row=9, column=2, padx=15)

#

    def calculate(self, type_of_converstion):
        enterd_data = self.entrys.get_data()
        if type_of_converstion == "kh_to_ms":
            enterd_data["k_h_value"] = round(
                float(enterd_data["k_h_value"]) / 3.6, 3)
            self.labels.m_s_label.config(
                text=f'{enterd_data["k_h_value"]} m/s ')
        elif type_of_converstion == "ms_to_kh":
            enterd_data["m_s_value"] = round(
                float(enterd_data["m_s_value"]) * 3.6, 3)
            self.labels.k_h_label.config(
                text=f'{enterd_data["m_s_value"]} k/h ')
        elif type_of_converstion == "sec_to_hours":
            enterd_data["sec_to_hours_value"] = round(
                float(enterd_data["sec_to_hours_value"]) / 3600, 3)
            self.labels.seconds_label.config(
                text=f'{enterd_data["sec_to_hours_value"]} hours ')
        elif type_of_converstion == "hours_to_sec":
            enterd_data["hours_to_sec_value"] = round(
                float(enterd_data["hours_to_sec_value"]) * 3600, 3)
            self.labels.hours.config(
                text=f'{enterd_data["hours_to_sec_value"]} seconds ')
        elif type_of_converstion == "cels_to_fahr":
            enterd_data["cels_to_fahr_value"] = round(
                float(enterd_data["cels_to_fahr_value"]) * 9/5 + 32, 3)
            self.labels.celsius.config(
                text=f'{enterd_data["cels_to_fahr_value"]} fahrenheit ')
        elif type_of_converstion == "fahr_to_cels":
            enterd_data["fahr_to_cels_value"] = round(
                (float(enterd_data["fahr_to_cels_value"])-32)*5/9, 3)
            self.labels.fahrenheit.config(
                text=f'{enterd_data["fahr_to_cels_value"]} celsius ')
        elif type_of_converstion == "kelv_to_cels":
            enterd_data["kelvin_to_cels_value"] = round(
                float(enterd_data["kelvin_to_cels_value"])-273.15, 3)
            self.labels.kelvin.config(
                text=f'{enterd_data["kelvin_to_cels_value"]} celsius ')
        elif type_of_converstion == "cels_to_kelv":
            enterd_data["cels_to_kelvin_value"] = round(
                float(enterd_data["cels_to_kelvin_value"])+273.15, 3)
            self.labels.celsius_k.config(
                text=f'{enterd_data["cels_to_kelvin_value"]} kelvin ')

        print(enterd_data)
