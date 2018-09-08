import pygame, sys, math
import time

def PlayCounting(bpm, bpb):
    sleep = 60.0 / bpm
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
    PlayCounting(60, 2)

if __name__ == '__main__':
    main()
