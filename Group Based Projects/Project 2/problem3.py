# Group Exercises 2

# Teammates: Luke Zerrer, Lance Wong

# Problem 3 (40 pts) - Finding Subsequences in DNA Strings
# DNA molecules consist of a sequence of
#  the four nucleotide bases: adenine, thymine, cytosine, and guanine.
#  The nucleotide bases are often abbreviated by
#  their first letter, ATCG) so that DNA is represented as a string
#  of these four letters. A DNA string can be millions of bases long.

# One important problem on DNA strings is substring matching, which is the
#  task of checking whether a shorter substring is contained within a longer
#  string. Obviously, finding a substring in a long string has many
#  interesting applications, but here we will focus on DNA sequences.

# Python strings already provide an s.find(substring) method that
#  returns the index in s at which substring first appears. If the
#  substring does not appear, the method returns -1.
#  For example: "C".find("CGCG") returns 2, but "ATCGCGTACT".find("CGAT") returns -1. 

# (a) Without using the existing find method of Python strings, write a function find(s, substring).

# that does the same thing as the find method. If the substring
#  appears in s, the method should return its index, otherwise it
#  should return -1. Write the function in the file problem3.py. 

# (b) Without using the existing find method, write a function
#  find_multi(s, substring), that returns a list of the indices
#  of all occurrences of the substring. If the substring is not found, the
#  function can return an empty list. Make sure your function can handle
#  overlapping substrings. For example: 

# find_multi("ATGCGCGAT", "GCG") should return [2,4].

# Add the function to the file problem3.py. 



#run a loop through the string. At every index position, the value from that position is checked against the the
#substring position for the length of the substring. If the sliced index value matches the substring values,
#the index location is added to location_idx. As soon as a new value replaced the index location the loop is broken 
#the index location is returned.

def find(s, substring):
  idx_loc = -1
  position = 0
  for i in s:
    if s[position:position + len(substring)] == substring:
      idx_loc = position
      if position != -1:
        break
    position += 1

  return idx_loc
print(find("ATCGCGTACT", "CGAT"))

            
#run a loop through the string. At every index position, the value from that position is checked against the the
#substring position for the length of the substring. If the sliced index value matches the substring values,
#the index location is added to location_idx.

def find_multi(s, substring):
  position = 0
  location_idx = []
  for i in s:
    if s[position:position + len(substring)] == substring:
      location_idx.append(position)
    position += 1

  return(location_idx)

print(find_multi("ATGCGCGAT", "GCG"))
