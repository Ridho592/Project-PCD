# Citra-Digital
---

### *1. Convert Color*
*Konversi Warna* adalah proses mengubah ruang warna citra dari satu model ke model lainnya. Contohnya: 
- Dari RGB ke Grayscale.
- Dari RGB ke HSV (Hue, Saturation, Value).
*Tujuan*:
- Mempermudah analisis citra (misalnya analisis fitur lebih sederhana dalam Grayscale).
- Menyesuaikan format untuk algoritma tertentu.

*Contoh:*
~~~python
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)~~~

Gambar Asli:

<img width="200" height="200" src="https://github.com/user-attachments/assets/a3017bb8-8003-4def-a3be-5f2b40184d1c" alt="Bidang">
