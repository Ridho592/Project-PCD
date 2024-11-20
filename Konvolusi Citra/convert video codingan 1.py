# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 09:54:58 2024

@author: Acer Nitro
"""

import cv2

# Inisialisasi kamera laptop
cap = cv2.VideoCapture(0)


while True:
    # membaca frame dari kamera
    ret, frame = cap.read()

    # Konversi frame Original
    frame = cv2.flip(frame, 1)

    # Konversi frame ke mode HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    print(hsv_frame)

    # Konversi frame ke grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Konversi frame ke black & white (binary)
    _, bw_frame = cv2.threshold(gray_frame, 128, 255, cv2.THRESH_BINARY)

    # menampilkan output jendela
    cv2.imshow('Original', frame) #membuka jendela warna asli
    cv2.imshow('HSV', hsv_frame) #membuka jendela warna pekat 
    cv2.imshow('Grayscale', gray_frame) #membuka jendela warna abu abu
    cv2.imshow('Black and White', bw_frame) #membuka jendela warna black & white

    # Tekan tombol 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# menutup kamera dan jendela
cap.release()
cv2.destroyAllWindows()