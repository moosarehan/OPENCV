import cv2
path = 'images/note.png'
img2 = cv2.imread(path)
img = cv2.imread('images/istockphoto-627966690-612x612.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
adapt=cv2.adaptiveThreshold(gray2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,4)
print(ret)
cv2.imshow('Adaptive',adapt)
cv2.imshow('thresh',thresh)
cv2.waitKey(0)