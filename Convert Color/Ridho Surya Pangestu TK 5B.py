# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 09:54:58 2024

@author: Acer Nitro
"""

import cv2

# Inisialisasi kamera bawaan laptop
cap = cv2.VideoCapture(0)

while True:
    # Baca frame dari kamera
    ret, frame = cap.read()

    # Membalik frame secara horizontal
    frame = cv2.flip(frame, 1)

    # Konversi frame ke mode HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Konversi frame ke grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Konversi frame ke citra hitam-putih (binary)
    _, bw_frame = cv2.threshold(gray_frame, 128, 255, cv2.THRESH_BINARY)

    # Tampilkan empat jendela
    cv2.imshow('Original', frame) #jendela warna asli
    cv2.imshow('HSV', hsv_frame) #jendela warna pekat 
    cv2.imshow('Grayscale', gray_frame) #jendela warna abu abu
    cv2.imshow('Black and White', bw_frame) #jendela warna hitam putih

    # Tekan tombol 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tutup kamera dan jendela
cap.release()
cv2.destroyAllWindows()