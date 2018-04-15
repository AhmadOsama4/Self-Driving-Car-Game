import pygame
import time
import random

black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)

class CarGame():
	self __init__():
		self.display_width = 800
		self.display_height = 600
		self.road_width = 360
		#Car, Person, Sign
		self.object_width = 50
		self.object_height = 100
		########################
		pygame.init()
		self.screen = pygame.display.set_mode([self.display_width, self.display_height])
		pygame.display.set_caption("Self Driving Car Game")
		self.clock  = pygame.time.Clock()
		#load images
		self.road = pygame.image.load('Images/road.jpg')
		self.mainCar = pygame.image.load('Images/our_car.png')
		self.otherCar = pygame.image.load('Images/other_car.png')
		self.crash = pygame.image.load('Images/crash.png')
		self.redSign = pygame.image.load('Images/red_sign.png')
		self.yellowSign = pygame.image.load('Images/red_sign.png')
		self.greenSign = pygame.image.load('Images/red_sign.png')

	def introWindow(self):
		flag = True
		#Coordinates and dimensions for start and exit buttons
		start_button_x = 200
		start_button_y = 400
		exit_button_x = 500
		exit_button_y = 400
		button_width = 100
		button_height = 50

		#Wait until exit or start is pressed
		while flag:



	def startGame(self):
		intro()
