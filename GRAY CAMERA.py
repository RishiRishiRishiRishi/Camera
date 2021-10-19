import cv2
cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame1 = cam.read()
    gray = cv2.cvtColor(frame1, cv2.COLOR_RGB2GRAY)
    if cv2.waitKey(10) == ord(' '):
      break
    cv2.imshow('CAMERA', gray)
