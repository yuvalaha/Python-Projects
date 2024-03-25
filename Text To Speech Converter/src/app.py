from gtts import gTTS
import os
from tkinter import *


# Main window
root = Tk()
root.title("Text to Audio")
# Creating Canvas
canvas = Canvas(root, width=400, height=300)
canvas.pack()

def text_to_speech():
    
    # Get the text from the Entry
    text = entry.get()
    
    # Set language english
    language = 'en'
    
    # Creating the audio file
    output = gTTS(text=text, lang=language, slow=False)
    output.save("file_output.mp3")
    os.system("start file_output.mp3")    

# Creating Entry(input)
entry = Entry(root, width=27)
canvas.create_window(200, 160, window=entry)

# Creating Button
button = Button(text="Start", command=text_to_speech)
canvas.create_window(200, 230, window=button)

root.mainloop()

    
