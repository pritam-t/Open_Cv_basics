import cv2 as cv


#Load an image from file
image = cv.imread("open_cv\images\sample.png")


#convert it into gray scale

grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

print("1) Display \n2)Grescale \n3) Save")

user_input = input("Enter your choice: ")


if user_input=='1':
    cv.imshow("Original Image", image)

elif user_input=='2':
    cv.imshow("Gray Scale Image", grey)

elif user_input=='3':
    
    if grey is not None:
        cv.imwrite("open_cv\images\gray_sample.png", grey)
        print("Gray scale image saved successfully.")
        
    else:
        print("Error: Gray scale image not available for saving.")
    
cv.waitKey(0)
cv.destroyAllWindows()