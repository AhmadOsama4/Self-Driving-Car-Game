from enum import Enum

class ObjectType(Enum):
	CAR = 0
	PERSON = 1
	SIGN = 2

class GameObject:
	def __init__(self, x, y, w, h, speed, img):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.speed = speed
		self.img = img
	#Getters
	def X(self):
		return self.x
	def Y(self):
		return self.y
	def width(self):
		return self.w	
	def height(self):
		return self.h	
	def Img(self):
		return self.img
	#Setters
	def setX(self, x):
		self.x = x
	def setY(self, y):
		self.y = y
	def setWidth(self, w):
		self.w = w
	def setHeight(self, h):
		self.h = h	
	def setImg(self, img):
		self.img = img

	def moveObject(self):
		self.x += self.speed[0]
		self.y += self.speed[1]
