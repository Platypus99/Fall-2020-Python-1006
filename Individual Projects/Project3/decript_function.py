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

key = np.load('key.npy')

secret = plt.imread('secret.bmp')
plt.imshow(secret)
image = secret

def decrypt(image, key):
    img2 = image.copy()
    height = img2.shape[0]
    width = img2.shape[1]

    print(type (img2))
    print('size of img2: ', img2.shape)
    print('height: ', img2.shape[0])
    print('width: ', img2.shape[1])
    
    for x in range(height):
        for y in range(width):
            for color in range(len(img2[x, y, :])):
                # print(img2[x, y, :][color])
                img2[x, y, :][color] = image[x, y, :][color] ^ key[y]
                
                
            # print("\n")
            # print(img2[x, y, :][0])
            # print(len(img2[x, y, :]))
    
    return img2


plt.imshow(decrypt(image, key))