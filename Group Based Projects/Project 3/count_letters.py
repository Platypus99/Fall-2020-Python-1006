#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 14:35:45 2020

@author: daniel
"""

# Step 1: Open the file 
f = open("constitution.txt",'r')


letter_count = {} # keys will be letters, values will be the int count

# Iterate through the file
for line in f: 
    line = line.strip()
    line = line.lower()
    
    for ch in line: 

        if ord(ch) >= ord('a') and ord(ch) <= ord('z'):            
            if not ch in letter_count: 
                letter_count[ch] = 0        
    
            letter_count[ch] = letter_count[ch] + 1
            
            #Alternatively: 
            #try: 
            #    letter_count[ch] = letter_count[ch] + 1
            #except KeyError: 
            #    letter_count[ch] = 1
        
# Now print a sorted list of letters and frequencies 
letters_and_freqs = []

for k,v in letter_count.items():
    letters_and_freqs.append((v,k))
    

letters_and_freqs.sort(reverse = True)
print(letters_and_freqs)    
