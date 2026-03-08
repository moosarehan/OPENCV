import cv2
#reading an image from  local disk
img = cv2.imread('image/istockphoto-627966690-612x612.jpg')

# writing the image to the local dist
cv2.imwrite('image/outout.jpg',img)

#displaying an image
cv2.imshow('FRAME',img)
cv2.waitKey(0)