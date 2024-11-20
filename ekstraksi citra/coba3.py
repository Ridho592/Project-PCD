import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
from skimage.morphology import remove_small_holes, remove_small_objects, closing, square

# Membaca gambar dalam format RGB
gambar = cv2.imread("NSP.jpg")
gambar_rgb = cv2.cvtColor(gambar, cv2.COLOR_BGR2RGB)

# Konversi RGB ke Grayscale
gambar_gray = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)

# Konversi Grayscale ke Biner menggunakan Threshold
_, gambar_biner = cv2.threshold(gambar_gray, 127, 255, cv2.THRESH_BINARY_INV)

# Menghilangkan objek kecil (noise) yang memiliki area di bawah 30
gambar_biner = remove_small_objects(gambar_biner > 0, min_size=30)
gambar_biner = (gambar_biner * 255).astype(np.uint8)

# Operasi Morfologi - Closing
kernel = square(5)
gambar_closing = closing(gambar_biner, kernel)

# Filling Holes - Mengisi lubang kecil pada objek
gambar_filled = remove_small_holes(gambar_closing > 0, area_threshold=100)
gambar_filled = (gambar_filled * 255).astype(np.uint8)

# Segmentasi dan pelabelan objek
label_gambar = label(gambar_filled)
properties = regionprops(label_gambar)

# Membuat gambar hasil anotasi
gambar_annotasi = gambar.copy()

# Fungsi untuk mengklasifikasikan bentuk berdasarkan jumlah sisi
def klasifikasi_bentuk(approx):
    if len(approx) == 3:
        return "Segitiga"
    elif len(approx) == 4:
        (x, y, w, h) = cv2.boundingRect(approx)
        rasio_aspek = float(w) / h
        if 0.95 <= rasio_aspek <= 1.05:
            return "Persegi"
        else:
            return "Persegi Panjang"
    elif len(approx) > 4:
        return "Lingkaran"
    return "Tidak Diketahui"

# Proses per objek untuk menghitung parameter dan klasifikasi bentuk
for prop in properties:
    if prop.area > 30:  # Filter objek kecil
        # Menghitung parameter: luas, keliling, eccentricity, dan metrik
        area = prop.area
        perimeter = prop.perimeter
        eccentricity = prop.eccentricity
        metric = 4 * np.pi * area / (perimeter ** 2) if perimeter > 0 else 0
        
        # Kontur untuk mengklasifikasikan bentuk objek
        kontur = cv2.findContours(gambar_filled, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        for cnt in kontur:
            approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
            bentuk = klasifikasi_bentuk(approx)
        
            # Menggambar bounding box dan label bentuk pada gambar anotasi
            minr, minc, maxr, maxc = prop.bbox
            cv2.rectangle(gambar_annotasi, (minc, minr), (maxc, maxr), (0, 255, 0), 2)
            cv2.putText(gambar_annotasi, bentuk, (minc, minr - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
            cv2.putText(gambar_annotasi, f"Area: {area}", (minc, minr + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
            cv2.putText(gambar_annotasi, f"Metric: {metric:.2f}", (minc, minr + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 255), 1)
            cv2.putText(gambar_annotasi, f"Eccentricity: {eccentricity:.2f}", (minc, minr + 40), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255), 1)

# Menampilkan gambar asli dan gambar hasil anotasi
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(gambar_rgb)
plt.title("Gambar Asli (RGB)")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(gambar_annotasi, cv2.COLOR_BGR2RGB))
plt.title("Hasil Deteksi dan Klasifikasi Bentuk")
plt.axis('off')
plt.show()