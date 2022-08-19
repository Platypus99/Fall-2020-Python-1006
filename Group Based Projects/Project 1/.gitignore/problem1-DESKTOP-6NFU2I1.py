# Group Exercises 1

# Teammates: Luke Zerrer, Lance Wong

# Problem 1 - Paint 

# Write a program that estimates how much paint is
#  needed to paint a rectangular room. Assume that
#  the room has no windows and no doors, and that
#  the floor does not have to be painted. Your program
#  should read in the height, width, and length
#  dimensions of the room in centimeters (cm). It
#  should then print out the amount of paint
#  needed in liters. Assume that 2.5 liters are needed
#  to paint a surface area of 10 m2.
 
 
# Input dimensions
height = float(input("Please input the height of the room in cm: "))
width = float(input("Please input the width of the room in cm: "))
length = float(input("Please input the length of the room in cm: "))
# room area
ceiling_area = (width * length)
wall_area = (width * height * 2 + length * height * 2)
room_area = float(ceiling_area + wall_area)
# paint conversion
paint_needed = room_area * 2.5 / 100000
print("You will need ", paint_needed, " cans of paint.")

