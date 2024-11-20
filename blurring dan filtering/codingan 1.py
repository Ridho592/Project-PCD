import cv2
import numpy as np
import matplotlib.pyplot as plt

img_color = cv2.imread('NSP.jpg', 1)
img_gray = cv2.imread('NSP.jpg', 0)

blur1 = cv2.blur(img_gray, (3, 3))
blur2 = cv2.GaussianBlur(img_gray, (3, 3), 0)
median = cv2.medianBlur(img_gray, 3)
blur3 = cv2.bilateralFilter(img_gray, 9, 75, 75)

titles = ["Original", "Averaging Blur", "Gaussian Blur", "Bilateral Blur", "Median Blur"]
images = [img_color, blur1, blur2, blur3, median]
is_color_flags = [True, False, False, False, False]

fig, axes = plt.subplots(len(images), 2, figsize=(12, 10))
fig.suptitle("Gambar dan Histogram ", fontsize=18)

for i, (title, image, is_color) in enumerate(zip(titles, images, is_color_flags)):
    
    if is_color:
        image_display = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    else:
        image_display = image
    axes[i, 0].imshow(image_display, cmap='gray' if not is_color else None)
    axes[i, 0].set_title(f'{title} Image')
    axes[i, 0].axis('off')

    
    axes[i, 1].hist(image.ravel(), bins=256, color='blue', alpha=0.7)
    axes[i, 1].set_title(f"Histogram of {title}")
    axes[i, 1].set_xlim([0, 256])
    axes[i, 1].set_xlabel('Pixel Intensity')
    axes[i, 1].set_ylabel('Frequency')
    axes[i, 1].grid(True, linestyle='--', alpha=0.5)


plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.show()
