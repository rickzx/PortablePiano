import pygame
from config import *

class Staff(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		pygame.sprite.Sprite.__init__(self,self.groups)
		self.pos_x, self.pos_y = pos_x, pos_y
		self.image = self.loadImg()
		self.rect = (pos_x, pos_y, Config.display_width, Config.display_height)

	def loadImg(self):
		surface = pygame.Surface((Config.display_width, 125))
		surface.fill(Config.grey)
		for i in range(5):
			pygame.draw.line(surface, Config.black, (0, i * 10), (Config.display_width, i * 10))
		for i in range(5):
			pygame.draw.line(surface, Config.black, (0, 80 + i * 10), (Config.display_width, 80 + i * 10))
		return surface

	def update(self, seconds):
		pass