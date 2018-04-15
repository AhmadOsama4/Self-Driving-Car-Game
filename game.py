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
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

			#draw a black rect => graphics issue
			pygame.draw.rect(self.screen,black,(start_button_x, start_button_y, button_width, button_height))
			pygame.draw.rect(self.screen,black,(exit_button_x, exit_button_y, button_width, button_height))
			
			#White background
			self.screen.fill(white)
			message_display("Self Driving Car Game", 100, self.display_width/2, self.display_height/2)
			#Start Button
			pygame.draw.rect(self.screen, green, (start_button_x, start_button_y, button_width, button_height))
			#Exit Button
			pygame.draw.rect(self.screen, red, (exit_button_x, exit_button_y, button_width, button_height))

			(mouse_x, mouse_y) = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()

			#mouse is clicked
			if click[0] == 1:
				#check if start button is clicked
				if mouse_x >= start_button_x and mouse_x < (mouse_x + button_width) and mouse_y >= start_button_y and mouse_y < (start_button_y + button_height):
					pygame.draw.rect(gameDisplay,blue,(200,400,100,50))
					flag = False

				if mouse_x >= start_button_x and mouse_x < (mouse_x + button_width) and mouse_y >= start_button_y and mouse_y < (start_button_y + button_height):
					pygame.draw.rect(gameDisplay,blue,(500,400,100,50))
					if click[0] == 1:
						pygame.quit()
						quit()

			message_display("Go",40,menu1_x+menu_width/2,menu1_y+menu_height/2)
			message_display("Exit",40,menu2_x+menu_width/2,menu2_y+menu_height/2)
			
			pygame.display.update()
			clock.tick(50)

	def startGame(self):
		intro()
