import cv2
from shape_detection import detect_shape
# Opens the Video file
cap= cv2.VideoCapture('./20210826_101644.mp4')
i=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    detect_shape(frame)
    i+=1

cap.release()
cv2.destroyAllWindows()
