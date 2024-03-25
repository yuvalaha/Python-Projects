from tkinter import *
import math

# ---------------------------------- Constants and Global variables ---------------------------------
# Constants
BG_COLOR = "#87CEFA"
SMALL_FONT = ("ariel", 13, "bold")
BIG_FONT = ("ariel", 40, "bold")
STARTING_TEXT = "00:00"
IMAGE_POSITION = 160, 111.5
TEXT_POSITION = 160, 130
WORKING_MINUETS = 0.1
SHORT_BREAK = 0.05
LONG_BREAK = 15
WORK_COLOR = "#E3CF57"
SHORT_BREAK_COLOR = "#CD3333"
LONG_BREAK_COLOR = "#66CD00"

# Global variables
reps = 1
check_marks_count = 1
timer = None

# ---------------------------------- Main window and Canvas ---------------------------------

# Creating the main window and changing the title of our window
window = Tk()
window.config(padx=100, pady=140, bg=BG_COLOR)
window.title(string="Pomodoro timer")


# Creating the canvas
canvas = Canvas(width=320, height=223, highlightthickness=0, bg=BG_COLOR)
pomo_img = PhotoImage(file="pomodoro.png")
canvas.create_image(IMAGE_POSITION, image=pomo_img)
timer_text = canvas.create_text(
    TEXT_POSITION, text=STARTING_TEXT, font=BIG_FONT, fill="white")
canvas.grid(row=1, column=1)

# ------------------------------------------ Labels ------------------------------------------

# Creating check marks
check_marks = Label(text="", fg="light green", font=SMALL_FONT, bg=BG_COLOR)
check_marks.grid(row=3, column=1)

# Creating the Timer label
timer_label = Label(text="Timer", font=BIG_FONT, fg="light green", bg=BG_COLOR)
timer_label.grid(row=0, column=1, pady=30)


# --------------------------------- Start and Reset functions --------------------------------

# Creating the timer countdown function
def count_down(timer_count):

    global reps
    global timer

    # Converting timer_count to minuets and seconds
    count_min = math.floor(timer_count/60)
    count_sec = round(timer_count % 60)
    # Change the timer text to format xx:xx
    timer_new_text = ""
    if count_sec < 10:
        timer_new_text = f"{count_min}:0{count_sec}"
    else:
        timer_new_text = f"{count_min}:{count_sec}"

    # Update the timer text
    canvas.itemconfig(timer_text, text=timer_new_text)
    if timer_count >= 0:
        timer = window.after(1000, count_down, timer_count - 1)
    else:
        start_timer()


# Function that calls the countdown function and it is starting to work after the start button is been pressed
def start_timer():
    global reps
    global check_marks_count
    
    work_sec = 60 * WORKING_MINUETS
    short_break = 60 * SHORT_BREAK
    long_break = 60 * LONG_BREAK
    if reps % 8 == 0:
        count_down(long_break)
        timer_label.config(text="Long Break", fg=LONG_BREAK_COLOR)
        
        # Update the check mark label after work session
        check_marks.config(text=("✔"*check_marks_count))
        check_marks.grid(row=3, column=1)
        check_marks_count += 1

    elif reps % 2 == 0:
        count_down(short_break)
        timer_label.config(text="Short Break", fg=SHORT_BREAK_COLOR)
        # Update the check mark label after work session
        check_marks.config(text=("✔"*check_marks_count))
        check_marks.grid(row=3, column=1)
        check_marks_count += 1

        
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=WORK_COLOR)

    reps += 1

# Reset timer function

def reset_timer():
    global check_marks_count, reps
    
    window.after_cancel(timer)
    timer_label.config(text="Timer",fg="light green")
    check_marks.config(text="")
    check_marks_count = 1
    reps = 1
    canvas.itemconfig(timer_text,text=STARTING_TEXT)

    

# ----------------------------------------- Buttons -------------------------------------

# Creating the start and reset buttons and all the labels

# Start buttons
start_button = Button(text="Start", font=SMALL_FONT, command=start_timer)
start_button.grid(row=2, column=0, pady=15, padx=15)

# Reset Button
reset_button = Button(text="Reset", font=SMALL_FONT, command=reset_timer)
reset_button.grid(row=2, column=2, pady=15, padx=15)


window.mainloop()
