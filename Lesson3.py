# Create Window and Close Window

import pygame
from pygame.locals import *

windoww = 600
windowh = 400
pygame.init()
fps = pygame.time.Clock()
window = pygame.display.set_mode(( windoww, windowh ))

# Declare colours, images, sounds, fonts
BLUE    = (0x00,0x00,0xFF)
RED     = (255,0,0)
GREEN   = (0,255,0)
YELLO   = (255,255,0)
BLACK   = (0,0,0)
WHITE   = (0xFF,0xFF,0xFF)
PINK	= (0xFF, 0x65, 0xFD)
ARIAL20 = pygame.font.SysFont("Arial", 20)
# Variables for keeping track of my game player etc
class ItemValue(object):
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
	def movex( self, shift, w):
		tmp = self.x + shift + self.w
		if tmp <= w and (self.x + shift) >= 0 :
			self.x += shift
	def movey( self, shift, h ):
		tmp = self.y + shift + self.h
		if tmp <= h and (self.y + shift) >= 0 :
			self.y += shift

item1 = ItemValue(200, 200, 50, 50)

movex = 0
movey = 0

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
			# Key Event for move

			if event.key == K_DOWN:
				movey = 10
			if event.key == K_UP:
				movey = -10
			if event.key == K_LEFT:
				movex = -10
			if event.key == K_RIGHT:
				movex = 10
		elif event.type == KEYUP:
			if event.key == K_DOWN or event.key == K_UP:
				movey = 0
			if event.key == K_LEFT or event.key == K_RIGHT:
				movex = 0
		elif event.type == MOUSEMOTION:
			(x,y) = event.pos
	# Perform calculation
	item1.movex(movex, windoww)
	item1.movey(movey, windowh)



	# Draw graphics
	window.fill(BLACK)
	pygame.draw.rect(window, GREEN, ( item1.x, item1.y, item1.w, item1.h))
	label_coordinates = ARIAL20.render("Mouse @ " + str( x ) + "," + str( y ) + "; Item @ " + str( item1.x + 25 ) + "," + str( item1.y + 25 ), 1, WHITE)
	window.blit(label_coordinates, (000,000))
	pygame.display.update()
	fps.tick(25)



pygame.quit()