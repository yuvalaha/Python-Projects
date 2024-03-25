from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from math import sqrt
from art import logo
import numpy as np


# ----------------------------------- Constants -----------------------------------

print(logo)
GRAVITY_CONSTANT = 9.81  # m/s²

# ---------------------------- Free Fall Motion Formula ---------------------------

# Free fall (Y axis)

# v₀ - initial velocity (in our case the initial speed is 0)
# t - time
# a - acceleration (in our case the acceleration is the gravity constant g)


# Y = v₀ * t + 1/2 * a * t²

# ----------------- Calculate the time when the distance is given -----------------

# # The function receive user answer - (yes = insert distance in meters, no = insert distance in km) and the distance. the function return time (in seconds) until falling to the ground
# def calculate_time_until_fall(user_answer, distance):

#     # The formula of free fall (if user enter "yes" calculation with meter if the user enters "no" we multiply distance by 1000 because he sent the units in km)
#     distance = distance * 1000 if user_answer == "no" else distance
#     time_until_fall = sqrt(2 * distance) / \
#         GRAVITY_CONSTANT

#     # return time until the object land in the ground
#     return time_until_fall


# # ------------------------- Graph of Free falling motion First Option --------------------------
# def free_fall_graph(time_until_fall, distance):
#     # Creating intervals of 0.001 seconds
#     time_intervals = 0.001

#     # Creating list of times divided to intervals. for example if time_until_fall= 3 seconds --> time_list = [0.001, 0.002, 0.003, 0.04, ..........2.999, 3] total of 3001 points in the x axis
#     time_list = [
#         t*time_intervals for t in range(int(time_until_fall/time_intervals)+1)]

#     # Creating list of distances using the free fall formula divided to intervals. for example if time_until_fall= 3 seconds --> distance_list = [1/2 * (0.01)² * g, .......... ,1/2 * 3² * g] total of 3001 points in the y axis
#     #                                                                                                                                                     t²                           t²

#     distance_list = [1/2 * time ** 2 * GRAVITY_CONSTANT for time in time_list]

#     # Reverse the order of the distance list
#     distance_list.reverse()

#     # Creating the plot   
    
#     my_plot.figure("Free Fall") 

#     #              x axis       y axis
#     my_plot.plot(time_list, distance_list)
    
#     # X axis label
#     my_plot.xlabel("Time (seconds) ")
    
#     # Y axis label
#     my_plot.ylabel("Height (meters) ")
    
#     # Title of the graph
#     my_plot.title("Free Fall Motion")
    
#     my_plot.show()


# # The user insert his answers
# user_answer = input("Hello and welcome to Free Fall simulator!!!\nIf you want to insert the distance in units of meters write yes.\n"
#                     "if you want to insert the distance in kilometer please write no: ")
# distance = float(input("Please enter the distance: "))
# time_until_fall = calculate_time_until_fall(user_answer, distance)
# print(f"Time until fall is: {time_until_fall} seconds")
# calculate_time_until_fall(user_answer, distance)
# free_fall_graph(time_until_fall, distance)
