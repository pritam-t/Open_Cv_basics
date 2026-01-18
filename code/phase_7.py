import cv2 as cv

#Read the image & Convert to grayscale
image=  cv.imread("open_cv/images/circle.jpg")
image= cv.resize(image,(600,600))
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

#Apply thresholding
_,thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)

#Find contours
contours, heirarchy = cv.findContours(thresh,cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

#Draw the contours
cv.drawContours(image,contours, -1, (0,255,0), 3)

for contour in contours:
    approx= cv.approxPolyDP(contour,0.01*cv.arcLength(contour,True),True)
    
    corners= len(approx)
    
    if corners == 3:
        shape_name= "Triangle"
    
    elif corners == 4:
        shape_name= "Rectangle"
        
    elif corners == 5:
        shape_name= "Pentagon"
        
    else:
        shape_name = "Unknown"
        
    cv.drawContours(image,[approx],0,(0,255,0),2)
    x= approx.ravel()[0]
    y= approx.ravel()[1]-10                                                                                                                                                                                                                 
    cv.putText(image,shape_name,(x,y),cv.FONT_HERSHEY_COMPLEX,0.6,(255))
    
    
cv.imshow("Contours", image)
cv.waitKey(0)
cv.destroyAllWindows()




