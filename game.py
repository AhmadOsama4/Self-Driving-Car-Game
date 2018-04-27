import pygame
import time
import random
import cv2
import numpy as np
from directions import Direction


black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)

class CarGame():
	def __init__(self):
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
		self.crashImg = pygame.image.load('Images/crash.png')
		self.redSign = pygame.image.load('Images/red_sign.png')
		self.redSign = pygame.transform.scale(self.redSign, (50, 100))

		self.yellowSign = pygame.image.load('Images/yellow_sign.png')
		self.yellowSign = pygame.transform.scale(self.yellowSign, (50, 100))

		self.greenSign = pygame.image.load('Images/green_sign.png')
		self.greenSign = pygame.transform.scale(self.greenSign, (50, 100))

		self.person = pygame.image.load('Images/person.png')
		#speed of car and backgroung
		self.personSpeed = 0
		self.carSpeed = 0
		self.bgSpeed = 0
		#
		self.gameObjects = []
		self.isRedSign = False
		self.objectX = 0
		self.objectY = 0
		self.curObject = -1
		self.curObjectImage = -1
		self.bg_Img1_x = self.display_width/2 - (self.road_width / 2)
		self.bg_Img1_y = 0;
		self.bg_Img2_x = self.bg_Img1_x
		self.bg_Img2_y = -self.display_height
		self.car_x = -1
		self.car_y = -1
		self.car_x_change = 0
		self.counter = 1

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
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

			#draw a black rect => graphics issue
			pygame.draw.rect(self.screen,black,(start_button_x, start_button_y, button_width, button_height))
			pygame.draw.rect(self.screen,black,(exit_button_x, exit_button_y, button_width, button_height))
			
			#White background
			self.screen.fill(white)

			#self.message_display("Self Driving Car Game", 80, self.display_width/2, self.display_height/2)
			self.message_display("Welcome to our", 60, self.display_width/2, 100)
			self.message_display("Self Driving Car Game", 60, self.display_width/2, 200)
			#Start Button
			pygame.draw.rect(self.screen, green, (start_button_x, start_button_y, button_width, button_height))
			#Exit Button
			pygame.draw.rect(self.screen, red, (exit_button_x, exit_button_y, button_width, button_height))

			(mouse_x, mouse_y) = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()

			#mouse is clicked
			if click[0] == 1:
				#check if start button is clicked
				if mouse_x >= start_button_x and mouse_x < (start_button_x + button_width) and mouse_y >= start_button_y and mouse_y < (start_button_y + button_height):
					flag = False
					print('Start Button Clicked')

				if mouse_x >= exit_button_x and mouse_x < (exit_button_x + button_width) and mouse_y >= exit_button_y and mouse_y < (exit_button_y + button_height):
					if click[0] == 1:
						print('Exit Button Clicked')
						pygame.quit()
						quit()
			else:
				#change button color on hover
				if mouse_x >= start_button_x and mouse_x < (start_button_x + button_width) and mouse_y >= start_button_y and mouse_y < (start_button_y + button_height):
					pygame.draw.rect(self.screen, blue, (start_button_x, start_button_y, button_width, button_height))
				elif mouse_x >= exit_button_x and mouse_x < (exit_button_x + button_width) and mouse_y >= exit_button_y and mouse_y < (exit_button_y + button_height):
					pygame.draw.rect(self.screen, blue, (exit_button_x, exit_button_y, button_width, button_height))

			self.message_display("Start", 40, start_button_x + button_width/2, start_button_y + button_height/2)
			self.message_display("Exit", 40, exit_button_x + button_width/2, exit_button_y + button_height/2)
			
			pygame.display.update()
			self.clock.tick(50)

	def gameLoop(self):
		#initial position of the main car
		self.car_x = (self.display_width / 2) - (self.object_width / 2)
		self.car_y = self.display_height - self.object_height
		
		self.addObject()
		exitGame = False
		self.car_x_change = 0		
		while not exitGame:
			exitGame = self.gameController()			
			#check if crash occurs
			self.checkCrash(self.car_x, self.car_y)
			
			self.screen.fill(green)
			self.screen.blit(self.road, (self.bg_Img1_x, self.bg_Img1_y))
			self.screen.blit(self.road, (self.bg_Img2_x, self.bg_Img2_y))
			self.screen.blit(self.mainCar, (self.car_x, self.car_y))
			self.screen.blit(self.curObjectImage, (self.objectX, self.objectY))

			self.moveObjects()
			#object went out of the page
			if self.objectY > self.display_height:
				self.addObject()

			if self.curObject == 1:
				self.counter += 1
				#change sign to yellow
				if self.counter >= 120 and self.counter < 240:
					self.curObjectImage = self.yellowSign
				#change sign to green
				elif self.counter >= 240:
					self.isRedSign = False
					self.curObjectImage = self.greenSign
			
			# get the image of the game
			pg_img = pygame.display.get_surface()
			color_image = pygame.surfarray.array3d(pg_img)

			color_image = cv2.transpose(color_image)
			color_image = cv2.cvtColor(color_image, cv2.COLOR_RGB2BGR)
			g = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

			# --- display CV2 image ---
			#car_match(4, g)
			# traffic_match(4,g)

			# cv2.imshow('Color', color_image)
			# cv2.waitKey(1)
			#cv2.destroyAllWindows()
			pygame.display.update() # update the screen
			self.clock.tick(60) # frame per sec


	def gameController(self):		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			#left or right buttons prssed
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					self.car_x_change = -5
				elif event.key == pygame.K_RIGHT:
					self.car_x_change = 5
			#up button pressed
				elif event.key == pygame.K_UP:
					self.personSpeed = 2
					self.carSpeed = 3
					self.bgSpeed = 6
			#left or right buttons released			
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					self.car_x_change = 0
			#UP button released
				elif event.key == pygame.K_UP:
					self.personSpeed = 0
					self.carSpeed = -3
					self.bgSpeed = 0
		self.car_x += self.car_x_change
		

	# add another car, a person or a traffic sign
	def addObject(self):
		#random object
		self.curObject = random.randrange(1000) % 2
		#self.curObject = 1
		self.isRedSign = False
		if self.curObject == 0: # add a car
			road_start_x =  (self.display_width/2)-112
			road_end_x = (self.display_width/2)+112
			self.objectX = random.randrange(road_start_x,road_end_x-self.object_width)
			self.curObjectImage = self.otherCar

		elif self.curObject == 1: # add a sign
			self.isRedSign = True
			self.objectX = self.display_width/2 - 140 - self.object_width/2
			self.curObjectImage = self.redSign
		else: # add a person
			self.curObjectImage = self.person

		self.counter = 0
		self.objectY = -200
	
	def moveObjects(self):
		
		self.bg_Img1_y += self.bgSpeed
		self.bg_Img2_y += self.bgSpeed

		#move the background
		if self.bg_Img1_y >= self.display_height:
			self.bg_Img1_y = -self.display_height

		if self.bg_Img2_y >= self.display_height:
			self.bg_Img2_y = -self.display_height

		#move objects
		if self.curObject == 0: #car
			self.objectY += self.carSpeed
		elif self.curObject == 1: #sign
			self.objectY += self.bgSpeed
		else: #person
			self.objectX += self.personSpeed

	def checkCrash(self, car_x, car_y):
		road_start_x = (self.display_width/2) - 112
		road_end_x = (self.display_width/2) + 112

		#check crashing with the sides of the road
		if car_x < road_start_x:
			self.crash(car_x - self.object_width, car_y)
		if car_x > road_end_x - self.object_width:
			self.crash(car_x , car_y)

		#check crashing with a car
		if self.curObject == 0 and car_y < self.objectY + self.object_height:
			if car_x >= self.objectX and car_x <= self.objectX + self.object_width:
				self.crash(car_x-25, car_y-self.object_height/2)
			if car_x + self.object_width >= self.objectX and car_x+self.object_width <= self.objectX+self.object_width:
				self.crash(car_x, car_y-self.object_height/2)

		#check passing a traffic light
		if self.curObject == 1 and self.isRedSign:
			if car_y < self.objectY + self.object_height:
				self.crash(car_x , car_y - 50)

	def crash(self, x, y):
		self.screen.blit(self.crashImg, (x, y))
		self.message_display("Crashed", 115, self.display_width/2, self.display_height/2)
		pygame.display.update()
		time.sleep(2)
		self.gameLoop() #restart the game

	def text_objects(self, text,font):
		textSurface = font.render(text,True,black)
		return textSurface, textSurface.get_rect()

	def message_display(self, text, size, x, y):
		font = pygame.font.Font("freesansbold.ttf", size)
		text_surface , text_rectangle = self.text_objects(text, font)
		text_rectangle.center =(x, y)
		self.screen.blit(text_surface, text_rectangle)

	def startGame(self):
		self.introWindow()
		self.gameLoop()