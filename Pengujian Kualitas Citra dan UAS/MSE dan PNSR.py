from math import log10, sqrt 
import cv2 
import numpy as np 

def PSNR(original, compressed): 
	mse = np.mean((original - compressed) ** 2) 
	if(mse == 0): # MSE is zero means no noise is present in the signal . 
				# Therefore PSNR have no importance. 
		return 100
	max_pixel = 255.0
	psnr = 20 * log10(max_pixel / sqrt(mse)) 
	return psnr 

def main(): 
	original = cv2.imread("NSP.jpg") 
	compressed = cv2.imread("NSP.jpg", 1) 
	value = PSNR(original, compressed) 
	print(f"PSNR value is {value} dB") 
	
if __name__ == "__main__": 
	main() 
# https://www.geeksforgeeks.org/python-peak-signal-to-noise-ratio-psnr/

"""
PSNR paling umum digunakan untuk memperkirakan efisiensi kompresor, filter, dll. 
Semakin besar nilai PSNR, semakin efisien metode kompresi atau filter yang sesuai.
Jika MSE = 0, artinya tidak ada perbedaan antara gambar asli dan gambar kompresi (keduanya identik).
"""