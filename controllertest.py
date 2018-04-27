import cv2
import numpy as np
from controller import CarController 

car_img = cv2.imread('TestingImages/image_car.png')
green_sign  = cv2.imread('TestingImages/green_sign.png')

cv2.imshow('Car', car_img)
cv2.imshow('Sign', green_sign)
cv2.waitKey(0)
cv2.destroyAllWindows()