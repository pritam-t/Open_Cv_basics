import cv2 as cv

# Load Haar Cascades
face_cascade = cv.CascadeClassifier(
    r"open_cv/resources/haarcascade_frontalface_default.xml"
)
eye_cascade = cv.CascadeClassifier(
    r"open_cv/resources/haarcascade_eye.xml"
)
smile_cascade = cv.CascadeClassifier(
    r"open_cv/resources/haarcascade_smile.xml"
)

# Open webcam
capture = cv.VideoCapture(0)

while True:
    ret, frame = capture.read()
    if not ret:
        print("Failed to grab frame")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        # Draw face rectangle
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Region of Interest (Face area)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Eye detection
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        if len(eyes) > 0:
            cv.putText(
                frame,
                "Eyes Detected",
                (x, y - 30),
                cv.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

        # Smile detection
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 20)
        if len(smiles) > 0:
            cv.putText(
                frame,
                "Smiling",
                (x, y - 10),
                cv.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    # Show frame
    cv.imshow("Smart Face Detector", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
