import numpy as np
import cv2



camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 340)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 680)

image1 = cv2.imread("NSP.jpg",0)
print(image1)
print("Ukuran Gambar:", camera.shape)
image2= cv2.imread("NSP.jpg",0)
print(image2)
print("Ukuran Gambar:", camera.shape)

#konvolusi manual
def konvolusi(image, kernel):
    row,col= image.shape
    mrow,mcol=kernel.shape
    h =int(mrow/2)

    canvas = np.zeros((row,col),np.uint8)
    for i in range(0,row):
        for j in range(0,col):
            if i==0 or i==row-1 or j==col-1:
                canvas.itemset((i,j),0)
            else:
                imgsum=0
                for k in range (-h, mrow-h):
                    for l in range (-h, mcol-h):
                        res=image[i+k,j+l] * kernel[h+k,h+l]
                        imgsum+=res
                canvas.itemset((i,j), imgsum)
    return canvas

def kernel1(image):
    kernel = np.array([[-1/9, -1/9, -1/9],[-1/9, 8/9, -1/9],[-1/9, -1/9, -1/9]],np.float32)
    canvas = konvolusi(image, kernel)
    return canvas

def kernel2(image):
    kernel = np.array([[0, 1/8, 0],[1/8, 1/2, 1/8],[0, 1/8, 0]],np.float32)
    canvas2 = konvolusi(image, kernel)
    return canvas2

test1=kernel1(camera)
cv2.imshow("gambar1",camera)
cv2.imshow("High pass",test1)
print(image1)


test2=kernel2(camera)
cv2.imshow("gambar2",camera)
cv2.imshow("low pass",test2)
print(image2)


cv2.waitKey(0)
cv2.destroyAllWindows()