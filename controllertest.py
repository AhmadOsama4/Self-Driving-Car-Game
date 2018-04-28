import cv2
import numpy as np
from controller import CarController 

road_start_x =  (800 / 2) - 112
road_end_x = (800 / 2) + 112
Controller = CarController(50, 100, 0, 0, road_start_x, road_end_x)

#Car Image
car_img = cv2.imread('TestingImages/image_car.png')
gray_car_img = cv2.cvtColor(car_img, cv2.COLOR_BGR2GRAY)
#Sign Image
green_sign  = cv2.imread('TestingImages/green_sign.png')
gray_green_sign = cv2.cvtColor(green_sign, cv2.COLOR_BGR2GRAY)

###################################################################
###############  Test the car #####################################
tmp = Controller.car_match(gray_car_img)
if tmp is not None:
	a, b, c, d = tmp
	cv2.rectangle(car_img, (a, b), (c, d), (255, 0, 0), 2)
	cv2.imshow('Car', car_img)
	print('Car Detected Correctly')
else:
	print('Incorrect: Output is None')
# No traffic signs
tmp = Controller.traffic_match(gray_car_img)
if tmp is not None:
	a, b, c, d = tmp
	cv2.rectangle(car_img, (a, b), (c, d), (0, 0, 255), 2)
	cv2.imshow('Car', car_img)
	print('Sign detects a car => Incorrect should give None')
else:
	print('Correct: Output is None')

######################################################################
##################   Test Traffic Sign  ##############################
tmp = Controller.traffic_match(gray_green_sign)
if tmp is not None:
	a, b, c, d = tmp
	cv2.rectangle(green_sign, (a, b), (c, d), (0, 0, 255), 2)
	cv2.imshow('Sign', green_sign)
	print('Sign Detected Correctly')
else:
	print('Incorrect: Output is None')

#No cars
tmp = Controller.car_match(gray_green_sign)
if tmp is not None:
	a, b, c, d = tmp
	cv2.rectangle(green_sign, (a, b), (c, d), (255, 0, 0), 2)
	cv2.imshow('Sign', green_sign)
	print('Sign detects car => Incorrect should give None')
else:
	print('Correct: Output is None')

##############
cv2.waitKey(0)
cv2.destroyAllWindows()