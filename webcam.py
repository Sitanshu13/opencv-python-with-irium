import cv2, time

video = cv2.VideoCapture(1)

a=0

while True:
    a=a+1
    
    check, frame = video.read()
    print(check)
    print(frame)

    cv2.imshow("Capturing", frame)

    key=cv2.waitKey(1)
    if key == 27:
        break
    else:
        cv2.imshow("Please press the escape(esc) key to stop the video", frame)

print(a)

video.release()