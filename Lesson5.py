# Create Window and Close Window

import pygame, time, random
from pygame.locals import *

WIDTH = 400
HEIGHT = 600
pygame.init()
fps = pygame.time.Clock()
window = pygame.display.set_mode(( WIDTH, HEIGHT ))

# Declare colours, images, sounds, fonts
BACKGROUND_COLOR = (184, 211, 239)
OUR_COLOR = (214,  83,  83)
OTHER_COLOR = (82, 102,  27)
BULLET_COLOR = (242, 171, 79)

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
		tmp = self.x + shift + self.w
		if tmp <= w and (self.x + shift) >= 0 :
			self.x += shift
	def moveY( self, shift, h ):
		tmp = self.y + shift + self.h
		if tmp <= h and (self.y + shift) >= 0 :
			self.y += shift
class ItemBullet(object):
	def __init__(self, x, y, speed):
		self.x = x
		self.y = y
		self.speed = speed
	def move( self ):
		self.y -= self.speed
# Default value
item1 = ItemValue(200, 200, 50, 50)
others = []
bullets = []
bulletSpeed = 5
otherSpeed = 8
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
				moveY = 5
			if event.key == K_UP:
				moveY = -5
			if event.key == K_LEFT:
				moveX = -5
			if event.key == K_RIGHT:
				moveX = 5

			# Key Event for fire
			if event.key == K_SPACE:
				if len(bullets) <= 8:
					bullets.append( ItemBullet( (item1.x + int(item1.w / 2)), item1.y, bulletSpeed))
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
		if other.y > HEIGHT:
			others = [ x for x in others if not (x.x == other.x and x.y == other.y)]
	if random.randint(0, 10) == 0:
		others.append( ItemValue(random.randint(0, 500), 0, 50, 50) )

	for bullet in bullets:
		bullet.move()
		if bullet.y <= 0:
			bullets = [x for x in bullets if not (x.y == bullet.y)]

	item1.moveX(moveX, WIDTH)
	item1.moveY(moveY, HEIGHT)

	window.fill( BACKGROUND_COLOR )

	# Draw graphics
	for other in others:
		window.blit(OTHER_SPRITE, ((other.x - (other.w / 2)), (other.y - (other.h / 2))) )
		# pygame.draw.rect( window, OTHER_COLOR, ((other.x - (other.w / 2)), (other.y - (other.h / 2)), other.w, other.h) )

	for bullet in bullets:
		pygame.draw.circle( window, BULLET_COLOR, ((bullet.x - 2), (bullet.y - 2)), 4, 4)
	window.blit(OUR_SPRITE, ( item1.x ,  item1.y ))
	# pygame.draw.rect( window, OUR_COLOR, ( (item1.x - (item1.w / 2) ) , ( item1.y - ( item1.h / 2) ), item1.w, item1.h))
	label_coordinates = ARIAL20.render("Mouse @ " + str( x ) + "," + str( y ) + "; Item @ " + str( item1.x + 25 ) + "," + str( item1.y + 25 ), 1, WHITE)
	window.blit(label_coordinates, (000,000))
	pygame.display.update()
	fps.tick(60)



pygame.quit()