import cv2
import numpy as np

image = cv2.imread("NSP.jpg")
image = cv2.resize(image, (500, 500))
image_temp = image.reshape((-1, 3))

image_temp = np.float32(image_temp)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
numberofKcluster = 4

ret, label, center = cv2.kmeans(image_temp, numberofKcluster, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

center = np.uint8(center)
result = center[label.flatten()]
result2 = result.reshape((image.shape))

cv2.imshow('Original', image)
cv2.imshow('Hasilnya', result2)

cv2.waitKey(0)
cv2.destroyAllWindows()