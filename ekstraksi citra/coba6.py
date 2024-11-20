import cv2
import numpy as np

# Load images
gambar = [
    cv2.imread("contoh.jpg"),
    cv2.imread("NSP.jpg")
]

# Check if images are loaded correctly
if gambar[0] is None or gambar[1] is None:
    print("Error: One or both images could not be loaded.")
else:
    iterasiClosing = [1, 4]
    iterasiOpening = [1, 4]
    kernelOpen = np.ones((5,5), np.uint8)
    kernelClose = np.ones((5,5), np.uint8)

    for i in range(len(gambar)):
        # Resize and convert to grayscale
        gambar[i] = cv2.resize(gambar[i], (640, 480))
        abu = cv2.cvtColor(gambar[i], cv2.COLOR_BGR2GRAY)
        _, biner = cv2.threshold(abu, 127, 255, cv2.THRESH_BINARY)

        # Perform closing and opening operations
        closing = cv2.morphologyEx(biner, cv2.MORPH_CLOSE, kernelClose, iterations=iterasiClosing[i])
        opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernelOpen, iterations=iterasiOpening[i])

        # Segment image
        segmen = cv2.Canny(opening, 30, 200)
        contours, _ = cv2.findContours(segmen, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        segmen = cv2.cvtColor(segmen, cv2.COLOR_GRAY2RGB)
        cv2.drawContours(gambar[i], contours, -1, (0, 0, 255), 1)

        # Loop through each contour and calculate properties
        pusat = []
        for j, contour in enumerate(contours):
            moments = cv2.moments(contour)
            if moments['m00'] == 0:  # Check to prevent division by zero
                continue

            # Calculate centroid
            pusat.append((int(moments['m10'] / moments['m00']), int(moments['m01'] / moments['m00'])))
            cv2.circle(gambar[i], pusat[-1], 1, (0, 0, 255), -1)  # Draw center point
            cv2.putText(gambar[i], str(j + 1), pusat[-1], cv2.FONT_HERSHEY_DUPLEX, 0.75, (0, 255, 255), 1)  # Label object

            # Calculate the best-fit ellipse if contour has enough points
            if len(contour) >= 5:  # fitEllipse requires at least 5 points
                (x, y), (minorAxis, majorAxis), angle = cv2.fitEllipse(contour)
                eccentricity = np.sqrt(1 - (minorAxis ** 2 / majorAxis ** 2))
            else:
                eccentricity = 0  # Default eccentricity for small contours

            luas = cv2.contourArea(contour)
            keliling = cv2.arcLength(contour, True)
            metrik = (4 * np.pi * luas) / keliling ** 2 if keliling != 0 else 0  # Avoid division by zero

            print("----------------------")
            print(f'Eccentricity of object {j+1} in image {i+1} : {eccentricity}')
            print(f'Luas objek {j+1} in image {i+1} : {luas}')
            print(f'Keliling objek {j+1} pada citra {i+1} : {keliling}')
            print(f'Metric of object {j+1} in image {i+1} : {metrik}')

            # Determine the shape based on the metric
            offset = (pusat[-1][0], pusat[-1][1] + 20)
            if metrik >= 0.8:
                bentuk = "Bulat"
            elif metrik < 0.6:
                bentuk = "Segitiga"
            elif 0.7 <= metrik < 0.8:
                bentuk = "Kotak"
            else:
                bentuk = "Undefined"
            
            # Display the shape name below the center point
            cv2.putText(gambar[i], str(bentuk), offset, cv2.FONT_HERSHEY_DUPLEX, 0.6, (255, 255, 0), 1)

    # Display images
    cv2.imshow('Gambar 1', gambar[0])
    cv2.imshow('Gambar 2', gambar[1])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
