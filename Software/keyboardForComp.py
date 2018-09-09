import pygame
import time

from config import *
from util import *

class Key(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, name, type):
        self.x, self.y = pos_x, pos_y
        self.name = name
        self.type = type
        self.mode = 0


    def draw(self, surface):
        '''
        mode 0： original keys
        mode 1： keys pressed by the user(yellow)
        mode 2： keys lighted up (brighter)
        '''
        if self.type == "black":
            if self.mode == 0:
                drawImageTL(surface, "media/keys/original/" + self.type + ".png", self.x, self.y, (35, 150))
            if self.mode == 1:
                drawImageTL(surface, "media/keys/yellow/" + self.type + ".png", self.x, self.y, (35, 150))
            if self.mode == 2:
                drawImageTL(surface, "media/keys/highlighted/" + self.type + ".png", self.x, self.y, (35, 150))
        elif self.type == "white2":#right white key
            if self.mode == 0:
                drawImageTL(surface, "media/keys/original/" + self.type + ".png", self.x-1, self.y+1, (55, 265))
            if self.mode == 1:
                drawImageTL(surface, "media/keys/yellow/" + self.type + ".png", self.x-1, self.y+1, (55, 265))
            if self.mode == 2:
                drawImageTL(surface, "media/keys/highlighted/" + self.type + ".png", self.x, self.y, (55, 265))
        else:#left white key and middle white key 
            if self.mode == 0:
                drawImageTL(surface, "media/keys/original/" + self.type + ".png", self.x, self.y, (55, 265))
            if self.mode == 1:
                drawImageTL(surface, "media/keys/yellow/" + self.type + ".png", self.x, self.y, (55, 265))
            if self.mode == 2:
                drawImageTL(surface, "media/keys/highlighted/" + self.type + ".png", self.x, self.y, (55, 265))

class Keyboard(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        self.x, self.y = pos_x, pos_y
        self.init_x = pos_x
        self.highlights = []
        self.count = 0
        if (self.count == 0):
            self.keys = self.initKeys()

    def initKeys(self):
        keys = {}
        gap = 46
        self.x -= 9
        self. y -= 100
        
        keys["C2"] = (Key(self.x, self.y, "C", "white1"))
        keys["C#2"] = (Key(self.x + 34, self.y + 5, "C#", "black"))
        keys["D2"] = (Key(self.x + gap * 1, self.y, "D", "white3"))
        keys["D#2"] = (Key(self.x + 81, self.y + 5, "D#", "black"))
        keys["E2"] = (Key(self.x + gap * 2, self.y, "E", "white2"))
        keys["F2"] = (Key(self.x + gap * 3, self.y, "F", "white1"))
        keys["F#2"] = (Key(self.x + 172.85, self.y + 5, "F#", "black"))
        keys["G2"] = (Key(self.x + gap * 4, self.y, "G", "white3"))
        keys["G#2"] = (Key(self.x + 219, self.y + 5, "G#", "black"))
        keys["A2"] = (Key(self.x + gap * 5, self.y, "A", "white3"))
        keys["A#2"] = (Key(self.x + 265, self.y + 5, "A#", "black"))
        keys["B2"] = (Key(self.x + gap * 6, self.y, "B", "white2"))
        
        self.x = self.x + gap * 6 + 47

        keys["C3"] = (Key(self.x, self.y, "C", "white1"))
        keys["C#3"] = (Key(self.x + 34, self.y, "C#", "black"))
        keys["D3"] = (Key(self.x + gap * 1, self.y, "D", "white3"))
        keys["D#3"] = (Key(self.x + 81, self.y, "D#", "black"))
        keys["E3"] = (Key(self.x + gap * 2, self.y, "E", "white2"))
        keys["F3"] = (Key(self.x + gap * 3, self.y, "F", "white1"))
        keys["F#3"] = (Key(self.x + 172.85, self.y, "F#", "black"))
        keys["G3"] = (Key(self.x + gap * 4, self.y, "G", "white3"))
        keys["G#3"] = (Key(self.x + 219, self.y, "G#", "black"))
        keys["A3"] = (Key(self.x + gap * 5, self.y, "A", "white3"))
        keys["A#3"] = (Key(self.x + 265, self.y, "A#", "black"))
        keys["B3"] = (Key(self.x + gap * 6, self.y, "B", "white2"))

        self.x += gap * 6 + 47
        
        keys["C4"] = (Key(self.x, self.y, "C", "white1"))
        keys["C#4"] = (Key(self.x + 34, self.y, "C#", "black"))
        keys["D4"] = (Key(self.x + gap * 1, self.y, "D", "white3"))
        keys["D#4"] = (Key(self.x + 81, self.y, "D#", "black"))
        keys["E4"] = (Key(self.x + gap * 2, self.y, "E", "white2"))
        keys["F4"] = (Key(self.x + gap * 3, self.y, "F", "white1"))
        keys["F#4"] = (Key(self.x + 172.85, self.y, "F#", "black"))
        keys["G4"] = (Key(self.x + gap * 4, self.y, "G", "white3"))
        keys["G#4"] = (Key(self.x + 219, self.y, "G#", "black"))
        keys["A4"] = (Key(self.x + gap * 5, self.y, "A", "white3"))
        keys["A#4"] = (Key(self.x + 265, self.y, "A#", "black"))
        keys["B4"] = (Key(self.x + gap * 6, self.y, "B", "white2"))

        return keys


    def playSound(self, serialStr):
        if serialStr == 'C4':
            Sound.C.play()
        elif serialStr == 'C4n':
            Sound.C.stop()
        elif serialStr == 'C#4':
            Sound.Cs.play()
        elif serialStr == 'C#4n':
            Sound.Cs.stop()
        elif serialStr == 'D4':
            Sound.D.play()
        elif serialStr == 'D4n':
            Sound.D.stop()
        elif serialStr == 'D#':
            Sound.Ds.play()
        elif serialStr == 'D#4n':
            Sound.Ds.stop()
        elif serialStr == 'E4':
            Sound.E.play()
        elif serialStr == 'E4n':
            Sound.E.stop()
        elif serialStr == 'F4':
            Sound.F.play()
        elif serialStr == 'F4n':
            Sound.F.stop()
        elif serialStr == 'F#4':
            Sound.Fs.play()
        elif serialStr == 'F#4n':
            Sound.Fs.stop()
        elif serialStr == 'G4':
            Sound.G.play()
        elif serialStr == 'G4n':
            Sound.G.stop()
        elif serialStr == 'G#4':
            Sound.Gs.play()
        elif serialStr == 'G#4n':
            Sound.Gs.stop()
        elif serialStr == 'A4':
            Sound.A.play()
        elif serialStr == 'A4n':
            Sound.A.stop()
        elif serialStr == 'A#4':
            Sound.As.play()
        elif serialStr == 'A#4n':
            Sound.As.stop()
        elif serialStr == 'B4':
            Sound.B.play()
        elif serialStr == 'B4n':
            Sound.B.stop()

    def setYellow(self, name):
        for key in self.keys:
            if key == name:
                self.keys[key].mode = 1
                self.playSound(name)
            else:
                self.keys[key].mode = 0

    def setHighlight(self, names):
        '''names is a list containing five notes that are to be highlighted'''
        for key in self.keys:
            if (key in names):
                self.keys[key].mode = 2
            else:
                self.keys[key].mode = 0
            

    def resetHighlight(self, name):
        self.keys[name].mode = 0

    def draw(self, surface):
        self.count += 1
        for key in self.keys.values():
            key.draw(surface)
