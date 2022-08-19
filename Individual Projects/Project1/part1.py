# Perry Flamer pf2416

# Take-home project 1

# Part 1 - Guessing Game (50 pts)
# In this problem you will implement a simple guessing game.

# First, the program should choose a secret number x between 1 and 10.
# Use the random function in the random module (random.random()) to pick a random number, as illustrated in class. 

# Then, the program should prompt the user to type in a number.
#  If the player guesses x correctly, the program should print a message and terminate.

# Otherwise, the program should print a hint and then ask the user for another guess:  

# if the difference between x and the guess is greater than 5, the program prints ‘not even close’.
# if the difference between x and the guess is between 3 and 5 (inclusive), the program prints ‘close’.
# if the difference between x and the guess is less than 3, the program prints ‘almost there’.
# The program should repeat asking the user for another
# input until the user guesses correctly or until there were five incorrect guesses.
# The program should keep track of the number of guesses.
#  If the user cannot guess x in his fifth guess, the program informs her that the game is lost and quits.

# Your program should be in a single file 
import random

num = random.random()
num1 = num * 10
num2 = num1 + 1 
num3 = int(num2)
print(num3)

user_number = int(input("Enter a number "))
diff = abs(num3 - user_number)
# print (diff)
count = 1

    
while not(user_number == num3):
    count = count + 1
    if count  == 6:
        break
    
    if diff > 5:
            print('not even close')
    elif (3 <= diff and diff <= 5):
        print('close')
    elif diff < 3:
        print ('almost there')
    
    user_number = int(input("Please enter another number "))
    diff = abs(num3 - user_number)
    
if (user_number == num3):
    print("You guessed correctly, the number was", user_number )  
else:   
    print("You have lost the game")