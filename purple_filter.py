
import numpy as np
import cv2

while(1):
	
	imageFrame = cv2.imread("car5.jpg")

	hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)


	purple_lower = np.array([129, 50, 70], np.uint8)
	purple_upper = np.array([158, 255, 255], np.uint8)
	purple_mask = cv2.inRange(hsvFrame, purple_lower, purple_upper)

	
	kernal = np.ones((5, 5), "uint8")
	
	purple_mask = cv2.dilate(purple_mask, kernal)
	res_purple = cv2.bitwise_and(imageFrame, imageFrame,
							mask = purple_mask)
	
	

	contours, hierarchy = cv2.findContours(purple_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
	
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area > 300):
			x, y, w, h = cv2.boundingRect(contour)
			imageFrame = cv2.rectangle(imageFrame, (x, y),
									(x + w, y + h),
									(0, 0, 255), 2)
			
			cv2.putText(imageFrame, "purple Colour", (x, y),
						cv2.FONT_HERSHEY_SIMPLEX, 1.0,
						(0, 0, 255))	

	cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
	if cv2.waitKey(10) & 0xFF == ord('q'):
		cap.release()
		cv2.destroyAllWindows()
		break

