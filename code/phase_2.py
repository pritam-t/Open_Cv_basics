import cv2 as cv 

image = cv.imread("open_cv/images/resized_sample.png")


#--------------------------------------------------- Resize the image and save it
# if image is not None:
#     print("Image loaded successfully")
    
#     resized_image= cv.resize(image,(300,300))
#     cv.imshow("Resized Image", resized_image)
#     cv.waitKey(0)
#     cv.destroyAllWindows()
#     cv.imwrite("open_cv/images/resized_sample.png", resized_image)

# else:
#     print("Error: Image not found")

#--------------------------------------------------- Slice the image and save it

# if image is not None:
#     sliced_image = image[100:200, 50:150]
#     cv.imshow("Sliced Image", sliced_image)
#     cv.waitKey(0)
#     cv.destroyAllWindows()
#     cv.imwrite("open_cv/images/sliced_sample.png", sliced_image)
# else:
#     print("Error: Image not found")

#--------------------------------------------------- Rotate the image and save it

# if image is not None:
    
#     size = (image.shape[1], image.shape[0])  # (width, height)
#     center = (size[0] // 2, size[1] // 2)
#     angle = 90
#     scale = 1.0
#     formula = cv.getRotationMatrix2D(center, angle, scale)
#     rotated_image = cv.warpAffine(image, formula, size)
#     cv.imshow("Rotated Image", rotated_image)
#     cv.waitKey(0)
#     cv.destroyAllWindows()
#     cv.imwrite("open_cv/images/rotated_sample.png", rotated_image)

# else:
#     print("Error: Image not found")

#--------------------------------------------------- Flip the image and save it

if image is not None:
    flipped_image = cv.flip(image, 1)  # Horizontal flip
    cv.imshow("Flipped Image", flipped_image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.imwrite("open_cv/images/flipped_sample.png", flipped_image)

else:
    print("Error: Image not found")