import cv2
import numpy as np

image = cv2.imread("NSP.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)

kernelX = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
])

kernelY = np.array([
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
])

prewittX = cv2.filter2D(gray, -1, kernelX)
prewittY = cv2.filter2D(gray, -1, kernelY)

prewittX = np.float32(prewittX)
prewittY = np.float32(prewittY)

prewitt = cv2.magnitude(prewittX, prewittY)

cv2.imshow("Original", image)
cv2.imshow("Prewitt.jpg", prewitt)
cv2.waitKey(0)
cv2.destroyAllWindows()
