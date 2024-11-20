import cv2
import numpy as np

img = cv2.imread("NSP.jpg", 0)
img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
numberLabel, Labelobjek = cv2.connectedComponents(img)
hueLabel = np.uint8(179*Labelobjek/np.max(Labelobjek))
emptyChannel = 255*np.ones_like(hueLabel)
Hasilimg = cv2.merge([hueLabel, emptyChannel, emptyChannel])
Hasilimg = cv2.cvtColor(Hasilimg, cv2.COLOR_HSV2BGR)
Hasilimg[hueLabel==0] = 0

cv2.imshow("connected Components", Hasilimg)
cv2.waitKey(0)
cv2.destroyAllWindows()