import cv2 as cv
import numpy as np


# # Read the image in grayscale mode
# image= cv.imread("open_cv/images/resized_sample.png",cv.IMREAD_GRAYSCALE)
# # Apply Canny edge detection
# edges = cv.Canny(image, 200, 255)
# cv.imshow("Canny Edges", edges)
# cv.waitKey(0)
# cv.destroyAllWindows()
# cv.imwrite("open_cv/images/canny_edges_sample.png", edges)

#----------------------------------------------------------------------------Thresholding the image

# image= cv.imread("open_cv/images/resized_sample.png",cv.IMREAD_GRAYSCALE)
# _, thresholded_image = cv.threshold(image, 80, 200, cv.THRESH_BINARY)
# cv.imshow("Thresholded Image", thresholded_image)
# cv.waitKey(0)
# cv.destroyAllWindows()
# cv.imwrite("open_cv/images/thresholded_sample.png", thresholded_image)

# image1 = np.zeros((300, 300), dtype=np.uint8)
# image2 = np.zeros((300, 300), dtype=np.uint8)

# cv.circle(image1, (150, 150), 100, (255), -1)  # White circle on black background
# cv.rectangle(image2, (50, 50), (250, 250), (255), -1)  # White square on black background
# # Bitwise AND
# bitwise_and = cv.bitwise_and(image1, image2)
# bitwise_or = cv.bitwise_or(image1, image2)
# bitwise_not= cv.bitwise_not(image1)

# cv.imshow("Bitwise AND", bitwise_and)
# cv.imshow("Bitwise OR", bitwise_or)
# cv.imshow("Bitwise NOT", bitwise_not)

# cv.waitKey(0)
# cv.destroyAllWindows()




