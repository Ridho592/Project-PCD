#konversi warna ke abu abu
import cv2 # menyertakan library cv2 dari opencv
import numpy as np

img = cv2.imread("NSP.jpg")
cv2.imshow("Original", img)

row, col = img.shape[0:2]

for i in range(row):
    for j in range(col):
        img[i, j] = sum(img[i, j]) * 0.33

# print(img.shape)

cv2.imshow("Hasil", img)
cv2.waitKey(0)
cv2.destroyAllWindows()