import cv2 as cv  


cap = cv.VideoCapture(0)

# Check if the webcam is opened correctly
# while True:
#     ret, frame = cap.read()
    
#     if not ret:
#         print("Failed to grab frame")
#         break
    
#     cv.imshow("Webcam Feed", frame)
    
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         print("Exiting...")
#         break

# cap.release()
# cv.destroyAllWindows()


frame_width= int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height= int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

codec = cv.VideoWriter_fourcc(*'XVID')

recorded= cv.VideoWriter('recorded_video.avi', codec, 20.0, (frame_width, frame_height))

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame")
        break
    
    recorded.write(frame)
    
    cv.imshow("Webcam Feed", frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        print("Exiting...")
        break
    
recorded.release()
cap.release()
cv.destroyAllWindows()