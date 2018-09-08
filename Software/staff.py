import pygame
from config import *

class Staff(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self,self.groups)
		self.image = self.loadImg()
		#self.mask = pygame.mask.from_surface(self.image)
		self.rect = (0, 0, Config.display_width, Config.display_height)

	def loadImg(self):
		surface = pygame.Surface((Config.display_width, Config.display_height // 3))
		surface.fill((255,255,255))
		return surface

	def update(self, seconds):
		pass