import pygame, sys, math
import serial
import threading

from config import *
from util import *
from status import *
from homepage import *

def loadingScreen():
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

		drawImage(gameDisplay, "media/logo.png", Config.display_width//2, Config.display_height//2 - 30, (500, 500))
		drawText(gameDisplay, "P I A N E E R", Config.display_width//2, Config.display_height//2 + 50, "Courier New", 30, Config.black)

		rect = pygame.Surface((Config.display_width, Config.display_height), pygame.SRCALPHA)
		rect.fill((255,255,255,Status.loadingAlpha))
		gameDisplay.blit(rect,(Status.loadingSec,0))

		if Status.loadingAlpha <= 253 and Status.loadingSec > 100:
			Status.loadingAlpha = Status.loadingAlpha + 5  
		else:
			Status.loadingAlpha

		
		pygame.display.update()

		Status.loadingSec += 1
		if Status.loadingSec == Status.loadingLimit:
			intro = False
			runHomepage()

		clock.tick(60)


def main():
	pygame.init()
	loadingScreen()

if __name__ == '__main__':
	main()