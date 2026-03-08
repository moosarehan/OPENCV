import cv2
path = 'images/pexels-roshan-kamath-793618-1661179.jpg'
img = cv2.imread(path)

# visualizng the original image
print(img.shape)
cv2.imshow('img',img)
cv2.waitKey(0)

#cropped image
crop=img[200:400,500:1000]
cv2.imshow('crop',crop)
cv2.waitKey(0)


#resize
resize=cv2.resize(img,(400,300))
cv2.imshow('resize',resize)
cv2.waitKey(0)