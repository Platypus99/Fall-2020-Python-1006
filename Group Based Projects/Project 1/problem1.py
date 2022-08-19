# Input dimensions of the room
height = float(input("Please input the height of the room in cm: "))
width = float(input("Please input the width of the room in cm: "))
length = float(input("Please input the length of the room in cm: "))

# room area
ceiling_area = (width * length)
wall_area = (width * height * 2 + length * height * 2)
room_area = float(ceiling_area + wall_area)
# paint conversion
paint_needed = room_area * 2.5 / 100000
print("You will need ", paint_needed, " cans.")

