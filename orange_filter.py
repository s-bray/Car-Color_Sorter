
import numpy as np
import cv2

while(1):
	
	imageFrame = cv2.imread("car6.jpg")

	hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)


	orange_lower = np.array([10, 50, 70], np.uint8)
	orange_upper = np.array([24, 255, 255], np.uint8)
	orange_mask = cv2.inRange(hsvFrame, orange_lower, orange_upper)

	
	kernal = np.ones((5, 5), "uint8")
	
	orange_mask = cv2.dilate(orange_mask, kernal)
	res_orange = cv2.bitwise_and(imageFrame, imageFrame,
							mask = orange_mask)
	
	

	contours, hierarchy = cv2.findContours(orange_mask,
										cv2.RETR_TREE,
										cv2.CHAIN_APPROX_SIMPLE)
	
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area > 300):
			x, y, w, h = cv2.boundingRect(contour)
			imageFrame = cv2.rectangle(imageFrame, (x, y),
									(x + w, y + h),
									(0, 0, 255), 2)
			
			cv2.putText(imageFrame, "orange Colour", (x, y),
						cv2.FONT_HERSHEY_SIMPLEX, 1.0,
						(0, 0, 255))	

	cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
	if cv2.waitKey(10) & 0xFF == ord('q'):
		cap.release()
		cv2.destroyAllWindows()
		break

