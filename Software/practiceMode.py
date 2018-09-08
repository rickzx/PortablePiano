import pygame, sys, math
import serial
import threading

from config import *
from util import *
from status import *
from composingMode import *

def practiceMode():
    
    gameDisplay = pygame.display.set_mode((Config.display_width, Config.display_height))
    clock = pygame.time.Clock()
    practice = True
    while practice:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                Status.isQuit = True
                practice = False
                sys.exit()
        
        gameDisplay.fill(Config.white)
        leftFly = pygame.image.load("media/left.png")
        rightFly = pygame.image.load("media/right.png")
        still = pygame.image.load("media/still.png")
        
        pygame.draw.line(gameDisplay, Config.black, (60,0), (60,600), 3)
        pygame.draw.line(gameDisplay, Config.black, (60, 300), (1024, 300), 3)
        drawImage(gameDisplay, "media/still.png", 80, 270, (40, 60))
        pygame.display.update()
        clock.tick(60)
        

def runPM():
    pygame.init()
    practiceMode()


if __name__ == '__main__':
    runPM()