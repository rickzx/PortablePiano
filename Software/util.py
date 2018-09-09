import pygame

def drawImage(surface, path, x, y, scale):
	img = pygame.image.load(path)
	img = pygame.transform.smoothscale(img, scale)
	surface.blit(img,(x - img.get_rect().size[0] // 2, y - img.get_rect().size[1] // 2))

def text_objects(text, font, color):
	textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()

def drawText(surface, text, x, y, font, size, color):
	myFont = pygame.font.SysFont(font, size, True)
	textSurf, textRect = text_objects(text, myFont, color)
	textRect.center = (x, y)		
	surface.blit(textSurf, textRect)

def drawImageTL(surface, path, x, y, scale):
	img = pygame.image.load(path)
	img = pygame.transform.scale(img,scale)
	surface.blit(img,(x,y))