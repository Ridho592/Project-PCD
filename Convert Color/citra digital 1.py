#memilih warna biru saja pada gambar gambar 
import cv2 # menyertakan library cv2 dari opencv
import numpy as np

img0 = cv2.imread("NSP.jpg")
gray = cv2.cvtColor(img0, cv2.COLOR_RGBA2GRAY)

# print(img0.shape)
# print("img0 ", img)
# lowBlue = np.array([30, 10, 10])
# highBlue = np.array([40, 255, 255])
# mask = cv2.inRange (img, lowBlue, highBlue)

cv2.imshow("Gray", gray)
print('gray = ' , gray)
# cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()