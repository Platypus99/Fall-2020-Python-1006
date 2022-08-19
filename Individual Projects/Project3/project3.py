# Perry Flamer
# Individual Project 3 ENGIE 1006

import numpy as np
import matplotlib-inline
import matplotlib.pyplot as plt
import math

# this makes image look better on a macbook pro
def imageshow(img, dpi=200):
    if dpi > 0:
        F = plt.gcf()
        F.set_dpi(dpi)
    plt.imshow(img)


# to read in the file 'pattern.png' before function calls it
pattern = plt.imread('pattern.png')
# imageshow(pattern)


# Part 1:  Color Channels (30 points) 

def onechannel(pattern, rgb):
    pattern_channel = pattern.copy()
    height = pattern_channel.shape[0]
    width = pattern_channel.shape[1]
    
    for x in range(height):
        for y in range(width):
            for color in range(len(pattern_channel[x, y, :])):                        
                if not color == rgb:
                    pattern_channel[x, y, :][color] = 0   
    
    return pattern_channel

# test of onechannel funtcion for red
plt.imshow(onechannel(pattern, 0))
    

# Part 2 - Channel Permutations (35 points) 

def permutecolorchannels(pattern,li):
    pattern_copy = pattern.copy()
        
    height = pattern_copy.shape[0]
    width = pattern_copy.shape[1] 
    
    for x in range(height):
        for y in range(width):

            pattern_copy[x, y, :][li[0]] = pattern[x, y, :][0]
            pattern_copy[x, y, :][li[1]] = pattern[x, y, :][1]
            pattern_copy[x, y, :][li[2]] = pattern[x, y, :][2]

    return pattern_copy


#  for the image of the Columbia Library
permcolors = plt.imread('permcolors.jpg')
# imageshow(permcolors)
plt.imshow(permutecolorchannels(permcolors, [1,2,0]))

# for the example of a permuted pattern
# plt.imshow(permutecolorchannels(pattern, [2,0,1]))


# Problem 3 - Image encryption with XOR (35 points)

# used to load the data required for the function
key = np.load('key.npy')
secret = plt.imread('secret.bmp')
# plt.imshow(secret)
image = secret

def decrypt(image, key):
    img2 = image.copy()
    height = img2.shape[0]
    width = img2.shape[1]
    
    for x in range(height):
        for y in range(width):
            for color in range(len(img2[x, y, :])):
                img2[x, y, :][color] = image[x, y, :][color] ^ key[y]
                
    return img2


plt.imshow(decrypt(image, key))



