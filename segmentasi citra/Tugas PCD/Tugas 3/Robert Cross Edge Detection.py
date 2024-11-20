import cv2
import numpy as np
from scipy import ndimage
image = cv2.imread("pisang.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernelX = np.array([[1, 0], [0, -1]])
kernelY = np.array([[0, 1], [-1, 0]])

robertX = ndimage.convolve(gray, kernelX)
robertY = ndimage.convolve(gray, kernelY)
robertX = np.float32(robertX)
robertY = np.float32(robertY)

robert = np.sqrt(np.square(robertX) + np.square(robertY))
# robert = cv2.addWeighted(robertX, 0.5, robertY, 0.5, 0)
_, robert = cv2.threshold(robert, 50, 255, cv2.THRESH_BINARY)

cv2.imshow("Robert.jpg", robert)
cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
