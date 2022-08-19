# Group Exercises 1

# Teammates: Luke Zerrer, Lance Wong

# Problem 3 (25 pts) - Perfect Numbers

#  A number is perfect if it is equal to the
#  sum of its factors (except itself, but including 1).
#  For example, 28 (with factors 1,2,4,7,14) is perfect
#  because 28 = 1+2+4+7+14. Write a Python program to
#  determine if a number is perfect. Try to make your program
#  as efficient as possible by reducing
#  the number of tests required.

#  Save your program in a file problem3.py.
factors = []
total = 0
numb  = int(input("Please input a integer: "))
for x in range(1, numb):
    if ((numb % x) == 0):
        # print(x)
        factors.append(x)
        total = total + x
if (total == numb):
    print("The number", numb,  " is perfect")
# print("factors: ", factors)
# print("total: ", total)
else:
    print("The number", numb, "is not perfect ")
        

