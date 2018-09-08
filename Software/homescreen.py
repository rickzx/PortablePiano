import pygame, sys, math
import serial
import threading
from config import *
from util import *

def homeScreen():
	gameDisplay = pygame.display.set_mode((Config.display_width, Config.display_height))
	clock = pygame.time.Clock()

	intro = True

	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				intro = False
				sys.exit()

			mouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()

		gameDisplay.fill(Config.black)

		if math.sqrt((mouse[0]-980)**2+(mouse[1]-50)**2) <= 15:
			pygame.draw.circle(gameDisplay, Config.grey, (980,50), 15)
			pygame.draw.line(gameDisplay, Config.black, (970,40), (988,60), 2)
			pygame.draw.line(gameDisplay, Config.black, (988,40), (970,60), 2)
			if click[0] == 1:
				pygame.quit()
				intro = False
				sys.exit()
		else:
			pygame.draw.circle(gameDisplay, Config.darkGrey, (980,50), 15)
			pygame.draw.line(gameDisplay, Config.black, (970,40), (988,60), 2)
			pygame.draw.line(gameDisplay, Config.black, (988,40), (970,60), 2)

		
		pygame.display.update()
		clock.tick(15)

def readFromPort(serialName, serialPort):
	ser = serial.Serial(serialName, serialPort)
	while True:
		print ser.readline()


def main():
	homeScreen()
	thread = threading.Thread(target=readFromPort, args=('/dev/cu.usbmodem1411', Config.serialPort,))
	thread.start()


if __name__ == '__main__':
	main()