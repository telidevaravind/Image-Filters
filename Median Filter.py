import numpy as np
from scipy.misc import toimage
import cv2
#from matplotlib import pyplot as plt
def median_filter(im):
    im = im.flatten('F')
    l = len(im)
    for i in range(l):
        for j in range(0, l - i - 1):
            if im[j] > im[j + 1]:
                im[j], im[j + 1] = im[j + 1], im[j]
    return im[(l//2) +1]

def Median_Filter():
    imageFileName = input("enter the image name with absolute path:\n ")
    image = cv2.imread(imageFileName, 0)
    # print image
    # toimage(image).show()
    height, width = image.shape
    print ('height:\n', height)
    print ('width:\n', width)
    # print 'channels:\n', channels
    m = input('Enter the height of filter:\n')
    n = input('Enter the width of filter:\n')
    m = int(m)
    n = int(n)
    print('The size of the filter is: %d * %d\n' % (m, n))
    pad = int((n - 1) / 2)
    print ('pad:', pad)
    image = cv2.copyMakeBorder(image, pad, pad, pad, pad, cv2.BORDER_CONSTANT)
    Blur = np.zeros((height, width), int)
    for y in np.arange(pad, height + 1):
        for x in np.arange(pad, width + 1):
            mod = image[y - pad:y + pad + 1, x - pad:x + pad + 1]
            # print mod
            k = median_filter(mod)
            # print k
            Blur[y - pad, x - pad] = k
    # print Blur
    
    return toimage(Blur).show()
Median_Filter()
