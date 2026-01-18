import cv2 as cv
image = cv.imread("open_cv/images/resized_sample.png")

if image is None:
    print("Image not loaded")
else:
    guss = cv.GaussianBlur(image, (3,3), 0)
    cv.imshow("Blurred Image", guss)
    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.imwrite("open_cv/images/gaussian_blurred_sample.png", guss)

# if image is None:
#     print("Image not loaded")
# else:
#     med = cv.medianBlur(image,11)
#     cv.imshow("Blurred Image", med)
#     cv.waitKey(0)
#     cv.destroyAllWindows()
#     cv.imwrite("open_cv/images/median_blurred_sample.png", med)

# import numpy as np

# sharpen_kernal = np.array([
#     [0,-1,0],
#     [-1,5,-1],
#     [0,-1,0]
# ])

# if image is None:
#     print("Image not loaded")
# else:
#     sharpened = cv.filter2D(image,-1,sharpen_kernal)
#     cv.imshow("Sharpened Image", sharpened)
#     cv.waitKey(0)
#     cv.destroyAllWindows()
#     cv.imwrite("open_cv/images/sharpened_sample.png", sharpened)


    


    


