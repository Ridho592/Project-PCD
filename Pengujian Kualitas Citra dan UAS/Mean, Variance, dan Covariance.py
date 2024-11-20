import cv2
import numpy as np

# Fungsi untuk menghitung Mean
def calculate_mean(image):
    mean = np.mean(image)
    return mean

# Fungsi untuk menghitung Variance
def calculate_variance(image):
    variance = np.var(image)
    return variance

# Fungsi untuk menghitung Covariance antara dua citra
def calculate_covariance(image1, image2):
    # Flatten gambar untuk perhitungan satu dimensi
    flat_image1 = image1.flatten()
    flat_image2 = image2.flatten()
    
    # Pastikan kedua gambar memiliki ukuran sama
    if flat_image1.shape != flat_image2.shape:
        raise ValueError("Ukuran kedua gambar harus sama untuk menghitung Covariance")
    
    # Covariance
    covariance_matrix = np.cov(flat_image1, flat_image2)
    covariance = covariance_matrix[0, 1]  # Ambil elemen (0, 1) atau (1, 0)
    return covariance

def main():
    # Membaca gambar
    image1 = cv2.imread("NSP.jpg", cv2.IMREAD_GRAYSCALE)  # Gambar pertama (Grayscale)
    image2 = cv2.imread("NSP.jpg", cv2.IMREAD_GRAYSCALE)  # Gambar kedua (Grayscale)
    
    if image1 is None or image2 is None:
        print("Gambar tidak ditemukan. Pastikan file ada dan jalurnya benar.")
        return
    
    # Hitung Mean, Variance, dan Covariance
    mean_image1 = calculate_mean(image1)
    variance_image1 = calculate_variance(image1)
    covariance = calculate_covariance(image1, image2)

    # Tampilkan hasil
    print(f"Mean Image 1: {mean_image1}")
    print(f"Variance Image 1: {variance_image1}")
    print(f"Covariance between Image 1 and Image 2: {covariance}")

if __name__ == "__main__":
    main()
