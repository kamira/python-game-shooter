# Create Window and Close Window

import pygame, time, random
from pygame.locals import *

WIDTH = 600
HEIGHT = 400
pygame.init()
fps = pygame.time.Clock()
window = pygame.display.set_mode(( WIDTH, HEIGHT ))

# Declare colours, images, sounds, fonts
BACKGROUND_COLOR = (184, 211, 239)
OUR_COLOR = (214,  83,  83)
OTHER_COLOR = (82, 102,  27)

OUR_SPRITE = pygame.image.load("sprite/f15.png").convert_alpha()
OTHER_SPRITE = pygame.image.load("sprite/su27.png").convert_alpha()


GREEN   = (0,255,0)
YELLO   = (255,255,0)
BLACK   = (0,0,0)
WHITE   = (0xFF,0xFF,0xFF)
PINK	= (0xFF, 0x65, 0xFD)
ARIAL20 = pygame.font.SysFont("Arial", 20)
# Variables for keeping track of my game player etc
# Class
class ItemValue(object):
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
	def moveX2( self, shift ):
		self.x += shift
	def moveY2( self, shift ):
		self.y += shift
	def moveX( self, shift, w):
		tmp = self.x + shift - (self.w / 2)
		if tmp <= w and (self.x + shift) >= 0 :
			self.x += shift
	def moveY( self, shift, h ):
		tmp = self.y + shift - (self.h / 2)
		if tmp <= h and (self.y + shift) >= 0 :
			self.y += shift
# Default value
item1 = ItemValue(200, 200, 50, 50)
others = []
otherSpeed = 20
moveX = 0
moveY = 0

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
				moveY = 10
			if event.key == K_UP:
				moveY = -10
			if event.key == K_LEFT:
				moveX = -10
			if event.key == K_RIGHT:
				moveX = 10
		elif event.type == KEYUP:
			if event.key == K_DOWN or event.key == K_UP:
				moveY = 0
			if event.key == K_LEFT or event.key == K_RIGHT:
				moveX = 0
		elif event.type == MOUSEMOTION:
			(x,y) = event.pos
	# Perform calculation
	for other in others:
		other.moveY2(otherSpeed)
		if other.y > 500:
			others = [ x for x in others if not (x.x == other.x and x.y == other.y)]
	if random.randint(0, 10) == 0:
		others.append( ItemValue(random.randint(0, 500), 0, 50, 50) )

	item1.moveX(moveX, WIDTH)
	item1.moveY(moveY, HEIGHT)

	window.fill( BACKGROUND_COLOR )

	# Draw graphics
	for other in others:
		print(other.x)
		print(other.y)
		# pygame.draw.rect( window, OTHER_COLOR, ((other.x - ( other.w / 2)), (other.y - ( other.h / 2 ))), (other.w, other.h))
		pygame.draw.rect( window, OTHER_COLOR, ((other.x - (other.w / 2)), (other.y - (other.h / 2)), other.w, other.h) )
	pygame.draw.rect( window, OUR_COLOR, ( (item1.x - (item1.w / 2) ) , ( item1.y - ( item1.h / 2) ), item1.w, item1.h))
	label_coordinates = ARIAL20.render("Mouse @ " + str( x ) + "," + str( y ) + "; Item @ " + str( item1.x + 25 ) + "," + str( item1.y + 25 ), 1, WHITE)
	window.blit(label_coordinates, (000,000))
	pygame.display.update()
	fps.tick(25)



pygame.quit()