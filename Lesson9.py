

# Create Window and Close Window

import pygame, time, random
from pygame.locals import *
from classes.Item import *

# 視窗寬高參數
WIDTH = 400
HEIGHT = 600
# Pygame初始化
pygame.init()
# 獲取FPS
fps = pygame.time.Clock()
# 設定視窗寬高
window = pygame.display.set_mode(( WIDTH, HEIGHT ))
# 設定視窗標題
pygame.display.set_caption('Shooter')

# 宣告顏色，圖像，聲音，字型
## 顏色
BACKGROUND_COLOR = (184, 211, 239)
OUR_COLOR = (214,  83,  83)
OTHER_COLOR = (82, 102,  27)
BULLET_COLOR = (242, 171, 79)

GREEN   = (0,255,0)
YELLO   = (255,255,0)
BLACK   = (0,0,0)
WHITE   = (0xFF,0xFF,0xFF)
PINK	= (0xFF, 0x65, 0xFD)

## 圖像

## 字型及大小
ARIAL20 = pygame.font.SysFont("Arial", 20)

# 宣告變數
# Variables for keeping track of my game player etc
# Class
# Item( Coordination, Size, Speed, spr, player, moveArea, time_to_die)
# 函式宣告
def render_item( Sprite_dir, Postion_at_X, Postion_at_Y ):
    Sprite = pygame.image.load(Sprite_dir).convert_alpha()
    window.blit(Sprite, (Postion_at_X, Postion_at_Y))

def collision_check(collsionA, collsionB):
    check_result = False

    for B in collsionB:
        for A in collsionA:
            movx, movy = A.getObjectSpeed()
            x = A.getObjectX() - B.getObjectX()
            y = A.getObjectY() - B.getObjectY()
            # print(str(x) + ", " + str(y))
            print("X:" + str(-B.getObjectWidth()) + "; Y: " + str(-(B.getObjectHeight() - movy) ))
            if ( x <= 0 and x > -B.getObjectWidth() ) and ( y <= 0 and y > -(B.getObjectHeight() - movy) ):
                collsionA = [ i for i in collsionA if not i.getObjectXYByList() == A.getObjectXYByList() ]
                collsionB = [ j for j in collsionB if not j.getObjectXYByList() == B.getObjectXYByList() ]
                check_result = True
    
    return collsionA, collsionB, check_result



# Default value

Player = Item( [200,200], [50,50], [0,0], "sprite/f15.png", True, [0, WIDTH, 0, HEIGHT] )
others = []
bullets = []
bulletSpeed = -6
otherSpeed = 3
moveX = 0
moveY = 0
shoot_down_count = 0
bullet_count = 0
quit = False

# Main game loop
while not quit:

    # Process events
    for event in pygame.event.get():

        # print(event)
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
                    # Item( Coordination, Size, Speed, spr, player, moveArea, time_to_die)
                    bullets.append( Item( [(Player.getObjectX() + int(Player.getObjectHeight() / 2)), Player.getObjectY()], [4,4], [0,bulletSpeed], None, False, [0,0,0,0], 50))
                    bullet_count += 1
        elif event.type == KEYUP:
            if event.key == K_DOWN or event.key == K_UP:
                moveY = 0
            if event.key == K_LEFT or event.key == K_RIGHT:
                moveX = 0
        elif event.type == MOUSEMOTION:
            (x,y) = event.pos
    # Perform calculation

    bullets, others, shoot_down_plus = collision_check(bullets, others)
    
    if shoot_down_plus:
        shoot_down_count += 1
    for other in others:
        other.movObjectCoordination()
        if other.getObjectY() > HEIGHT:
            others = [ x for x in others if not (x.getObjectX() == other.getObjectX() and x.getObjectY() == other.getObjectY())]
    if (random.randint(0, 10) == 0) and len(others) <= 5:
        others.append( Item( [random.randint(0, 500),0], [100,50], [0,5], "sprite/su27.png") )
        
    for bullet in bullets:
        bullet.movObjectCoordination()
        if (bullet.getTTL() <= 0) or (bullet.getObjectY() <= 0):
            bullets = [x for x in bullets if not ((x.getObjectY() == bullet.getObjectY()) or x.getTTL() == bullet.getTTL())]
        bullet.doTTL()
            
    Player.movObjectCoordination([moveX, moveY])
    
    window.fill( BACKGROUND_COLOR )
    
    # Draw graphics
    for other in others:
        render_item(other.getObjectSprite(), (other.getObjectX() - (other.getObjectWidth() / 2)), (other.getObjectY() - (other.getObjectHeight() / 2)))
        # pygame.draw.rect( window, OTHER_COLOR, ((other.x - (other.w / 2)), (other.y - (other.h / 2)), other.w, other.h) )
        
    for bullet in bullets:
        pygame.draw.circle( window, BULLET_COLOR, ((bullet.getObjectX() - 2), (bullet.getObjectY() - 2)), 4, 4)
    render_item(Player.getObjectSprite(), Player.getObjectX(), Player.getObjectY())
    # pygame.draw.rect( window, OUR_COLOR, ( (item1.x - (item1.w / 2) ) , ( item1.y - ( item1.h / 2) ), item1.w, item1.h))
    label_coordinates = ARIAL20.render("Shot Down : " + str( shoot_down_count ) + "; Bullets : " + str( bullet_count ) + "; Score : " + str( 100 * shoot_down_count - bullet_count ), 1, WHITE)
    window.blit(label_coordinates, (000,000))
    pygame.display.update()
    fps.tick(80)

pygame.quit()
