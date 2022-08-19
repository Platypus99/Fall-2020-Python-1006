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

def onechannel(pattern, rgb):
    pattern_channel = pattern.copy()
    height = pattern_channel.shape[0]
    width = pattern_channel.shape[1]

    # print(type (pattern_channel))
    # print('size of pattern_channel: ', pattern_channel.shape)
    # print('height: ', pattern_channel.shape[0])
    # print('width: ', pattern_channel.shape[1])
    
    for x in range(height):
        for y in range(width):
            for color in range(len(pattern_channel[x, y, :])):                        
                if not color == rgb:
                    pattern_channel[x, y, :][color] = 0   
    
    return pattern_channel
plt.imshow(onechannel(pattern, 0))