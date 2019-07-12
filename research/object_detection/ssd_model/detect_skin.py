import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
      ret, image = cap.read()
      image_flip = cv2.flip(image, 1)
      gray = cv2.cvtColor(image_flip,cv2.COLOR_BGR2GRAY)
      blur = cv2.GaussianBlur(gray,(5,5),0)
      ret, image_np = cv2.threshold(blur,70,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
      cv2.imshow('Image', image_np)
      if cv2.waitKey(25) & 0xFF == ord('q'):
          cap.release()
          cv2.destroyAllWindows()
          break      
