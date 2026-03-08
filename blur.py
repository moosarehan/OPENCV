import cv2
img = cv2.imread('images/balloons_noisy.png')

# normal blur
blur=cv2.blur(img,(10,10))
guassblur=cv2.GaussianBlur(img,(7,7),0)
medianblur=cv2.medianBlur(img,5)
cv2.imshow('guassblur',guassblur)
cv2.imshow('blur',blur)
cv2.imshow('median',medianblur)
cv2.waitKey(0)
