import cv2 as cv 


path = input("Enter the path/name of the image: ")
image= cv.imread(path)

opt=image

print("Choose the shape to draw on the image:")
print("1. Line\n2. Rectangle\n3. Circle\n4. Text")
num =input("Enter the number: : ")

clr=(255,255,255)
thixkness=3

if image is not None:
    if num == '1':
        pt1=(0,100)
        pt2=(200,100)
        opt= cv.line(image,pt1,pt2,clr,thixkness)
    
    elif num == '2':
        top_left=(40,80)
        bottom_right=(150,220)
        opt= cv.rectangle(image,top_left,bottom_right,clr,thixkness)
    
    elif num == '3':
        center=(90,140)
        radius=70
        opt= cv.circle(image,center,radius,clr,thixkness)
    
    elif num == '4':
        text = "OpBLACK"
        org = (50, 50)  
        font = cv.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        opt= cv.putText(image, text, org, font, fontScale, clr, thixkness, cv.LINE_AA)
    else:
        print("Invalid input")
        
    cv.imshow("Image with Shape", opt)
    cv.waitKey(0)
    cv.destroyAllWindows()

print("User want to save image ? (y/n): ")
save = input().lower()

if save == 'y':
    cv.imwrite("open_cv/images/ass_2.png",opt)
    print("Image saved successfully")
    
        
        