import cv2
import numpy as np

img = cv2.imread('download.jpeg', 0)
img0 = cv2.imread('NSP.jpg', 0)
imgC = cv2.imread('semarang.jpg', 0)

kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)
dilation = cv2.dilate(img, kernel, iterations=1)
opening = cv2.morphologyEx(img0, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(imgC, cv2.MORPH_CLOSE, kernel)

#resize ukuran gambar
img0 = cv2.resize(img0, (300,300))
imgC = cv2.resize(imgC, (300,300))
img = cv2.resize(img, (300,300))
dilation = cv2.resize(dilation, (300,300))
opening = cv2.resize(opening, (300,300))
closing = cv2.resize(closing, (300,300))
erosion = cv2.resize(erosion, (300,300))

#titles = ['Original Image', 'Erosion', 'Dilation', 'Before Opening', 'Opening', 'Before Closing', 'Closing']
#images = [img, erosion, dilation, img0, opening, imgC, closing]
cv2.imshow('erosion', erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()
