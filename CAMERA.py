import cv2
cam = cv2.VideoCapture(0)
while cam.isOpened():
    r, frame = cam.read()
    if cv2.waitKey(10) == ord(' '):
      break
    cv2.imshow('CAMERA', frame)