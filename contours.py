import cv2
path = 'images/birds.jpg'
img = cv2.imread(path)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray,12,255,cv2.THRESH_BINARY_INV)
contours,heirarchy=cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,255,0),4)
cv2.imshow('frame',img)
cv2.waitKey(0)