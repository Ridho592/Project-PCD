import cv2
import numpy as np

threshold = 0.8
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

img = cv2.imread("pisang.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.namedWindow("camera", 1)
cv2.namedWindow("camera2", 2)
cv2.namedWindow("camera3", 3)
cv2.setMouseCallback("camera2", on_mouse, 0)
cv2.resize(img, (300,300))
cv2.resize(hsv, (300,300))

while True:
    src = cv2.blur(img, (3, 3))
    min_color = np.array([H - thr_H, S - thr_S, V - thr_V])
    max_color = np.array([H + thr_H, S + thr_S, V + thr_V])
    mask = cv2.inRange(hsv, min_color, max_color)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel5)
    cv2.putText(mask, "H:" + str(H) + " S:" + str(S) + " V:" + str(V), (10, 30),
                cv2.FONT_HERSHEY_PLAIN, 2.0, (255, 255, 255), thickness=1)
    cv2.imshow("camera", mask)
    cv2.imshow("camera2", src)
    src_segmented = cv2.add(src, src, mask=mask)
    cv2.imshow("camera3", src_segmented)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
