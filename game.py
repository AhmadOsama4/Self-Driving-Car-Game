import pygame
import time
import random
from gameobject import *

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
		self.crash = pygame.image.load('Images/crash.png')
		self.redSign = pygame.image.load('Images/red_sign.png')
		self.yellowSign = pygame.image.load('Images/red_sign.png')
		self.greenSign = pygame.image.load('Images/red_sign.png')
		self.person = pygame.image.load('Images/person.png')
		#speed of car and backgroung
		self.carSpeed = 3
		self.bgSpeed = 6
		#
		self.gameObjects = []

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
		bg_Img1_x = self.display_width/2 - (self.road_width / 2)
		bg_Img1_y = 0;
		bg_Img2_x = bg_Img1_x
		bg_Img2_y = -self.display_height

		#initial position of the main car
		car_x = (self.display_width / 2) - (self.object_width / 2)
		car_y = self.display_height - self.object_height
		car_x_change = 0

		exitGame = False

		while not exitGame:
			#to move objects, and stop when meeting a red traffic sign
			move = False
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameExit = True
					pygame.quit()
					quit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						car_x_change = -5
					elif event.key == pygame.K_RIGHT:
						car_x_change = 5

				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
						car_x_change = 0

			car_x += car_x_change

			#Detect Crash
				#TODO:
			###################

			'''
			#move game objects
			for i in range(len(self.gameobjects)):
				self.gameObjects[i].moveObject()

			#get indexes of those objects to be removed
			delObjects = []
			for i in range(len(self.gameobjects)):
				if self.gameobjects[i].Y() > self.display_height or self.gameobjects[i].X() > (self.display_width+self.road_width/2):
					delObjects.push(i)

			#remove object
			for i in delObjects:
				del(self.gameObjects[i])

			#add objects to the screen
			for obj in self.gameObjects:
				self.screen.blit(obj.Img(), (obj.X(), obj.Y()))
			'''
			self.screen.fill(green)

			self.screen.blit(self.mainCar, (car_x, car_y))
			self.screen.blit(self.road, (bg_Img1_x, bg_Img1_y))
			self.screen.blit(self.road, (bg_Img2_x, bg_Img2_y))

			#background images
			bg_Img1_y += self.bgSpeed
			bg_Img2_y += self.bgSpeed

			if bg_Img1_y >= self.display_height:
				bg_Img1_y = -self.display_height

			if bg_Img2_y >= self.display_height:
				bg_Img2_y = -self.display_height

			pygame.display.update() # update the screen
			self.clock.tick(60) # frame per sec

	# add another car, a person or a traffic sign
	def addObject(self):
		oType = ObjectType( random.randrange(2) )
		x, y, w, h, img = 1
		if oType == ObjectType.CAR: #add a car
 			y = -self.display_height
 			#helpers
 			road_start_x =  (self.display_width/2)-112
 			road_end_x = (self.display_width/2)+112
 			####
 			x = random.randrange(road_start_x, road_end_x-self.object_width)
 			w = self.object_width
 			h = self.object_height
 			img = self.otherCar

		elif oType == ObjectType.SIGN: #add a traffic sign
			y = -self.display_height
			x = self.display_width/2 - road_width/2
			w = self.object_width
			h = self.object_height
 			# assign a sign randomly
			if random.randrange(2) == 1:
				img = self.greenSign
			else:
				img = self.redSign

		elif oType == ObjectType.PERSON: #add a person
			y = -self.display_height
			x = self.display_width/2 - road_width/2
			w = self.object_width
			h = self.object_height
			img = self.person

		newObject = GameObject(x, y, w, h, img , oType)
		self.gameObjects.push(newObject)

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