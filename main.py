# https://www.youtube.com/watch?v=8dfePlONtls&ab_channel=freeCodeCamp.org  20:00

import pygame
from pygame.locals import *

def draw_block():

	surface.fill((141,172,194))
	surface.blit(block, (block_x, block_y))
	surface.blit(bad_guy,(600,600))
	pygame.display.flip()


if __name__ == "__main__":
	pygame.init()
	surface = pygame.display.set_mode((1000, 1000))

	surface.fill((141,172,194))
	block = pygame.image.load("resources/NmJgg.jpeg").convert()
	bad_guy = pygame.image.load("resources/pusheen.png").convert()

	block = pygame.transform.scale(block, (200,100))
	block_y = 500
	block_x = 250
	surface.blit(block,(block_x,block_y))
	surface.blit(bad_guy,(600,600))
	pygame.display.flip()

	running = True

	while running:
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False

				if event.key == K_UP:
					block_y -= 30
					draw_block()
				if event.key == K_DOWN:
					block_y += 30
					draw_block()
				if event.key == K_LEFT:
					block_x -= 30
					draw_block()
				if event.key ==K_RIGHT:
					block_x += 30
					draw_block()

				elif event.type == QUIT:
					running = False

