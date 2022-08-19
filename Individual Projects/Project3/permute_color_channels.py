import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math

# this makes image look better on a macbook pro
def imageshow(img, dpi=200):
    if dpi > 0:
        F = plt.gcf()
        F.set_dpi(dpi)
    plt.imshow(img)


pattern = plt.imread('pattern.png')
imageshow(pattern)

# li = [2,0,1]
# li  = [1,0,2]
def permutecolorchannels(pattern,li):
    pattern_copy = pattern.copy()
    
    red,green,blue = range(3)
    
    height = pattern_copy.shape[0]
    width = pattern_copy.shape[1]
    
    print(type (pattern_copy))
    print('size of pattern_copy: ', pattern_copy.shape)
    print('height: ', pattern_copy.shape[0])
    print('width: ', pattern_copy.shape[1])
    
    
    for x in range(height):
        for y in range(width):
            # x1 = x // box
            # y1 = y // box
            
            #red pixels
            # if  not ((x1 + y1 + 2) % 4) ==3:
                # pattern[x, y,:] = (255, 0, 0)
            # else:
                # pattern[x, y,:] = (0, 0, 0) 
            
            
            # this_pixel1 = pattern[x, y, :].copy()
            # this_pixel2 = pattern[x, y, :]
            # this_pixel3 = pattern[x, y, :]
            

            # pattern[x, y, :][1:3] = this_pixel[1:3]
            
            
            # print(pattern_copy[x, y, :], " is pattern_copy before change")
            pattern_copy[x, y, :][li[0]] = pattern[x, y, :][0]
            pattern_copy[x, y, :][li[1]] = pattern[x, y, :][1]
            pattern_copy[x, y, :][li[2]] = pattern[x, y, :][2]
            
            # print (pattern_copy[x, y, :], " is new pattern_copy[x, y, :]",)
            # print(pattern[x, y, :], " is pattern after change in pattern_copy should be same as before change")
            # print("\n")
            
                
    return pattern_copy

# print ("pattern")
# plt.imshow(pattern)
# print ("permuted pattern using li")
# plt.imshow(permutecolorchannels(pattern, [2,0,1]))


permcolors = plt.imread('permcolors.jpg')
imageshow(permcolors)
plt.imshow(permutecolorchannels(permcolors, [1,2,0]))