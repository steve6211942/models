import cv2

for x in range(320):
	image = cv2.imread('images/train_img/up_' + str(x+1) + '.jpg')
	image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	cv2.imwrite('images/tmp/up_' + str(x+1) + '.jpg', image_grey)
