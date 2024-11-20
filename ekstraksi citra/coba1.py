import cv2
import numpy as np

# Load images
images = [
    cv2.imread("NSP.jpg"),
    cv2.imread("apel.jpg")
]

iterations = [5, 1]
kernelOpen = np.ones((5,5), np.uint8)
kernelClose = np.ones((5,5), np.uint8)

for i in range(len(images)):
    # Resize and convert to grayscale
    images[i] = cv2.resize(images[i], (600, 600))
    gray = cv2.cvtColor(images[i], cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Perform closing and opening operations
    closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernelClose, iterations=iterations[i])
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernelOpen)

    # Segment image
    segment = cv2.Canny(opening, 30, 200)
    contours, hierarchy = cv2.findContours(segment, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    segment = cv2.cvtColor(segment, cv2.COLOR_GRAY2RGB)
    cv2.drawContours(images[i], contours, -1, (0, 0, 255), 1)

    # Find centers and calculate parameters
    centers = []
    for j in range(len(contours)):
        # Calculate moments and check if m00 is zero
        moments = cv2.moments(contours[j])
        if moments['m00'] != 0:
            cx = int(moments['m10'] / moments['m00'])
            cy = int(moments['m01'] / moments['m00'])
            centers.append((cx, cy))
            cv2.circle(images[i], (cx, cy), 1, (0, 0, 255), -1)  # Draw center point
            cv2.putText(images[i], str(j + 1), (cx, cy), cv2.FONT_HERSHEY_DUPLEX, 0.75, (0, 255, 255), 1)  # Label center

            # Calculate parameters
            (x, y), (minorAxis, majorAxis), angle = cv2.fitEllipse(contours[j])
            eccentricity = np.sqrt(1 - (minorAxis ** 2 / majorAxis ** 2))
            area = cv2.contourArea(contours[j])
            perimeter = cv2.arcLength(contours[j], True)
            metric = (4 * np.pi * area) / perimeter ** 2

            print("----------------------")
            print(f'Eccentricity of object {j+1} in image {i+1} : {eccentricity}')
            print(f'Area of object {j+1} in image {i+1} : {area}')
            print(f'Perimeter of object {j+1} in image {i+1} : {perimeter}')
            print(f'Metric of object {j+1} in image {i+1} : {metric}')

            # Label the form based on metric
            offset = (cx, cy + 20)
            form = "Round" if round(metric, 1) >= 0.7 else "Ellipse"
            cv2.putText(images[i], str(form), offset, cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 0, 0), 1)
        else:
            print(f"Contour {j+1} in image {i+1} has zero area and cannot calculate centroid.")

# Display images
for i in range(len(images)):
    cv2.imshow(f'Gambar {i+1}', images[i])
cv2.waitKey(0)
cv2.destroyAllWindows()
