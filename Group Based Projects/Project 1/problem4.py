# Group Exercises 1

# Teammates: Luke Zerrer, Lance Wong

# Problem 4 (25 pts) - k-smallest numbers

# Write a Python program to produce 
# a list of the k-smallest numbers in
#  a list of numbers. For example, if
# li = [1,2,5,4,3,2]
# k=3
# The output should be a list
# [1,2,2]



li = [4,3,3,1,0,2]
k = 3

sorted = []
output = []
if len(li) >= k: # check that the list has k number of values in it
  while len(li) > 0:
      current_min_idx = 0 # restart search of the list from the begining
      for idx in range(len(li)): # find and set current_min_idx to the index of the smallest number in the list
          if li[idx] < li[current_min_idx]:
              current_min_idx = idx
              
      sorted.append(li[current_min_idx]) # while loopimg through the list li in the while loop, place the smallest value of li into a new list called sorted
      li.remove(li[current_min_idx]) # remove the smallest value
# prints the sorted list          
#  print(sorted)

# insert the k smallest numbers from the sorted list into a list called output and then print it
  while k > 0:
      output.append(sorted[0])
      sorted.remove(sorted[0])
      k = k-1
  print(output)
else:
  print("li must be at least {} numbers in length".format( k))


