
import cv2 # menyertakan library cv2 dari opencv
import numpy as np

img = cv2.imread("NSP.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
(tresh, BW) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)


print("Original = ", img.shape)
print("Gray = ", gray.shape)
print("BW = ", BW.shape)
print(BW)
cv2.imwrite("Hasil.png", BW)