import cv2
import numpy as np

# Load the image
image = cv2.imread('apel.jpg')

# Convert image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert grayscale image to binary using thresholding
_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Use median blur to reduce noise
filtered_image = cv2.medianBlur(binary_image, 5)

# Create a structural element (kernel) for morphology operations
kernel = np.ones((5,5), np.uint8)

# Fill holes inside shapes using closing operation
filled_image = cv2.morphologyEx(filtered_image, cv2.MORPH_CLOSE, kernel)

# Find contours for segmentation
contours, _ = cv2.findContours(filled_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Make a copy of the original image to display segmentation results
segmented_image = image.copy()

# Draw contours and add labels on the segmented image
for i, contour in enumerate(contours):
    # Calculate area
    area = cv2.contourArea(contour)
    
    # Calculate perimeter
    perimeter = cv2.arcLength(contour, True)
    
    # Calculate circularity (metric), avoid division by zero
    circularity = (4 * np.pi * area) / (perimeter ** 2) if perimeter > 0 else 0
    
    # Draw the contour
    cv2.drawContours(segmented_image, [contour], -1, (0, 255, 0), 2)
    
    # Get bounding box for positioning the label
    x, y, w, h = cv2.boundingRect(contour)
    
    # Label each contour with unique ID and measurements
    label = f"ID: {i + 1}, Area: {area:.2f}, Circ: {circularity:.2f}, Peri: {perimeter:.2f}"
    cv2.putText(segmented_image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

# Add k-means clustering to the segmented result
# Convert image to 2D for k-means
Z = segmented_image.reshape((-1, 3))
Z = np.float32(Z)

# Define criteria and number of clusters
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 3  # Number of desired clusters
_, labels, centers = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Convert centers back to uint8 and apply to the image
centers = np.uint8(centers)
clustered_image = centers[labels.flatten()]
clustered_image = clustered_image.reshape((segmented_image.shape))

# Display results
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray_image)
cv2.imshow("Binary", binary_image)
cv2.imshow("Filtering", filtered_image)
cv2.imshow("Morfologi (Filling Hole)", filled_image)
cv2.imshow("Segmentasi dengan Label", segmented_image)
cv2.imshow("Clustering", clustered_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
