import cv2
import numpy as np
import argparse
import imutils
import math

def process_image(image_path):
    # Membaca gambar dan merubah ukuran
    gambar1 = cv2.imread(image_path)
    gambar1 = cv2.resize(gambar1, (400, 400))
    
    # Konversi gambar ke grayscale dan blurring
    gray = cv2.cvtColor(gambar1, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Thresholding untuk menghasilkan gambar biner
    _, BW1 = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)
    
    # Deteksi tepi dengan Canny pada gambar biner
    edges = cv2.Canny(blurred, 100, 100)
    
    # Temukan kontur pada gambar hasil Canny
    cnts = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    
    # Buat salinan gambar asli untuk ditampilkan dengan label kontur
    labeled_image = gambar1.copy()
    centers = []
    
    # Loop untuk setiap kontur yang terdeteksi
    for c in cnts:
        # Hitung momen untuk menemukan pusat kontur
        M = cv2.moments(c)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            
            # Hitung keliling dan area kontur
            perimeter = cv2.arcLength(c, True)
            area = cv2.contourArea(c)
            
            # Gambar kontur dan pusat pada gambar asli
            cv2.drawContours(labeled_image, [c], -1, (0, 0, 255), 1)
            cv2.circle(labeled_image, (cX, cY), 5, (255, 255, 255), -1)
            
            # Tambahkan titik pusat ke dalam daftar centers
            centers.append((cX, cY))
    
    # Hitung jarak antar pusat objek dan sudut antar garis
    if len(centers) >= 2:
        # Jarak Euclidean antara dua pusat objek pertama
        c1, c2 = centers[0], centers[10]
        distance = math.sqrt((c2[0] - c1[0]) ** 2 + (c2[1] - c1[1]) ** 2)
        
        # Tampilkan jarak dalam satuan piksel
        mid_point = ((c1[0] + c2[0]) // 2, (c1[1] + c2[1]) // 2)
        cv2.line(labeled_image, c1, c2, (0, 255, 255), 1)
        cv2.putText(labeled_image, f"Dist: {distance:.2f} px",
                    (mid_point[0], mid_point[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
        
        # Hitung sudut antara garis horizontal dan garis antara dua pusat
        dx = c2[0] - c1[0]
        dy = c2[1] - c1[1]
        angle = math.degrees(math.atan2(dy, dx))
        
        # Tampilkan sudut dalam derajat
        cv2.putText(labeled_image, f"Angle: {angle:.2f} deg",
                    (c1[0] - 40, c1[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)
    
    # Tampilkan gambar hasil dengan label kontur, jarak, dan sudut
    cv2.imshow(f"Labeled Image with Geometry - {image_path}", labeled_image)
    cv2.imshow(f"Edges - {image_path}", edges)

# Inisialisasi argparse
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", nargs='+', default=["sawah2.png", "pulau3.png"], help="path to the input images")
args = vars(ap.parse_args())

# Proses setiap gambar
for image_path in args["images"]:
    process_image(image_path)

cv2.waitKey(0)
cv2.destroyAllWindows()
