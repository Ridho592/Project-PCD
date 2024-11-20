import cv2
import numpy as np
def calculate_ber(img1, img2):
  

  """

  Fungsi untuk menghitung BER antara dua citra grayscale.

  Args:

    img1: Citra referensi.

    img2: Citra yang terdistorsi.



  Returns:

    Nilai BER.

  """
  # Pastikan kedua citra memiliki ukuran yang sama

  if img1.shape != img2.shape:

    raise ValueError("Kedua citra harus memiliki ukuran yang sama")
  # Ubah citra menjadi array 1D

  img1_flat = img1.flatten()

  img2_flat = img2.flatten()
  # Hitung jumlah bit yang berbeda
  num_diff_bits = np.sum(np.bitwise_xor(img1_flat, img2_flat))
  # Hitung total jumlah bit
  total_bits = img1_flat.size * 8  # Asumsikan 8 bit per pixel
  # Hitung BER
  ber = num_diff_bits / total_bits
  return ber

# Contoh penggunaan

img1 = cv2.imread('NSP.jpg', cv2.IMREAD_GRAYSCALE)

img2 = cv2.imread('NSP.jpg', cv2.IMREAD_GRAYSCALE)

ksize = (10, 10) 
img2 = cv2.blur(img2, ksize)

ber = calculate_ber(img1, img2)

print("Bit Error Rate:", ber)