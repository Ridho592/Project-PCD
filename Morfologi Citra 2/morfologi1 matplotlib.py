import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('download.jpeg', 0)
img0 = cv2.imread('NSP.jpg', 0)
imgC = cv2.imread('semarang.jpg', 0)

kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(img,kernel,iterations=1)
dilation = cv2.dilate(img,kernel,iterations=1)
opening = cv2.morphologyEx(img0, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(imgC, cv2.MORPH_CLOSE,kernel)

#resize ukuran gambar
img0 = cv2.resize(img0, (500,500))
imgC = cv2.resize(imgC, (500,500))
img = cv2.resize(img, (500,500))
dilation = cv2.resize(dilation, (500,500))
opening = cv2.resize(opening, (500,500))
closing = cv2.resize(closing, (500,500))
erosion = cv2.resize(erosion, (500,500))


titles = ['Normal Image', 'Erosion', 'Dilation', 'Before Opening', 'Opening', 'Before Closing', 'Closing']
images = [img, erosion, dilation, img0, opening, imgC, closing]

for i in range(7):
    plt.subplot(2,5,i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
