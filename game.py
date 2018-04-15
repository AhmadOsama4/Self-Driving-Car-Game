import pygame
import time
import random

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
