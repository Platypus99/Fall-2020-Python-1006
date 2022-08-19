# Group Exercises 2

# Teammates: Luke Zerrer, Lance Wong

# Problem 1 (30 pts) - Pig Latin 

# Pig Latin is a language game in which words are altered according to certain rules. 
# To make the pig latin form of an English word, the initial consonant sound is
#  transposed to the end of the word, and an "ay" is affixed. Specifically, there are two rules: 

# If a word begins with a vowel, append "yay" to the end of the word. 
# If a word begins with a consonant, remove all the consonants from the
#  beginning up to the first vowel and append them to the end of the word.
#  Finally, append "ay" to the end of the word. The letter "y" counts
#  as a consonant. If there are no vowels, simply append "ay" to the end of the word. 
# For example: 

# dog => ogday
# python => onpythay
# scratch => atchscray
# is => isyay
# apple => appleyay
# (a) In the file problem1.py, write a function

# def piggify(word):
#     ...
# that takes an input String word as its parameter and returns
#  a string containing the pig latin translation of the word. You
#  can assume that the input is always a lower-case string (no input verifdogication is necessary). 

# Hints: Use indexing and slicing. You might also want to use a string
#  of vowels and then use the in operator to check if a letter is a vowel.

# vowels = 'aeiou'
# (b) In the same file, write a program that repeatedly prompts the user
#  to input a new word and then prints the pig latin translation
# of the word (by calling the piggify function). When the user types
# a single period, the program should quit. 
    




#If a word begins with a vowel, append "yay" to the end of the word. 

#If a word begins with a consonant, remove all the consonants from the beginning up to the first vowel and append them to the end of the word. Finally, append "ay" to the end of the word. The letter "y" counts as a consonant. If there are no vowels, simply append "ay" to the end of the word. 

#Defining function with in/else statements to match the specifications of the piglatin language
def piggify(word):
    vowels = "aeiou"
    counter = 0
    if word[0] in vowels:
        word = word + "yay"
    else:
        for x in range(len(word)):
            if word[x] in vowels:
                word = word[x:]+word[:x]+"ay"
                counter += 1
                break
        if counter == 0:
            word = word + "ay"
    return word
    
            
g = (input("Please input a word to piggify: "))   
if not g =='.':
    while not g =='.':
        print(piggify(g))
        g = (input("Please input a word to piggify: "))
          
# print(g)
# g = piggify(input("Please input a word to piggify: "))


    
    
    
