import serial
import sys
import cv2

cap = cv2.VideoCapture(0)
COM_PORT = '/dev/ttyUSB0'
BAUD_RATES = 9600
ser = serial.Serial(COM_PORT, BAUD_RATES)
try:
	while True:
		ret, frame = cap.read()
		image_np = cv2.flip(frame, 1)
		cv2.imshow('camera', image_np)
		key = cv2.waitKey(25) & 0xFF
		if key == ord('q'):
			ser.write(b'Q message\n');
		elif key == ord('e'):
			ser.write(b'E message\n');
		


except KeyboardInterrupt:
	ser.close()
	print("bye")
