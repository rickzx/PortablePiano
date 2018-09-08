import pygame, sys, math
import serial
import threading

from config import *
from util import *
from status import *

def composingMode():
    gameDisplay = pygame.display.set_mode((Config.display_width, Config.display_height))
    clock = pygame.time.Clock()
    composing = True
    while composing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                Status.isQuit = True
                composing = False
                sys.exit()
        
        gameDisplay.fill(Config.white)
        
        drawImage(gameDisplay, "media/sheet.png", Config.display_width//2, Config.display_height//2+50, (20,200))
    
        pygame.display.update()
        clock.tick(60)
    
def runCM():
    pygame.init()
    composingMode()
    
if __name__ == '__main__':
    runCM()