import cv2
import numpy as np

image = cv2.imread("NSP.jpg", cv2.IMREAD_COLOR)
image = cv2.GaussianBlur(image, (3, 3), 0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ddepth = cv2.CV_16S
scale = 1
delta = 0

gradientX = cv2.Sobel(gray, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
gradientY = cv2.Sobel(gray, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)

absoluteGradientX = cv2.convertScaleAbs(gradientX)
absoluteGradientY = cv2.convertScaleAbs(gradientY)

sobel = cv2.addWeighted(absoluteGradientX, 0.5, absoluteGradientY, 0.5, 0)

cv2.imshow("Original", image)
cv2.imshow("Sobel", sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()
