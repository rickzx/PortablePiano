import pygame, sys, math
import serial
import threading

from config import *
from util import *
from status import *
from staff import *
from metronome import *

def playSound(serialStr):
	if serialStr == 'c':
		Sound.C.play()
	elif serialStr == 'cn':
		Sound.C.stop()
	elif serialStr == 'c#':
		Sound.Cs.play()
	elif serialStr == 'c#n':
		Sound.Cs.stop()
	elif serialStr == 'd':
		Sound.D.play()
	elif serialStr == 'dn':
		Sound.D.stop()
	elif serialStr == 'd#':
		Sound.Ds.play()
	elif serialStr == 'd#n':
		Sound.Ds.stop()
	elif serialStr == 'e':
		Sound.E.play()
	elif serialStr == 'en':
		Sound.E.stop()
	elif serialStr == 'f':
		Sound.F.play()
	elif serialStr == 'fn':
		Sound.F.stop()
	elif serialStr == 'f#':
		Sound.Fs.play()
	elif serialStr == 'f#n':
		Sound.Fs.stop()
	elif serialStr == 'g':
		Sound.G.play()
	elif serialStr == 'gn':
		Sound.G.stop()
	elif serialStr == 'g#':
		Sound.Gs.play()
	elif serialStr == 'g#n':
		Sound.Gs.stop()
	elif serialStr == 'a':
		Sound.A.play()
	elif serialStr == 'an':
		Sound.A.stop()
	elif serialStr == 'a#':
		Sound.As.play()
	elif serialStr == 'a#n':
		Sound.As.stop()
	elif serialStr == 'b':
		Sound.B.play()
	elif serialStr == 'bn':
		Sound.B.stop()


def composition():
	gameDisplay = pygame.display.set_mode((Config.display_width, Config.display_height))
	clock = pygame.time.Clock()
	background = pygame.Surface((gameDisplay.get_size()))

	intro = True
	pygame.mixer.init()

	staffGroup = pygame.sprite.Group()
	metronomeGroup = pygame.sprite.Group()
	allGroups = pygame.sprite.LayeredUpdates()

	Staff.groups = staffGroup, allGroups
	Metronome.groups = metronomeGroup, allGroups
	Staff._layer = 1
	Metronome._layer = 2

	staff = Staff(0, 0)
	metronome = Metronome(0, 500)

	while intro:
		milliseconds = clock.tick_busy_loop(Config.fps)  # milliseconds passed since last frame
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

def readFromPort(serialName, serialPort):
	try:
		ser = serial.Serial(serialName, serialPort, timeout=1)
		while True:
			if Status.isQuit:
				break
			line = ser.readline().strip()
			print ("1")
			if line:
				print (line)
				Status.curNote = line
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