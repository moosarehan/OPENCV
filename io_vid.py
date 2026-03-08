import cv2

# Path to the video file inside the 'image' folder
video_path = 'images/Urban Environmental Intelligence Engine - Opera 2026-03-01 23-17-07.mp4'

video=cv2.VideoCapture(video_path)

#visuaqlizng a video
ret=True
while ret:
    ret,frame=video.read()
    if ret:
        cv2.imshow('frame',frame)
        cv2.waitKey(25)
    
video.release()
cv2.destroyAllWindows()
