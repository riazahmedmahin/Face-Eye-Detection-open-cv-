



import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
cap = cv2.VideoCapture('stock-footage-kid-child-girl-making-online-video-call-recording-vlog-sitting-on-sofa-portrait-funny-girl2.webm')

while cap.isOpened():
    _, img = cap.read()
    font = cv2.FONT_ITALIC
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y , w ,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255 , 0), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey ,ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 255, 0), 3)
            date = str(datetime.datetime.now())
            img = cv2.putText(img, date, (10, 50), font, 1, (0, 0, 0), 2, cv2.LINE_AA)

    # Display the output
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

cap.release()









