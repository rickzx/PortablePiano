import pygame, sys, math
import serial
import threading

from config import *
from util import *
from status import *

def homePage():
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

		drawImage(gameDisplay, "media/background.jpg", Config.display_width//2, Config.display_height//2, (Config.display_width,Config.display_height))
		drawText(gameDisplay, "P I A N E E R", Config.display_width//2, Config.display_height//2 + 180, "Courier New", 30, Config.black)

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
	try:
		ser = serial.Serial(serialName, serialPort, timeout=1)
		while True:
			if Status.isQuit:
				break
			print ser.readline()
	except:
		pass


def runHomepage():
	pygame.init()
	thread = threading.Thread(target=readFromPort, args=('/dev/cu.usbmodem1411', Config.serialPort,))
	thread.start()
	homePage()


if __name__ == '__main__':
	runHomepage()