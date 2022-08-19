# Group Exercises 2

# Teammates: Luke Zerrer, Lance Wong

# Write a function

# def print_box(s):
#    ...
# That prints  out the string s centered, in a box. For example, print_box("Python rocks!") should print.

# ******************
# * Python rocks! *
# ******************

# Make sure this also works for multi-line strings. The multi-line string "Python\nRocks\n!" should
#  be printed like this:

# **********
# * Python *
# * Rocks  *
# *   !    *
# **********
# Write a main program that prompts the user to input a string, and then calls the print_box function to print it.

# Save your program, including the function, in a file problem2.py.


# should return list containing strings for each line
def split_to_strs(s): 
    a = s.split('\n')
    return a

def max_length_str(li):
    max  = 0
    for x in li:
        a = len(x)
        if a > max:
            max = a
    return max

def add_white_spaces(max_length_str, this_str):
    pre = (max_length_str - len(this_str)) // 2
    post = (max_length_str - len(this_str) - pre)
    this_line_str = '* '+' '*pre + this_str + ' '*post+' *'
    return this_line_str

        


def print_box(s):
    s_length = len(s)
    if '\n' in s:
        # print('has many lines')
        li = split_to_strs(s)
        max = max_length_str(li)
        long_stars = '*'*max+'*'*4
        print(long_stars)
        for x in range(len(li)):
            full_line = add_white_spaces(max, li[x])
            print(full_line)
        print(long_stars)
        
    
    else:
        long_stars = '*'*s_length+'*'*4
        stri = '* ' + s + ' *'
        print(long_stars)
        print(stri)
        print(long_stars)


# g = 'hie'
# g = "Python\nRocks\n!" 
z = str(input('Please enter some words: '))
   
g = z.replace('\\n','\n')
print_box(g)

# if s contains '\n':
#     num_lines_to_print(s)
#     split_to_strs('s', num_lines_to_print)
#     max_length_str()
#     # midpoint_each_lin()
#     # add_white_spaces()
#     # add_left_star()
#     # add_right_star()
    
    

    
# def num_lines_to_print(s):
#     count = 1
#     if s contains '\n':         
#         for x in s:
#             if x==('\n'):
#             count +=
#     return count


        
        



   

        
        
