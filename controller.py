import cv2
import numpy as np 
from directions import Direction

class CarController(object):
	def __init__(self, car_width, car_height, car_x, car_y, road_start_x, road_end_x):
		self.carTemplate = cv2.imread("Images/other_car.png", 0)
		self.signTemplate = cv2.imread("Images/red_sign.png", 0)
		self.signTemplate = cv2.resize(self.signTemplate, (50, 100))

		self.carWidth = car_width
		self.carHeight = car_height
		self.imgHeight = 600
		self.imgWidth = 800
		#road start/end
		self.roadStart = road_start_x
		self.roadEnd = road_end_x
		#position of the main car
		self.carX = car_x
		self.carY = car_y

	def setCarDimensions(self, car_width, car_height):
		self.carWidth = car_width
		self.carHeight = car_height

	def setCarPosition(self, car_x, car_y):
		self.carX = car_x
		self.carY = car_y

	#template matching for the car

	def car_match(self, img, matchvalue = cv2.TM_CCOEFF_NORMED):
		trows, tcols = self.carTemplate.shape[:2]
		# img2 = img.copy()

		result = cv2.matchTemplate(img, self.carTemplate, matchvalue)

		#cv2.normalize(result, result, 0, 255, cv2.NORM_MINMAX)

		loc = np.where(result >= 0.45)
		# if no match found return None
		if loc[0].size == 0:
			return None
		
		mini, maxi, (mx, my), (Mx, My) = cv2.minMaxLoc(
			result)  # We find minimum and maximum value locations in result

		if matchvalue in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:  # For SQDIFF and SQDIFF_NORMED, the best matches are lower values.
			MPx, MPy = mx, my
		else:  # Other cases, best matches are higher values.
			MPx, MPy = Mx, My

		# Normed methods give better results, ie matchvalue = [1,3,5], others sometimes shows errors
		# cv2.rectangle(img2, (MPx, MPy), (MPx + tcols, MPy + trows), (0, 0, 255), 2)

		# cv2.imshow('Car Bounding Box', img2)
		# cv2.waitKey(10)
		#cv2.imshow('output', result)

		return (MPx, MPy, MPx + tcols, MPy + trows)

	#template matching for the sign

	def traffic_match(self, img, matchvalue = cv2.TM_CCOEFF_NORMED):
		trows, tcols = self.signTemplate.shape[:2]
		img2 = img.copy()

		result = cv2.matchTemplate(img, self.signTemplate, matchvalue)

		#cv2.normalize(result, result, 0, 255, cv2.NORM_MINMAX)

		loc = np.where(result >= 0.8)
		# if no match found return None
		if loc[0].size == 0:
			return None

		mini, maxi, (mx, my), (Mx, My) = cv2.minMaxLoc(
			result)  # We find minimum and maximum value locations in result

		if matchvalue in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:  # For SQDIFF and SQDIFF_NORMED, the best matches are lower values.
			MPx, MPy = mx, my
		else:  # Other cases, best matches are higher values.
			MPx, MPy = Mx, My

		# Normed methods give better results, ie matchvalue = [1,3,5], others sometimes shows errors
		#cv2.rectangle(img2, (MPx, MPy), (MPx + tcols, MPy + trows), (0, 0, 255), 2)

		# cv2.imshow('input', img2)
		# cv2.imshow('output', result)

		return (MPx, MPy, MPx + tcols, MPy + trows)

	#Detemine the direction the car should go to: left, right, none
	def getDirection(self, image, car_x, car_y):
		self.setCarPosition(car_x, car_y)

		# matched a traffic sign
		# ret = self.traffic_match(image)
		# if ret is not None:
		# 	#check if sign is red or yellow
		# 	if False: #TODO: check sign color
		# 		return Direction.STOP

		# 	return Direction.FORWARD

		# matched a car
		tmpImg = image[0:int(self.imgHeight - 100), int(self.roadStart):int(self.roadEnd)]
		# cv2.imshow('Extracted', tmpImg)
		ret = self.car_match(tmpImg)
		cv2.waitKey(2)

		if ret is not None:
			x_start, y_start, x_end, y_end = ret
			x_start += self.roadStart
			x_end += self.roadStart

			print('Our Car:', self.carX, self.carX + self.carWidth)
			print('Other Car:', x_start, x_end)
			#Continue forward: no crash will occur
			if (self.carX > x_end) or (self.carX + self.carWidth < x_start):
				return Direction.FORWARD

			#Check if we can go right: will not crash with the right side of the road
			if x_end + self.carWidth < self.roadEnd:
				return Direction.RIGHT 

			return Direction.LEFT
		else:
			print('Car Not Found')
		#if no directions chosen continue forward
		return Direction.FORWARD


