# Create Window and Close Window

import pygame
from pygame.locals import *

pygame.init()
fps = pygame.time.Clock()
window = pygame.display.set_mode((600,400))

# Declare colours, images, sounds, fonts
BLUE    = (0x00,0x00,0xFF)
RED     = (255,0,0)
GREEN   = (0,255,0)
YELLO   = (255,255,0)
BLACK   = (0,0,0)
WHITE   = (0xFF,0xFF,0xFF)
PINK	= (0xFF, 0x65, 0xFD)
ARIAL60 = pygame.font.SysFont("Arial", 60)
# Variables for keeping track of my game player etc

quit = False

# Main game loop
while not quit:

	# Process events
	for event in pygame.event.get():

		print(event)

		if event.type == QUIT :
			quit = True
		elif event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				quit = True
		elif event.type == MOUSEMOTION:
			(x,y) = event.pos

	# Perform calculation


	# Draw graphics
	window.fill(BLACK)
	pygame.draw.line(window, BLUE, (50,60), (50, 160), 10)
	pygame.draw.rect(window, GREEN, (52, 160, 120, 40))
	pygame.draw.circle(window, WHITE, (110, 110), 40, 10)
	pygame.draw.ellipse(window, PINK, (200,100,80,40))
	pygame.draw.polygon(window, RED, ((20,20), (50,60), (100,60), (20,70), (10,30)), 5)
	label = ARIAL60.render("Hello Python!", 1 , WHITE)
	window.blit(label, (300,50))
	label_coordinates = ARIAL60.render("Mouse @ "+str(x)+","+str(y), 1, WHITE)
	window.blit(label_coordinates, (000,200))
	pygame.display.update()
	fps.tick(25)



pygame.quit()