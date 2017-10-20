import ReadDataFiles#import from previous file
import numpy as np
def readImage(no):
    myimage = ReadDataFiles.train_images[no]
    myimage = np.array(myimage)
    return myimage
# print image to console
def printImage(myimage):
    for row in myimage:
        for col in row:
            print('.' if col<128 else '/',end='')#set  the range
        print()
number = 3
printImage(readImage(number))

