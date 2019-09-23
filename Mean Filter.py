import numpy as np
from scipy.misc import toimage
import cv2

def Mean_Filter():
    imageFileName = input("enter the image name with absolute path:\n ")
    image = cv2.imread(imageFileName, 0)
    print(image)
    height, width = image.shape
    print('height:\n', height)
    print('width:\n', width)
    # print 'channels:\n', channels
    m = input('Enter the height of filter:\n')
    n = input('Enter the width of filter:\n')
    m = int(m)
    n = int(n)
    print ('The size of the filter is: %d * %d\n' % (int(m), int(n)))
    pad = int((int(n) - 1) / 2)
    print ('pad:\n', pad)
    image_org = cv2.copyMakeBorder(image, pad, pad, pad, pad, cv2.BORDER_CONSTANT)
    mean_filter = float(1) / (m * n) * np.ones((m, n), dtype=int)
    Blur = np.zeros((height, width), int)
    for y in np.arange(pad, height + 1):
        for x in np.arange(pad, width + 1):
            mod = image_org[y - pad:y + pad + 1, x - pad:x + pad + 1]
            k = (mod * mean_filter).sum()
            Blur[y - pad, x - pad] = k
    print (Blur.shape)
    # return toimage(Blur).show()

    return toimage(Blur).show()
Mean_Filter()