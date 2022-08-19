# Perry Flamer pf2416

# Take-home project 1

# Part 2 - Inverse guessing game (50 pts) 

# Let’s inverse the roles in the guessing game.
#  This time, the player chooses a secret number
#  between 1 and 10 (in their mind) that the computer
#  must guess. For this purpose, the computer suggests
#  a number and the player indicates if it is 1) too big, 2) too small or 3) correct.
#  The player's response should be read as user input. If the number is correct, 
#  the program should terminate. Otherwise the computer will ask another number repeatedly. The
 # computer only has three attempts to guess the right number.

# Write the inverse guessing game as a new Python program in the file part2.py.
#  Before starting to program, make sure to plan out your algorithm (maybe on paper).

# Hint: The strategy the compute should follow is similar to Binary Search.
#  It's okay if the computer always guesses 5 as the first number although
#  that will make some numbers "unreachable". You may also select a random number as
#  the first number, but you should still use the steps of Binary Search to guess the next numbers.

x = int(input("Enter an number between 1 and 10: "))

while not (x <= 10 and x >0):
    x = int(input("Invalid entry, enter a number between 1 and 10: "))
    
li = [1,2,3,4,5,6,7,8,9,10]
left = 0 
right = len(li)-1
mid = (left + right) // 2
counter = 1
print('Is the number', li[mid], 'correct or is it, too big, or too small?')
print("Try ", counter, "of 3")
response = input()
while not (response == 'correct' or response == 'too big' or response == 'too small'):
    print('Invalid entry, is the number', li[mid], 'correct or is it, too big, or too small?')
    print("Try ", counter, "of 3")
    response = input()
# print(response)


while not (response == 'correct' or counter >=3):
   
    # print('incorrect')
    if response == 'too big':
        # left = 0
        right = mid-1
    elif response == 'too small':
        left = mid+1
        # right = len(li)-1
        
    mid = (left + right) // 2  
    # print("Left is: ", li[left], "Right is: ", li[right], 'Mid is', li[mid])
    counter = counter +1
    print('Is the number', li[mid], 'correct or is it, too big, or too small')
    print("Try ", counter, "of 3")
    response = input()
    while not (response == 'correct' or response == 'too big' or response == 'too small'):
        print('Invalid entry, is the number', li[mid], 'correct or is it, too big, or too small?')
        print("Try ", counter, "of 3")
        response = input()

# print("I think the number is ", li[mid])
    
    

if response == 'correct':
    print('Computer guessed correctly, the number is ', li[mid] )
elif (response == 'too small' and (li[mid]==9)):
    print("I believe the number is 10 but am out of tries so I cannot confirm :) ")
elif (response == 'too small' and (li[mid]==3)):
    print("I believe the number is 4 but am out of tries so I cannot confirm :) ")    
elif (response == 'too small' and (li[mid]==6)):
    print("I believe the number is 7 but am out of tries so I cannot confirm :) ")   

if counter >=3:
    print("The computer has used up 3 guesses")

