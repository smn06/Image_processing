import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage

kernel_5x5= np.array ([[-1,-1,-1,-1,-1],[-1,1,2,1,-1],[-1,2,4,2,-1],[-1,1,2,1,-1],[-1,-1,-1,-1,-1]])

img = cv2.imread('a.png',0)
k5 = ndimage.convolve(img, kernel_5x5)

blur = cv2.GaussianBlur(img,(17,17),0)

g_hpf=img-blur


plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(g_hpf),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()