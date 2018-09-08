import pygame, sys, math
import serial
import threading

from config import *
from util import *
from status import *
from staff import *

def playSound(serialStr):
	if serialStr == 'a':
		Sound.C.play()
	elif serialStr == 'b':
		Sound.Cs.play()
	elif serialStr == 'c':
		Sound.D.play()
	elif serialStr == 'd':
		Sound.Ds.play()
	elif serialStr == 'e':
		Sound.E.play()
	elif serialStr == 'f':
		Sound.F.play()
	elif serialStr == 'g':
		Sound.Fs.play()
	elif serialStr == 'h':
		Sound.G.play()
	elif serialStr == 'i':
		Sound.Gs.play()
	elif serialStr == 'j':
		Sound.A.play()
	elif serialStr == 'k':
		Sound.As.play()
	elif serialStr == 'l':
		Sound.B.play()


def composition():
	gameDisplay = pygame.display.set_mode((Config.display_width, Config.display_height))
	clock = pygame.time.Clock()
	background = pygame.Surface((gameDisplay.get_size()))

	intro = True
	pygame.mixer.init()

	staffGroup = pygame.sprite.Group()
	allGroups = pygame.sprite.LayeredUpdates()

	Staff.groups = staffGroup, allGroups
	Staff._layer = 1

	staff = Staff()

	while intro:
		milliseconds = clock.tick(Config.fps)  # milliseconds passed since last frame
		seconds = milliseconds / 1000.0

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				Status.isQuit = True
				intro = False
				sys.exit()

		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		gameDisplay.fill(Config.white)

		allGroups.clear(gameDisplay, background)
		allGroups.update(seconds)
		allGroups.draw(gameDisplay)


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
			line = ser.readline()
			print line
			if line and line[0].isalpha():
				print line[0]
				Status.curNote = line[0]
				playSound(Status.curNote)

	except:
		pass


def runComposition():
	pygame.init()
	thread = threading.Thread(target=readFromPort, args=('/dev/cu.usbmodem1411', Config.serialPort,))
	thread.start()
	composition()


if __name__ == '__main__':
	runComposition()