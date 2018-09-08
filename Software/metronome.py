<<<<<<< HEAD
import pygame
import time
import threading

from config import *
from util import *
from status import *

class Metronome(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.pos_x, self.pos_y = pos_x, pos_y
        self.isStart = False
        self.dragging = False
        self.sliderPos = 10
        self.image = self.loadImg(10)
        self.rect = (pos_x, pos_y, 100, 100)
        self.counter = 0
        self.click = pygame.mixer.Sound("media/click.ogg")

    def loadImg(self, pos):
        self.sliderPos = pos
        surface = pygame.Surface((100, 100))
        surface.fill(Config.darkGrey)
        pygame.draw.line(surface, Config.black, (50, 5), (50, 85))
        pygame.draw.rect(surface, Config.black, (43, pos, 15, 15))
        if self.isStart:
            drawImage(surface, "media/pause.png", 80, 80, (20, 20))
        else:
            drawImage(surface, "media/play.png", 80, 80, (20, 20))
        return surface

    def playMetronome(self):
        self.counter += 1
        if self.counter % (75 - self.sliderPos) == 0:
            self.click.play()


    def update(self, seconds):
        if self.isStart:
            self.playMetronome()

        if pygame.mouse.get_pressed()[0]:
            mouse_x = pygame.mouse.get_pos()[0]
            mouse_y = pygame.mouse.get_pos()[1]
            
            if ((self.rect[0]) + 43 < mouse_x < (self.rect[0]) + 57 and 
                    (self.rect[1]) + 10 < mouse_y < (self.rect[1]) + 70):
                self.image = self.loadImg(pygame.mouse.get_pos()[1] - self.rect[1])

            elif ((self.rect[0]) + 70 < mouse_x < (self.rect[0]) + 90 and 
                    (self.rect[1]) + 70 < mouse_y < (self.rect[1]) + 90 and 
                        not Status.mouseDown):
                if not self.isStart:
                    self.isStart = True
                else:
                    self.isStart = False
                self.image = self.loadImg(self.sliderPos)

            Status.mouseDown = True

        if not pygame.mouse.get_pressed()[0]:
            Status.mouseDown = False
=======
import pygame, sys, math
import time

def PlayCounting(bpm, bpb):
    sleep = 60 / bpm / bpb
    counter = 0
    metronomeSound = pygame.mixer.Sound("media/metronome_klack.wav")
    while True:
        if counter % bpb == 0:
            metronomeSound.set_volume(1.0)
            metronomeSound.play()
        else:
            metronomeSound.set_volume(0.6)
            metronomeSound.play()
        time.sleep(sleep)

def main():
    pygame.init()
    PlayCounting(80, 2)

if __name__ == '__main__':
    main()
>>>>>>> origin/software
