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


def rgb_ints_example():
    '''should produce red,purple,green squares
    on the diagonal, over a black background'''
    # RGB indexes
    red,green,blue = range(3)
    # img array 
    # all zeros = black pixels
    # shape: (150 rows, 150 cols, 3 colors)
    
    box = 30
    width = 300
    height = 200
    img = np.zeros((height, width, 3), dtype=np.uint8)
    

    
    for x in range(height):
        for y in range(width):
            # while x < width:
                # print(x , '\n')
                x1 = x // box
                y1 = y // box
                # if y == 199:
                    # print('y is 199')
                
                # green pixels           
                if  ((x1 + y1 + 2) % 4) ==0:
                    img[x, y,:] = (0, 255, 0)
                    
                # blue pixels    
                if  ((x1 + y1 + 2) % 4) ==1:
                    img[x, y,:] = (0, 0, 255) 
                    
                # blank (black) pixels
                if  ((x1 + y1 + 2) % 4) ==2:
                    img[x, y,:] = (0, 0, 0)    
                    
                # red pixels
                if  ((x1 + y1 + 2) % 4) ==3:
                    img[x, y,:] = (255, 0, 0) 
               
    
        #         # red pixels
        #         img[x,y,red] = 255
        #         # purple pixels
        #         # set all 3 color components
        #         img[x+50, y+50,:] = (128, 0, 128)
        #         # green pixels
        #         img[x+100,y+100,green] = 255
    
    
    
    
    # for x in range(50):
    #     for y in range(50):
    #         # red pixels
    #         img[x,y,red] = 255
    #         # purple pixels
    #         # set all 3 color components
    #         img[x+50, y+50,:] = (128, 0, 128)
    #         # green pixels
    #         img[x+100,y+100,green] = 255
    return img

plt.imshow(rgb_ints_example())

    



            
    
    
    
           