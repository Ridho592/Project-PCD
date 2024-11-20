import cv2
import numpy as np

# Load images
images = [
    cv2.imread("NSP.jpg"),
    cv2.imread("kotak.jpg")
]
iterations = [5, 1]
kernelOpen = np.ones((5, 5), np.uint8)
kernelClose = np.ones((5, 5), np.uint8)

for i in range(len(images)):
    images[i] = cv2.resize(images[i], (600, 600))
    gray = cv2.cvtColor(images[i], cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Perform closing and opening operations on the image
    closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernelClose, iterations=iterations[i])
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernelOpen)

    # Segment the image
    segment = cv2.Canny(opening, 30, 200)
    contours, hierarchy = cv2.findContours(segment, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    segment = cv2.cvtColor(segment, cv2.COLOR_GRAY2RGB)
    cv2.drawContours(images[i], contours, -1, (0, 0, 255), 1)

    # Segmentation, clustering, labeling, and calculating parameters
    centers = []
    for j in range(len(contours)):
        # Clustering and labeling
        moments = cv2.moments(contours[j])
        centers.append((int(moments['m10'] / moments['m00']), int(moments['m01'] / moments['m00'])))
        
        # Draw circle at the centroid
        cv2.circle(images[i], centers[-1], 1, (0, 0, 255), -1)
        cv2.putText(images[i], str(j + 1), centers[-1], cv2.FONT_HERSHEY_DUPLEX, 0.75, (0, 255, 255), 1)
        
        # Calculate parameters
        (x, y), (minorAxis, majorAxis), angle = cv2.fitEllipse(contours[j])
        eccentricity = np.sqrt(1 - (minorAxis ** 2 / majorAxis ** 2))
        area = cv2.contourArea(contours[j])
        perimeter = cv2.arcLength(contours[j], True)
        metric = (4 * np.pi * area) / perimeter ** 2

        # Print parameters
        print("----------------------")
        print(f'Eccentricity of object {j + 1} in image {i + 1}: {eccentricity}')
        print(f'Area of object {j + 1} in image {i + 1}: {area}')
        print(f'Perimeter of object {j + 1} in image {i + 1}: {perimeter}')
        print(f'Metric of object {j + 1} in image {i + 1}: {metric}')

        # Label shape on the image
        offset = (centers[-1][0], centers[-1][1] + 20)
        form = "Round" if round(metric, 1) >= 0.7 else "Ellipse"
        cv2.putText(images[i], form, offset, cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 0, 0), 1)

# Display the images
for i in range(len(images)):
    cv2.imshow(f'Image {i + 1}', images[i])

cv2.waitKey(0)
cv2.destroyAllWindows()
