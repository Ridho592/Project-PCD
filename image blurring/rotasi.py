#rotasi

import cv2
import numpy as np

img = cv2.imread("download.jpeg")
print(img.shape)

baris, coloms, ghgh = img.shape

#MTranslasi = np.float32([[2, 0, 100],[0, 2, 50]])

#print(MTranslasi, '\n')

MRotasi = cv2.getRotationMatrix2D((coloms/2, baris/2,),90, 1)

print(MRotasi, '\n')


dst = cv2.warpAffine (img, MRotasi, (coloms, baris))
#dst = cv2.warpAffine (img, MTranslasi, (coloms, baris))
cv2.imshow("Hasil", dst) 
#cv2.imshow("rotasi", )

cv2.waitKey(0)
cv2.destroyAllWindows()