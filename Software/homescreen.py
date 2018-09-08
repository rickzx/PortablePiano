import pygame, sys
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

		gameDisplay.fill(Config.red)
		pygame.display.update()
		clock.tick(15)

def readFromPort(serialPort):
	ser = serial.Serial('/dev/cu.usbmodem1411', serialPort)
	while True:
		print ser.readline()


def main():
	pygame.init()
	thread = threading.Thread(target=readFromPort, args=(Config.serialPort,))
	thread.start()
	homeScreen()


if __name__ == '__main__':
	main()