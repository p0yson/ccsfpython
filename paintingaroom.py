'''
Program:  paint_room.py. 

Programmer: Devon Chavez

Date: 07/10/2024

Description:  The program calculates the amount of paint needed to paint the walls of a room of the given length and width. It assumes that the paint covers 350 square feet per gallon.

'''
# Constants
COVERAGE = 350  #paint covers 350 sq ft/gal
DOOR_AREA = 20  # Area covered by one door
WINDOW_AREA = 15 # Area covered by one window

# Input Section
length = int(input('Enter the length of the room: '))  # Room length
width = int(input("Enter the width of the room: ")) # Room width
height = int(input("Enter the height of the room: "))  # Room height
num_doors = int(input("How many doors are in the room? ")) # Number of doors
num_windows = int(input("How many windows are in the room? "))  # Number of windows   

# Calculation Section
total_sqft = 2 * width * height + 2 * length * height # Total wall area
total_sqft = total_sqft - num_doors * DOOR_AREA - num_windows * WINDOW_AREA # Adjusted wall area subtracting doors and windows
paint_needed = total_sqft / COVERAGE  # Amount of paint needed

# Output Section
print(paint_needed, "gallons of paint are needed to paint a room", width, "feed wide by", length, "feet long by", height, "feet high with", num_doors, "and", num_windows)
