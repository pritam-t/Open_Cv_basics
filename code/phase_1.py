import cv2 as cv

#====================================================Read an image from file
image = cv.imread("open_cv\images\sample.png")

#=---------------------------------------------------Display the image in a window
# if image is not None:
#     cv.imshow("Sample Image", image)
#     cv.waitKey(0)
#     cv.destroyAllWindows()

# else:
#     print("Error: Could not read the image.")
    
#--------------------------------------------------- Save the image to a new file
# if image is not None:
#     success= cv.imwrite("open_cv\images\output_sample.png", image)
#     if success:
#         print("Image saved successfully:", success)
#     else:
#         print("Error: Could not save the image.")

#--------------------------------------------------- Get image properties
# if image is not None:
#     h,w,c = image.shape
#     print("Height:", h)
#     print("Width:", w)
#     print("Channels:", c)  
# else:
#     print("Error: Could not read the image.")
    
#--------------------------------------------------- Convert image to grayscale

if image is not None:
    gray= cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("Grayscale Image", gray)
    cv.waitKey(0) 
    cv.destroyAllWindows()
else:
    print("Error: Could not read the image.")