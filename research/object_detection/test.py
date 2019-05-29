import requests
import cv2
import numpy as np

cap = cv2.VideoCapture(1)



while True:
	ret, image = cap.read()
	image_np = cv2.resize(image,(1280,720),cv2.INTER_CUBIC)
	cv2.imshow("Cam", image_np)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break;

cap.release()
cv2.destroyAllWindows()
