
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
# Class class


# 設定物件大小
class ObjectSize(object):
    def __init__(self):
        pass
    def setSize(self, size):
        w, h = size
        self.__width = w
        self.__height = h
    def getSize(self):
        return self.__width, self.__height

# 設定物件是否為玩家及圖案
class ObjectPlayer(object):
    def __init__(self):
        pass
    def setPlayerStatus(self, player = False):
        self.__player = player
    def getPlayerStatus(self):
        return self.__player
    def setObjectSprite(self, spr = None):
        self.__sprite = spr
    def getObjectSprite(self):
        return self.__sprite

# 設定玩家可移動範圍
class PlayerArea(object):
    def __init__(self):
        pass
    def setPlayerArea(self, area):
        xs, xe, ys, ye = area
        self.__player_X_Start = xs
        self.__player_X_End = xe
        self.__player_Y_Start = ys
        self.__player_Y_End = ye
    def getPlayerArea(self):
        return [self.__player_X_Start, self.__player_X_End, self.__player_Y_Start, self.__player_Y_End]


# 設定物件座標系統
class ObjectCoordinate(ObjectSize, ObjectPlayer, PlayerArea):
    # 物件座標系統 Class 初始化
    def __init__(self):
        # 不設定任何參數，直接略過
        pass
    # 設定物件座標
    def setCoordination(self, coor):
        (x,y) = coor
        self.__x = x
        self.__y = y
    # 移動物件座標
    def movCoordination(self, coor):
        (x,y) = coor
        w,h = super().getSize()
        # 確認是否為玩家本身
        if super().getPlayerStatus() :
            print("X: " + str(x) + ";Y: " + str(y) )
            newX = self.__x + x
            newY = self.__y + y
            print("New X: " + str(newX) + ";New Y: " + str(newY) )
            (areaWS, areaWE, areaHS, areaHE) = super().getPlayerArea()
            print(str(areaWS) + ";" + str(areaWS) + ";" + str(areaHS) + ";" + str(areaHE) )
            # 避免超過玩家移動區域
            if ( newX > areaWS ) and ( ( newX + w ) < areaWE ):
                self.__x = newX
            elif newX <= areaWS:
                self.__x = areaWS
            
            if ( newY > areaHS ) and ( ( newY + h ) < areaHE ):
                self.__y = newY
            elif newY <= areaHS:
                self.__y = areaHS

        # 若非玩家則依照原本設定的位移量位移
        else:
            self.__x = self.__x + self.__speedInX
            self.__y = self.__y + self.__speedInY
    # 獲得物件的XY座標
    def getCoordination(self):
        return self.__x, self.__y
    # 設定物件在XY坐標系上的速度
    def setSpeed(self, coor):
        (x,y) = coor
        self.__speedInX = x
        self.__speedInY = y

class Item(ObjectCoordinate):
    def __init__(self, objectCoordinationArray = [0,0], objectSizeArray = [0,0], objectSpeed = [0,0], spr = None, player = False, moveAreaArray = [0,0,0,0]):
        # objectCoordination 為物件座標
        super().setCoordination(objectCoordinationArray)
        # objectWidth, objectHeight 分別為物件的寬與高
        super().setSize(objectSizeArray)
        # moveArea 依序為X座標開始, X座標結束, Y座標開始, Y座標結束的矩形區域
        super().setPlayerArea(moveAreaArray)
        # player 為設定該物件是否為玩家
        super().setPlayerStatus(player)
        # objectSpeed 為物件在XY的每次位移量
        super().setSpeed(objectSpeed)
        #
        super().setObjectSprite(spr)
    def getObjectXYByList(self):
        return super().getCoordination()
    def getObjectXYByTuple(self):
        x,y = super().getCoordination()
        return (x, y)
    def getObjectX(self):
        x,y = super().getCoordination()
        return x
    def getObjectY(self):
        x,y = super().getCoordination()
        return y
    def getObjectSize(self):
        return super().getSize()
    def getObjectWidth(self):
        w,h = super().getSize()
        return w
    def getObjectHeight(self):
        w,h = super().getSize()
        return h
    def getObjectSprite(self):
        return super().getPlayerSprite()
    def setObjectSpeed(self, coor):
        super().setSpeed(coor)
    def movObjectCoordination(self, coor = [0,0]):
        super().movCoordination(coor)

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