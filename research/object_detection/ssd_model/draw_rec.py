import numpy as np
import cv2

cap = cv2.VideoCapture(0)
width = cap.get(3)
height = cap.get(4)
width -= 15
height -= 15
min_x = 0
min_y = 0
max_x = 100
max_y = 100
status = 0

while True:
	ret, frame = cap.read()
	image_np = cv2.flip(frame,1)
	cv2.rectangle(image_np, (min_x, min_y), (max_x, max_y), (0, 255, 0), 2)
	crop_img = image_np[min_y:max_y, min_x:max_x]
	cv2.imshow('camera', image_np)
	cv2.imshow('crop', crop_img)
	key = cv2.waitKey(25) & 0xFF
	if status == 0:
		if key == ord('w'):
			if min_y >= 15:
				min_y -= 15
				max_y -= 15
		elif key == ord('a'):
			if min_x >= 15:
				min_x -= 15
				max_x -= 15
		elif key == ord('s'):
			if max_y <= height:
				min_y += 15
				max_y += 15
		elif key == ord('d'):
			if max_x <= width:
				min_x += 15
				max_x += 15
		elif key == ord('q'):
			if max_x <= width and max_y <= height and min_x >= 15 and min_y >= 15:
				min_x -= 15
				min_y -= 15
				max_x += 15
				max_y += 15
		elif key == ord('e'):
			if max_x-min_x >= 100:
                                min_x += 15
                                min_y += 15
                                max_x -= 15
                                max_y -= 15
		elif key == 32:
			status += 1;
	if key == 27:
		cap.release()
		cv2.destroyAllWindows()
		break
