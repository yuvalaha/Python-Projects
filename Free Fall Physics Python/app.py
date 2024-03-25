import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from math import sqrt
from art import logo


# ----------------------------------- Constants -----------------------------------


GRAVITY_CONSTANT = 9.81  # m/s²


# ---------------------------- Free Fall Motion Formula ---------------------------

# Free fall (Y axis)

# v₀ - initial velocity (in our case the initial speed is 0)
# t - time
# a - acceleration (in our case the acceleration is the gravity constant g)


# Y = v₀ * t + 1/2 * a * t²

# ----------------- Calculate the time when the distance is given -----------------

# The function receive user answer - (yes = insert distance in meters, no = insert distance in km) and the distance. the function return time (in seconds) until falling to the ground
# def calculate_time_until_fall(user_answer, distance):

#     # The formula of free fall (if user enter "yes" calculation with meter if the user enters "no" we multiply distance by 1000 because he sent the units in km)
#     distance = distance * 1000 if user_answer == "no" else distance
#     time_until_fall = sqrt(2 * distance) / \
#         GRAVITY_CONSTANT


# ------------------------- Graph of Free falling motion --------------------------

print(logo)

GRAVITY_CONSTANT = 9.81  # m/s²


# The user enters the height he wants to check
height = float(input("Hello And Welcome to the Free Fall Simulator\nPlease enter the height(meters) of an object, and I will tell you how long it will take for it to fall to the ground: "))

# Calculate how long it will take for an object to fall to the ground.
time_until_fall = sqrt(2 * height / GRAVITY_CONSTANT)

# Initialize function. Data that the line will contain (x, y)


def init():
    line.set_data([], [])
    return line,

# The main animation graph


def animate(i, time_until_fall):
    
    # Calculate the time until the object falls to the ground
    fall_time = sqrt(2 * height / GRAVITY_CONSTANT)

    # Create discrete time points as the object falls

    # Creating a list of 100 points with equal time intervals from t=0 to t=time_until_fall
    discrete_time_points = np.linspace(0, fall_time, 100)

    # Using the formula for calculating free fall to obtain the list of heights
    heights_list = [(1/2) * t ** 2 *
                    GRAVITY_CONSTANT for t in discrete_time_points]
    # Reverses the list to start the fall from the peak height
    heights_list.reverse()

    # Create the index of every frame (between 0 to 100)
    frame_index = int(i % len(discrete_time_points))

    # Building the graph - Draws the graph each time from 0 to the current frame index
    line.set_data(discrete_time_points[frame_index],
                heights_list[frame_index])

    # Stop drawing if we complete one cycle
    if frame_index == len(discrete_time_points) - 1:
        anim.event_source.stop()

    return line,


# Creating the graph
fig = plt.figure("Free Fall")

# The axis values
axis = plt.axes(xlim=(0, time_until_fall+2),
                ylim=(0, height + 200))

# Use blue circles as markers for the object
line, = axis.plot([], [], 'yo', ms=12)

# The axis labels and graph title
plt.title("Free Fall Simulator")
plt.xlabel("Time (Seconds)")
plt.ylabel("Height (Meters)")

# Call the main animation function
anim = FuncAnimation(fig, animate, fargs=(time_until_fall,), init_func=init,
                    frames=1000, interval=40, blit=True)  # Adjust interval for animation speed

# Displays the graph
#         x    y             Text of time until fall in the graph
plt.text(3.5, 600, f"Time until fall:{round(time_until_fall, 3)} seconds")

plt.show()
