import cv2
img = cv2.imread('images/istockphoto-627966690-612x612.jpg')
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('rgb',rgb)
cv2.imshow('hsv',hsv)
cv2.imshow('gray',gray)
cv2.waitKey(0)

