import numpy as np  # Menyertakan library numpy sebagai np
import cv2  # Menyertakan library opencv-python

# Mengambil gambar dari direktori lalu ubah menjadi warna abu-abu
image1 = cv2.imread("download.jpeg", 0)
image2 = cv2.imread("NSP.jpg", 0)

# Definisi fungsi konvolusi manual dengan parameter citra dan kernel
def konvolusi(image, kernel):
    row, col = image.shape  # Mengambil nilai lebar dan tinggi dari citra
    mrow, mcol = kernel.shape  # Mengambil nilai lebar dan tinggi dari kernel
    h = int(mrow / 2)  # Mengambil setengah tinggi dari kernel

    # Membuat citra kosong atau citra penuh dengan piksel hitam yang setiap
    # pikselnya berukuran 8bit
    canvas = np.zeros((row, col), np.uint8)
    for i in range(0, row):  # Perulangan untuk membaca setiap baris dari citra
        for j in range(0, col):  # Perulangan untuk membaca setiap kolom dari citra
            # Memeriksa apakah piksel saat ini berada di tepi gambar
            if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                canvas.itemset((i, j), 0)  # Ubah piksel tersebut menjadi hitam
            else:  # Memeriksa apakah piksel saat ini bukan berada di tepi citra
                imgsum = 0
                # Perulangan untuk membaca setiap baris dari kernel
                for k in range(-h, mrow - h):
                    # Perulangan untuk membaca setiap kolom dari kernel
                    for l in range(-h, mcol - h):
                        # Perkalian piksel citra dengan piksel kernel
                        res = image[i + k, j + l] * kernel[h + k, h + l]
                        # Tambahkan hasil perkalian ke variable imgsum
                        imgsum += res
                # Ubah piksel tersebut menjadi hasil konvolusi
                canvas.itemset((i, j), imgsum)
    return canvas  # Mengembalikan hasil konvolusi

# Definisi fungsi kernel High Pass Filter dengan parameter citra
def kernel1(image):
    # Kernel High Pass Filter dengan setiap pikselnya merupakan nilai float 32-bit
    kernel = np.array([[-1 / 9, -1 / 9, -1 / 9], [-1 / 9, 8 / 9, -1 / 9], [-1 / 9, -1 / 9, -1 / 9]], np.float32)
    # Lakukan proses konvolusi lalu simpan ke variable canvas
    canvas = konvolusi(image, kernel)
    print("Hasil konvolusi kernel1 = ", canvas)  # Cetak piksel hasil konvolusi
    return canvas  # Mengembalikan hasil konvolusi

# Definisi fungsi kernel Low Pass Filter dengan parameter citra
def kernel2(image):
    # Kernel Low Pass Filter dengan setiap pikselnya merupakan nilai float 32-bit
    kernel = np.array([[0, 1 / 8, 0], [1 / 8, 1 / 2, 1 / 8], [0, 1 / 8, 0]], np.float32)
    # Lakukan proses konvolusi lalu simpan ke variable canvas2
    canvas2 = konvolusi(image, kernel)
    print("Hasil konvolusi kernel2 = ", canvas2)  # Cetak piksel hasil konvolusi
    return canvas2

test1 = kernel1(image1)  # Lakukan proses High Pass Filter
print("gambar1 ordo = ", image1.shape)  # Cetak ukuran citra image1
print("gambar1 ori = ", image1)  # Cetak piksel citra image1
# Cetak ukuran citra setelah di filter dengan High Pass Filter
print("gambar1 HPF ordo = ", test1.shape)
# Cetak piksel citra setelah di filter dengan High Pass Filter
print("gambar1 HPF = ", test1)
cv2.imshow("gambar1", image1)  # Tampilkan citra image1 di jendela
cv2.imshow("High pass", test1)  # Tampilkan citra image1 High Pass Filter di jendela

test2 = kernel2(image2)  # Melakukan proses Low Pass Filter pada image2
print("gambar2 ori ordo = ", image2.shape)  # Mencetak ukuran image2
print("gambar2 ori = ", image2)  # Mencetak seluruh piksel dari image2

row, col = image2.shape  # Mengambil baris dan kolom dari image2
for i in range(0, row):  # Perulangan untuk membaca setiap baris dari image2
    print("pixel = ", image2[i])  # Mencetak piksel dari image2
    # Mencetak nilai min dari piksel image2
    print("nilai min = ", min(image2[i]))
    # Mencetak nilai max dari piksel image2
    print("nilai max = ", max(image2[i]))

# Mencetak ukuran low pass filter image2
print("gambar1 LPF ordo = ", test2.shape)
print("gambar1 LPF = ", test2)  # Mencetak piksel low pass filter image2

cv2.imshow("gambar2", image2)  # Menampilkan image2 pada jendela
cv2.imshow("low pass", test2)  # Menampilkan image2 low pass filter pada jendela
cv2.waitKey(0)  # Menunda selama 0 detik atau menunggu interupsi dari keyboard
cv2.destroyAllWindows()  # Tutup semua jendela gambar

print(image1.shape)
cv2.resize(image1, (664,670))