import cv2
import numpy as np
from controller import CarController 

road_start_x =  (800 / 2) - 112
road_end_x = (800 / 2) + 112
Controller = CarController(50, 100, 0, 0, road_start_x, road_end_x)

car_img = cv2.imread('TestingImages/image_car.png')
green_sign  = cv2.imread('TestingImages/green_sign.png')

#Test the car
a, b, c, d = Controller.car_match(car_img)
cv2.rectangle(car_img, (a, b), (c, d), (0, 0, 255), 2)

cv2.imshow('Car', car_img)
# cv2.imshow('Sign', green_sign)
cv2.waitKey(0)
cv2.destroyAllWindows()