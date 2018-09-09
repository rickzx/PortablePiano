import pygame, sys, math
import serial
import threading

from config import *
from util import *
from status import *

class Homepage(object):

	def __init__(self):
		self.icon5 = pygame.image.load("media/icon-5.png")
		self.icon6 = pygame.image.load("media/icon-6.png")
		self.icon7 = pygame.image.load("media/icon-7.png")
		self.icon8 = pygame.image.load("media/icon-8.png")
		pygame.font.init()
		self.titlefont = pygame.font.SysFont('comicsansms', 40, bold = True)
		self.word5 = self.titlefont.render("Composing Mode", False, (255,255,255))
		self.word6 = self.titlefont.render("Play Mode", False, (255,255,255))
		self.word7 = self.titlefont.render("Practice Mode", False, (255,255,255))
		self.word8 = self.titlefont.render("Help", False, (255,255,255))
		
		self.word6 = pygame.transform.rotate(self.word6, -36)
		self.word5 = pygame.transform.rotate(self.word5, 36)
		self.w5show = False
		self.w6show = False
		self.w7show = False
		self.w8show = False
		self.icon8 = pygame.transform.rotate(self.icon8, -90)
		self.icon6 = pygame.transform.rotate(self.icon6, -36)
		self.icon5 = pygame.transform.rotate(self.icon5, 36)
		self.icon7 = pygame.transform.rotate(self.icon7, 90)
		(self.icon5x, self.icon5y) = (Config.display_width//2-200, Config.display_height//2-85)
		(self.icon5xF, self.icon5yF) = (self.icon5x-58, self.icon5y-75)
		(self.icon5xS, self.icon5yS) = (self.icon5x, self.icon5y)
		(self.icon6x, self.icon6y) = (Config.display_width//2-25, Config.display_height//2-80)
		(self.icon7x, self.icon7y) = (Config.display_width//2-230, Config.display_height//2+160)
		(self.icon8x, self.icon8y) = (Config.display_width//2+45, Config.display_height//2+160)
		(self.icon6xS, self.icon6yS) = (self.icon6x, self.icon6y)
		(self.icon7xS, self.icon7yS) = (self.icon7x, self.icon7y)
		(self.icon8xS, self.icon8yS) = (self.icon8x, self.icon8y)
		(self.icon6xF, self.icon6yF) = (self.icon6x+58, self.icon6y-75)
		(self.icon7xF, self.icon7yF) = (self.icon7x-65, self.icon7y)
		(self.icon8xF, self.icon8yF) = (self.icon8x+70, self.icon8y)
	
	def expanding(self):
		x, y = pygame.mouse.get_pos()
		if  x<=Config.display_width//2 and x > Config.display_width//2-300 and y <= Config.display_height//2+100 and y >= Config.display_height//2-200:
			(self.icon7x, self.icon7y) = (self.icon7xS, self.icon7yS)
			(self.icon8x, self.icon8y) = (self.icon8xS, self.icon8yS)
			(self.icon6x, self.icon6y) = (self.icon6xS, self.icon6yS)
			(self.icon5x, self.icon5y) = (max(self.icon5xF, self.icon5x-30), max(self.icon5yF, self.icon5y-30))
			self.w6show = False
			self.w5show = True
			self.w7show = False
			self.w8show = False
		elif x>=Config.display_width//2 and x < Config.display_width//2+300 and y <= Config.display_height//2+100 and y >= Config.display_height//2-200:
			(self.icon6x, self.icon6y) = (min(self.icon6xF, self.icon6x+30), min(self.icon6yF, self.icon6y+30))
			self.w6show = True
			self.w5show = False
			self.w7show = False
			self.w8show = False
			(self.icon5x, self.icon5y) = (self.icon5xS, self.icon5yS)
			(self.icon8x, self.icon8y) = (self.icon8xS, self.icon8yS)
			(self.icon7x, self.icon7y) = (self.icon7xS, self.icon7yS)
		elif x<=Config.display_width//3 and y >= Config.display_height//2+100:
			self.w6show = False
			self.w5show = False
			self.w7show = True
			self.w8show = False
			(self.icon7x, self.icon7y) = (max(self.icon7xF, self.icon7x-25), self.icon7yF)
			(self.icon5x, self.icon5y) = (self.icon5xS, self.icon5yS)
			(self.icon8x, self.icon8y) = (self.icon8xS, self.icon8yS)
			(self.icon6x, self.icon6y) = (self.icon6xS, self.icon6yS)
		elif x>=Config.display_width*2//3 and y>= Config.display_height//2+100:
			self.w6show = False
			self.w5show = False
			self.w7show = False
			self.w8show = True
			(self.icon8x, self.icon8y) = (max(self.icon8xF, self.icon8x-25), self.icon8yF)
			(self.icon5x, self.icon5y) = (self.icon5xS, self.icon5yS)
			(self.icon7x, self.icon7y) = (self.icon7xS, self.icon7yS)
			(self.icon6x, self.icon6y) = (self.icon6xS, self.icon6yS)
		else:
			self.w6show = False
			self.w5show = False
			self.w7show = False
			self.w8show = False
			(self.icon5x, self.icon5y) = (self.icon5xS, self.icon5yS)
			(self.icon7x, self.icon7y) = (self.icon7xS, self.icon7yS)
			(self.icon8x, self.icon8y) = (self.icon8xS, self.icon8yS)
			(self.icon6x, self.icon6y) = (self.icon6xS, self.icon6yS)
			
	
			
	
	
	def homeScreen(self):
		gameDisplay = pygame.display.set_mode((Config.display_width, Config.display_height))
		clock = pygame.time.Clock()
	
		intro = True
	
		while intro:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					Status.isQuit = True
					intro = False
					sys.exit()
	
			mouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
	
			gameDisplay.fill(Config.white)
			self.expanding()
			drawImage(gameDisplay, "media/background.jpeg", Config.display_width//2, Config.display_height//2, (Config.display_width,Config.display_height))
			gameDisplay.blit(self.icon8, (self.icon8x, self.icon8y))
			gameDisplay.blit(self.icon6, (self.icon6x, self.icon6y))
			gameDisplay.blit(self.icon5, (self.icon5x, self.icon5y))
			gameDisplay.blit(self.icon7, (self.icon7x, self.icon7y))
			drawImage(gameDisplay, "media/pianoop.png", Config.display_width//2+30, Config.display_height-150, (350,350))
			if (self.w6show):
				gameDisplay.blit(self.word6, (600, 50))
			if (self.w5show):
				gameDisplay.blit(self.word5, (200, 40))
			if (self.w7show):
				gameDisplay.blit(self.word7, (50, 400))
			if (self.w8show):
				gameDisplay.blit(self.word8, (900, 350))
			
			
	
	
			if math.sqrt((mouse[0]-980)**2+(mouse[1]-50)**2) <= 15:
				pygame.draw.circle(gameDisplay, Config.grey, (980,50), 15)
				pygame.draw.line(gameDisplay, Config.black, (970,40), (988,60), 2)
				pygame.draw.line(gameDisplay, Config.black, (988,40), (970,60), 2)
				if click[0] == 1:
					pygame.quit()
					Status.isQuit = True
					intro = False
					sys.exit()
			else:
				pygame.draw.circle(gameDisplay, Config.darkGrey, (980,50), 15)
				pygame.draw.line(gameDisplay, Config.black, (970,40), (988,60), 2)
				pygame.draw.line(gameDisplay, Config.black, (988,40), (970,60), 2)
	
			
			pygame.display.update()
			clock.tick(60)
	
def readFromPort(serialName, serialPort):
	ser = serial.Serial(serialName, serialPort, timeout=1)
	while True:
		if Status.isQuit:
			break
		print (ser.readline())
	
	
def runHomescreen():
	pygame.init()
	#thread = threading.Thread(target=readFromPort, args=('/dev/cu.Bluetooth-Incoming-Port', Config.serialPort,))
	#thread.start()
	h = Homepage()
	h.homeScreen()
	
	
if __name__ == '__main__':
	runHomescreen()