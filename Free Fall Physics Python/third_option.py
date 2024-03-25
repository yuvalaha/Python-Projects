from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from math import sqrt
from art import logo
import numpy as np
from converter import get_hight_conversion



# ----------------------------------------- Constants -----------------------------------------

print(logo)
GRAVITY_CONSTANT = 9.81  # m/s²

# ----------------------------------------- Free Fall Motion Formula Explanation -----------------------------------------

# Free fall (Y axis)

# v₀ - initial velocity (in our case the initial speed is 0)
# t - time
# a - acceleration (in our case the acceleration is the gravity constant g)


# Height = v₀ * t + 1/2 * a * t²


# # ---------------------------------------- Graph of Free falling motion  -----------------------------------------

# The user enters the unit  of length he would like to use (meters, km, mile , foot, cm, inch, yard ) 
user_answer = input("Hello And Welcome to the Free Fall Simulator\nPlease enter in which unit of length would you like to use: (meters, km, mile , foot, cm, inch, yard): ")
# The user enters a height he wants to check
user_height = float(input("Please enter the height of an object, and I will tell you how long it will take for it to fall to the ground: "))

# Convert the data that the user enters
height = get_hight_conversion(user_answer, user_height)

# Calculate how long it will take for an object to fall to the ground.
time_until_fall = sqrt(2 * height / GRAVITY_CONSTANT)

# Initialize function. data which the line will contain (x, y)


def init():
    line.set_data([], [])
    return line,

# The main animation graph


def animate(i, time_until_fall):
    # Creating a list of 1000 points with equal time intervals from t=0 to t=time_until_fall
    time_list = list(np.linspace(0, time_until_fall, 1000))

    # Using the formula for calculating free fall to obtain the list of heights
    heights_list = [(1/2) * t ** 2 * GRAVITY_CONSTANT for t in time_list]

    # Reverses the list to start the fall from the peak height
    heights_list.reverse()

    # Initialize frames per one cycle (im my case 1000 frames)
    frames_per_cycle = len(time_list)

    # Create the index of every frame (between 0 to 1000)
    frame_index = int(i % frames_per_cycle)

    # Building the graph - Draws the graph each time from 0 to the current frame index
    line.set_data(time_list[:frame_index], [heights_list[:frame_index]])

    # Stop drawing if we complete one cycle
    if frame_index == frames_per_cycle - 1:
        anim.event_source.stop()

    return line,


# Creating the graph
fig = plt.figure("Free Fall")

# The axis values
axis = plt.axes(xlim=(0, time_until_fall+2),
                ylim=(0, height+200))

# The axis labels and graph title
plt.xlabel("Time (Seconds)")
plt.ylabel("Height (Meters)")
plt.title("Free Fall Simulator")

# initializing a line variable
line, = axis.plot([], [], 'yo',lw=5)

# Call the main animation function
anim = FuncAnimation(fig, animate, fargs=(time_until_fall,),
                     init_func=init, frames=1000, interval=1, blit=True)


# Displays the graph
plt.show()

