import pygame, sys, math
import serial
import threading

from config import *
from util import *
from status import *
from composition import *
import pygame.gfxdraw
import keyboard as kb
from homescreen import *

class PracticePage():

    def __init__(self):
        self.practice = True
        self.clock = pygame.time.Clock()

        self.gameDisplay = pygame.display.set_mode((Config.display_width, Config.display_height))
        self.gameDisplay.fill(Config.white)
        pygame.font.init()
        self.menufont = pygame.font.SysFont('comicsansms', 25, bold = False)
        self.user = self.menufont.render("User", False, (255,255,255))
        self.home = self.menufont.render("Home", False, (255,255,255))
        
        self.background = pygame.image.load('media/batmanBg.jpg')
        self.background = pygame.transform.scale(self.background,(964,566))
        self.userIcon = pygame.image.load('media/ui icons/batman.jpg')
        self.homeIcon = pygame.image.load('media/ui icons/thor.jpg')
        self.userIcon = pygame.transform.scale(self.userIcon,(50,50))
        self.homeIcon = pygame.transform.scale(self.homeIcon,(50,50))
        self.batIcon = pygame.image.load('media/batIcon.png')
        self.batIcon = pygame.transform.scale(self.batIcon,(200,115))
        self.whiteKeys = ['C2','D2','E2','F2','G2','A2','B2',
                     'C3','D3','E3','F3','G3','A3','B3',
                     'C4','D4','E4','F4','G4','A4','B4']
        self.keys = ['C2','C#2','D2','D#2','E2','F2','F#2','G2','G#2','A2','A#2','B2',
                     'C3','C#3','D3','D#3','E3','F3','F#3','G3','G#3','A3','A#3','B3',
                     'C4','C#4','D4','D#4','E4','F4','F#4','G4','G#4','A4','A#4','B4']
        self.blackKeys = ['C#2','D#2','F#2','G#2','A#2',
                     'C#3','D#3','F#3','G#3','A#3',
                     'C#4','D#4','F#4','G#4','A#4']
        self.lightDelta = 18
        self.leftLimPie = 60
        self.rightLimPie = 1024
        self.leftEnd = 60
        self.rightEnd = 60 + 3 * (45.9)#the width of each key is 45.9
        self.leftmostHighKey = None
        self.myKeyboard = kb.Keyboard(60,400)
    
    def highlightBlack(self,keysToBeHigh,keysToBeHighInd):
        min = keysToBeHighInd[0]
        max = keysToBeHighInd[2]
        mid = keysToBeHighInd[1]
        real_min = self.keys.index(self.whiteKeys[min])
        real_max = self.keys.index(self.whiteKeys[max])
        real_mid = self.keys.index(self.whiteKeys[mid])
        black = []
        if (real_min == real_mid - 2):
            black += [self.keys[real_min+1]]
        if (real_max == real_mid + 2):
            black += [self.keys[real_mid+1]]
        return black

    def highlightKeys(self):
        indLeftmostHighKey = int((self.leftEnd-60)/45.9)
        keysToBeHighInd = [indLeftmostHighKey, indLeftmostHighKey + 1,indLeftmostHighKey + 2]
        keysToBeHigh = [self.whiteKeys[keysToBeHighInd[0]],self.whiteKeys[keysToBeHighInd[1]],self.whiteKeys[keysToBeHighInd[2]]]
        black = self.highlightBlack(keysToBeHigh, keysToBeHighInd)
        for i in range(len(black)):
            keysToBeHigh += [black[i]]
        kb.Keyboard.setHighlight(self.myKeyboard, keysToBeHigh)
      
    def drawKeyboard(self):
        self.highlightKeys()
        self.myKeyboard.draw(self.gameDisplay)

         

    def drawPie(self):
        leftSt = (490,50)#(480,50)
        rightSt = (575,50)#(583,50)
        points = [leftSt,rightSt,(self.rightEnd,367),(self.leftEnd,367)]
        pygame.gfxdraw.filled_polygon(self.gameDisplay,points,(224,216,113,100))
    

    def drawLight(self):
        if (self.leftEnd < self.leftLimPie):
            self.lightDelta *= -1
        elif (self.rightEnd >= self.rightLimPie):
            self.lightDelta *= -1
        self.leftEnd += self.lightDelta
        self.rightEnd += self.lightDelta
         

    def draw(self,surface):
        pygame.draw.rect(self.gameDisplay, Config.black, ((0,0,60,566)),0)
        pygame.draw.line(self.gameDisplay, (225,225,225), (60,0), (60,600), 3)

        #draw the left menu bar
        self.gameDisplay.blit(self.userIcon, (5, 5))
        self.gameDisplay.blit(self.user, (11, 65))
        self.gameDisplay.blit(self.homeIcon, (5, 90))
        self.gameDisplay.blit(self.home, (9, 150))
        self.gameDisplay.blit(self.background, (60, 0))

        self.drawPie()
        self.drawKeyboard()

        self.gameDisplay.blit(self.batIcon,(436,0))

        self.drawLight()

    def handleEvents(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
             #check if home button is clicked
            if pygame.Rect(5,90,50,50).collidepoint(event.pos):
                runHomescreen()
            elif pygame.Rect(5, 175, 50, 50).collidepoint(event.pos):
                self.rec = True
            elif pygame.Rect(5, 260, 50, 50).collidepoint(event.pos):
                self.rec = False
            elif pygame.Rect(5, 345, 50, 50).collidepoint(event.pos):
                pass


    def practiceMode(self):
        while self.practice:
            #area for the background is 964 * 566
            for event in pygame.event.get():
                #refresh to home page 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    Status.isQuit = True
                    self.practice = False
                    sys.exit()
                self.handleEvents(event)

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            self.draw(self.gameDisplay)
        

            
            pygame.display.update()
            self.clock.tick(60)
            

    def runPM(self):
        pygame.init()
        self.practiceMode()


if __name__ == '__main__':
    pp = PracticePage()
    pp.runPM()