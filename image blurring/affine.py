# Affine

import cv2
import numpy as np

ttkAsal = np.float32([[172,109], [282,65], [272,316]])
ttkTujuan = np.float32([[53,128], [471,46], [275, 385]])

MAffine = cv2.getAffineTransform(ttkAsal, ttkTujuan)

print(MAffine)

dstAffine = cv2.warpAffine(img, MAffine, (cols, rows))

cv2_imshow(dstAffine)