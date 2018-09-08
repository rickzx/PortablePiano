import pygame

class Config(object):
	display_width = 1024
	display_height = 566

	white = (255,255,255)
	black = (0,0,0)
	grey = (214, 215, 216)
	darkGrey = (127, 129, 130)
	red = (255,0,0)
	blue = (0, 134, 179)

	fps = 30
	serialPort = 115200

class Sound(object):
	pygame.mixer.init()
	C = pygame.mixer.Sound("media/sound/C4.ogg")
	Cs = pygame.mixer.Sound("media/sound/C#.ogg")
	D = pygame.mixer.Sound("media/sound/D4.ogg")
	Ds = pygame.mixer.Sound("media/sound/D#.ogg")
	E = pygame.mixer.Sound("media/sound/E.ogg")
	F = pygame.mixer.Sound("media/sound/F.ogg")
	Fs = pygame.mixer.Sound("media/sound/F#.ogg")
	G = pygame.mixer.Sound("media/sound/G.ogg")
	Gs = pygame.mixer.Sound("media/sound/G#.ogg")
	A = pygame.mixer.Sound("media/sound/A4.ogg")
	As = pygame.mixer.Sound("media/sound/A#.ogg")
	B = pygame.mixer.Sound("media/sound/B.ogg")