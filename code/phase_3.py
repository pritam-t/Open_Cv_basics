import cv2 as cv  

image = cv.imread("open_cv/images/resized_sample.png")

#--------------------------------------------------- Draw a Straight Line on the image and save it

# if image is not None:
#     print("Image loaded successfully")
#     pt1=(0,100)
#     pt2=(200,100)
#     color=(0,255,0) # Green color in BGR
#     thixkness=3
    
#     cv.line(image,pt1,pt2,color,thixkness)
#     cv.imshow("Image with Line", image)
#     cv.waitKey(0)
#     cv.destroyAllWindows()
#     cv.imwrite("open_cv/images/line_sample.png", image)
# else:
#     print("Error: Image not found")

#--------------------------------------------------- Draw a Rectangle on the image and save it

# if image is not None:
#     print("Image loaded successfully")
#     top_left=(40,80)
#     bottom_right=(150,220)
#     color=(255,0,0) # Blue color in BGR
#     thickness=2
    
#     cv.rectangle(image,top_left,bottom_right,color,thickness)
#     cv.imshow("Image with Rectangle", image)
#     cv.waitKey(0)
#     cv.destroyAllWindows()
#     cv.imwrite("open_cv/images/rectangle_sample.png", image)

# else:
#     print("Error: Image not found")

#--------------------------------------------------- Draw a Circle on the image and save it

# if image is not None:
#     print("Image loaded successfully")
#     center=(90,140)
#     radius=70
#     color=(0,0,255) # Red color in BGR
#     thickness=3
    
#     cv.circle(image,center,radius,color,thickness)
#     cv.imshow("Image with Circle", image)
#     cv.waitKey(0)
#     cv.destroyAllWindows()
#     cv.imwrite("open_cv/images/circle_sample.png", image)
    
# else:
#     print("Error: Image not found")

#--------------------------------------------------- Draw an Text on the image and save it

if image is not None:
    print("Image loaded successfully")
    text="Black Fang"
    org=(60,70)
    font=cv.FONT_HERSHEY_SIMPLEX
    fontScale=1
    color=(255,255,255) # White color in BGR
    thickness=2
    
    cv.putText(image,text,org,font,fontScale,color,thickness)
    cv.imshow("Image with Text", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    cv.imwrite("open_cv/images/text_sample.png", image)
    
else:
    print("Error: Image not found")