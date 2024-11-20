import numpy as np  # Menyertakan library numpy sebagai np
import cv2  # Menyertakan library opencv-python

# Mengambil video dari direktori
camera = cv2.VideoCapture("Ridho Surya Pangestu_TK5B_226201033_Tugas2_KonvolusiCitra.mp4")  # konvolusi manual

# Definisi fungsi konvolusi manual dengan parameter citra dan kernel
def konvolusi(image, kernel):
    row, col = image.shape  # Mengambil nilai lebar dan tinggi dari citra
    mrow, mcol = kernel.shape  # Mengambil nilai lebar dan tinggi dari kernel
    h = int(mrow / 2)  # Mengambil setengah tinggi dari kernel

    # Membuat citra kosong atau citra penuh dengan piksel hitam yang setiap pikselnya berukuran 8bit
    canvas = np.zeros((row, col), np.uint8)

    for i in range(0, row):  # Perulangan untuk membaca setiap baris dari citra
        for j in range(0, col):  # Perulangan untuk membaca setiap kolom dari citra
            # Memeriksa apakah piksel saat ini berada di tepi gambar
            if i == 0 or i == row - 1 or j == col - 1:
                canvas.itemset((i, j), 0)  # Ubah piksel tersebut menjadi hitam
            else:
                # Deklarasi variabel untuk penempatan hasil penjumlahan dari hasil perkalian citra dengan kernel
                imgsum = 0

                # Perulangan untuk membaca setiap baris dari kernel
                for k in range(-h, mrow - h):
                    # Perulangan untuk membaca setiap kolom dari kernel
                    for l in range(-h, mcol - h):
                        # Perkalian piksel citra dengan piksel kernel
                        res = image[i + k, j + l] * kernel[h + k, h + l]
                        # Tambahkan hasil perkalian ke variabel imgsum
                        imgsum += res
                
                # Ubah piksel tersebut menjadi hasil konvolusi
                canvas.itemset((i, j), imgsum)

    return canvas  # Mengembalikan hasil konvolusi

# Definisi fungsi kernel High Pass Filter dengan parameter citra
def kernel1(image):
    # Kernel High Pass Filter dengan setiap pikselnya merupakan nilai float 32-bit
    kernel = np.array([[-1 / 9, -1 / 9, -1 / 9], [-1 / 9, 8 / 9, -1 / 9], [-1 / 9, -1 / 9, -1 / 9]], np.float32)
    # Lakukan proses konvolusi lalu simpan ke variabel canvas
    canvas = konvolusi(image, kernel)
    print("Hasil konvolusi kernel1 = ", canvas)  # Cetak piksel hasil konvolusi
    return canvas  # Mengembalikan hasil konvolusi

# Definisi fungsi kernel Low Pass Filter dengan parameter citra
def kernel2(image):
    # Kernel Low Pass Filter dengan setiap pikselnya merupakan nilai float 32-bit
    kernel = np.array([[0, 1 / 8, 0], [1 / 8, 1 / 2, 1 / 8], [0, 1 / 8, 0]], np.float32)
    # Lakukan proses konvolusi lalu simpan ke variabel canvas2
    canvas2 = konvolusi(image, kernel)
    print("Hasil konvolusi kernel2 = ", canvas2)  # Cetak piksel hasil konvolusi
    return canvas2

while True:
    ret, frame = camera.read()  # Membaca setiap frame dari video
    if not ret:
        break

    image1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Mengubah frame video menjadi warna abu-abu
    test1 = kernel1(image1)  # Lakukan proses High Pass Filter
    print("gambar1 ordo = ", image1.shape)  # Cetak ukuran citra frame
    print("gambar1 ori = ", image1)  # Cetak piksel citra frame
    print("gambar1 HPF ordo = ", test1.shape)  # Cetak ukuran citra setelah di-filter dengan High Pass Filter
    print("gambar1 HPF = ", test1)  # Cetak piksel citra setelah di-filter dengan High Pass Filter

    cv2.imshow("gambar1", image1)  # Tampilkan citra frame di jendela
    cv2.imshow("High pass", test1)  # Tampilkan citra frame High Pass Filter di jendela

    test2 = kernel2(image1)  # Lakukan proses Low Pass Filter pada frame
    print("gambar2 ori ordo = ", image1.shape)  # Cetak ukuran frame
    print("gambar2 ori = ", image1)  # Cetak piksel frame
    print("gambar1 LPF ordo = ", test2.shape)  # Cetak ukuran frame Low Pass Filter
    print("gambar2 LPF = ", test2)  # Cetak piksel frame Low Pass Filter

    cv2.imshow("gambar2", image1)  # Tampilkan frame di jendela
    cv2.imshow("low pass", test2)  # Tampilkan frame Low Pass Filter di jendela

    # Menunda selama 1 detik dan menunggu interupsi dari keyboard jika pengguna menekan 'q'
    if cv2.waitKey(1) == ord('q'):
        break  # Hentikan program

camera.release()  # Menutup kamera
cv2.destroyAllWindows()  # Menutup semua jendela frame
