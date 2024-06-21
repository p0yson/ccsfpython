'''
Program: student_info.py

Programmer: Insert your name

Date: 06/10/2024

Description:  The program displays student basic information and calculates how many credits are needed to graduate.

'''

#students name input variable
student_name = input('Enter student name:')
#degree input variable
degree_program = input('Enter degree program:')
#credits for degree stored as integer input variable
credits_degree = int(input('Enter credits required for degree:'))
#credits taken stored as integer input variable
credits_taken = int(input('Enter credits required for degree:'))

#calculation for credits left
credits_left = credits_degree - credits_taken

#student name output
print("This student's name is", student_name)
#degree name output
print("The degree program is", degree_program)
#credits required and taken output
print("The program requires", credits_degree, "and they have taken", credits_taken, "so far")
#credits left output
print("This means there are", credits_left, "left to take")