import cv2
import numpy as np

threshold = 0.7
kernel5 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20, 20))
x_co = 0
y_co = 0
hsv = None
H = 0
S = 0
V = 0
thr_H = 180 * threshold
thr_S = 255 * threshold
thr_V = 255 * threshold

def on_mouse(event, x, y, flag, param):
    global x_co, y_co, H, S, V, hsv
    if event == cv2.EVENT_LBUTTONDOWN:
        x_co = x
        y_co = y
        p_sel = hsv[y_co][x_co]
        H = p_sel[0]
        S = p_sel[1]
        V = p_sel[2]

cv2.namedWindow("camera", 1)
cv2.namedWindow("camera2", 2)
cv2.namedWindow("camera3", 3)

src = cv2.imread('warna.jpg')
#src = cv2.imread('stroberi.jpg')  
src = cv2.resize(src, (640, 480))  
src = cv2.blur(src, (3, 3))
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
cv2.setMouseCallback("Original",on_mouse, 0)


while True:
    min_color = np.array([H - thr_H, S - thr_S, V - thr_V])
    max_color = np.array([H + thr_H, S + thr_S, V + thr_V])
    mask = cv2.inRange(hsv, min_color, max_color)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel5)
    #cv2.setMouseCallback("Original",on_mouse, 0)

    # Show the mask and original image
    cv2.putText(mask, "H:" + str(H) + " S:" + str(S) + " V:" + str(V), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2.0, (255, 255, 255), thickness=1)
    cv2.imshow("Gambar1", mask)
    cv2.imshow("Original", src)
    cv2.imshow("Gambar2", mask)
    
    src_segmented = cv2.add(src, src, mask=mask)
    
    # Press 'ESC' to break the loop
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
