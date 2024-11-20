import cv2
import numpy as np
from matplotlib import pyplot as plt

# Membaca gambar
img = cv2.imread('NSP.jpg')

# Membuat berbagai jenis blur
blur1 = cv2.blur(img, (3, 3))
blur2 = cv2.GaussianBlur(img, (3, 3), 0)
median = cv2.medianBlur(img, 3)
blur3 = cv2.bilateralFilter(img, 9, 75, 75)

# Judul untuk setiap gambar
titles = ['Gambar Asli', 'Averaging', 'Gaussian Blur', 'Bilateral Blur', 'Median Blur']

# Gambar yang akan ditampilkan
images = [img, blur1, blur2, blur3, median]

# Menampilkan gambar dan histogram secara bersamaan
for i in range(5):
    plt.subplot(5, 2, 2 * i + 1), plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))  # Menampilkan gambar (konversi ke RGB)
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

    plt.subplot(5, 2, 2 * i + 2), plt.hist(images[i].ravel(), 256, [0, 256])  # Menampilkan histogram
    plt.title('Histogram')
    plt.xlim([0, 256])

# Menampilkan hasil
plt.tight_layout()
plt.show()
