
# Create Window and Close Window

import pygame, time, random
from pygame.locals import *
from classes.Item import *

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
# Class class




# Default value
Player = Item( [200,200], [50,50], [0,0], "sprite/f15.png", True, [0, WIDTH, 0, HEIGHT] )
others = []
bullets = []
bulletSpeed = -5
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
					bullets.append( Item( [(Player.getObjectX() + int(Player.getObjectHeight() / 2)), Player.getObjectY()], [4,4], [0,bulletSpeed]))
		elif event.type == KEYUP:
			if event.key == K_DOWN or event.key == K_UP:
				moveY = 0
			if event.key == K_LEFT or event.key == K_RIGHT:
				moveX = 0
		elif event.type == MOUSEMOTION:
			(x,y) = event.pos
	# Perform calculation

	for other in others:
		other.movObjectCoordination()
		if other.getObjectY() > HEIGHT:
			others = [ x for x in others if not (x.getObjectX() == other.getObjectX() and x.getObjectY() == other.getObjectY())]
	if random.randint(0, 10) == 0:
		others.append( Item( [random.randint(0, 500),0], [50,50], [0,8], "sprite/su27.png") )

	for bullet in bullets:
		bullet.movObjectCoordination()
		if bullet.getObjectY() <= 0:
			bullets = [x for x in bullets if not (x.getObjectY() == bullet.getObjectY())]

	Player.movObjectCoordination([moveX, moveY])

	window.fill( BACKGROUND_COLOR )

	# Draw graphics
	for other in others:
		window.blit(OTHER_SPRITE, ((other.getObjectX() - (other.getObjectWidth() / 2)), (other.getObjectY() - (other.getObjectHeight() / 2))) )
		# pygame.draw.rect( window, OTHER_COLOR, ((other.x - (other.w / 2)), (other.y - (other.h / 2)), other.w, other.h) )

	for bullet in bullets:
		pygame.draw.circle( window, BULLET_COLOR, ((bullet.getObjectX() - 2), (bullet.getObjectY() - 2)), 4, 4)
	window.blit(OUR_SPRITE, Player.getObjectXYByList() )
	# pygame.draw.rect( window, OUR_COLOR, ( (item1.x - (item1.w / 2) ) , ( item1.y - ( item1.h / 2) ), item1.w, item1.h))
	label_coordinates = ARIAL20.render("Mouse @ " + str( x ) + "," + str( y ) + "; Item @ " + str( Player.getObjectX() + 25 ) + "," + str( Player.getObjectY() + 25 ), 1, WHITE)
	window.blit(label_coordinates, (000,000))
	pygame.display.update()
	fps.tick(60)



pygame.quit()
