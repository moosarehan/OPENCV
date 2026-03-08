import cv2

web=cv2.VideoCapture(0)# 0 for webcam
# vsiaulzing the webcam
while True:
    ret,frame=web.read()
    cv2.imshow('frame',frame)
    key=cv2.waitKey(25)
    if key==ord('q'):
        break
web.release()
cv2.destroyAllWindows()
