# skala

import cv2

img = cv2.imread("download.jpeg")

dstSkala = cv2.resize(img, None, fx=2.5, fy=2.0, interpolation=cv2.INTER_CUBIC)
cv2.imshow("ori",img)
cv2.imshow("scale",dstSkala)

cv2.waitKey(0)
cv2.destroyAllWindows()