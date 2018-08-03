

# Create Window and Close Window

import pygame, time, random
from pygame.locals import *
from classes.Item import *

# 視窗寬高參數

WIDTH = 600
HEIGHT = 600

PLAY_AREA_WIDTH  = 400
PLAY_AREA_HEIGHT = 600

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
DARK_YELLOW   = (200,200,50)
BLACK   = (0,0,0)
WHITE   = (0xFF, 0xFF, 0xFF)
RED     = (0xFF, 0x00, 0x00)
PINK	= (0xFF, 0x65, 0xFD)

## 圖像

## 字型及大小
ARIAL80 = pygame.font.SysFont("Arial", 80)
ARIAL40 = pygame.font.SysFont("Arial", 40)
ARIAL20 = pygame.font.SysFont("Arial", 20)
ARIAL12 = pygame.font.SysFont("Arial", 12)

# 宣告變數
# Variables for keeping track of my game player etc
# Class



# Default value

Player = Item( [200,500], [50,50], [0,0], "sprite/f15.png", True, [0, PLAY_AREA_WIDTH, 0, PLAY_AREA_HEIGHT] )
others = []
bullets = []
bulletSpeed = -6
otherSpeed = 3
moveX = 0
moveY = 0
shoot_down_count = 0
bullet_count = 0




# Circle Value
quit = False
game_circle = False
title_circle = True
loss_check = False
MENU_SELCETER = 0
# Item( Coordination, Size, Speed, spr, player, moveArea, time_to_die)
# 函式宣告
def render_item( Sprite_dir, Postion_at_X, Postion_at_Y ):
    Sprite = pygame.image.load(Sprite_dir).convert_alpha()
    # print("X:" + str(Postion_at_X) + " ;Y:" + str(Postion_at_Y) )
    window.blit(Sprite, (Postion_at_X, Postion_at_Y))

def collision_check(collsionA, collsionB):
    check_result = False

    for B in collsionB:
        if not isinstance(collsionA, list):
            A = collsionA
            x = abs(A.getObjectX() - B.getObjectX())
            y = abs(A.getObjectY() - B.getObjectY())
            
            # pygame.draw.rect(window, GREEN, (A.getObjectX(), A.getObjectY(), A.getObjectWidth(), A.getObjectHeight()), 5)
            # pygame.draw.rect(window, GREEN, (B.getObjectX(), B.getObjectY(), B.getObjectWidth(), B.getObjectHeight()), 5)
            # print(str(x) + ", " + str(y))
            # print("X:" + str(-B.getObjectWidth()) + "; Y: " + str(-(B.getObjectHeight() - movy) ))
            if ( x < B.getObjectWidth() ) and ( y < B.getObjectHeight() ):
                collsionB = [ j for j in collsionB if not j.getObjectXYByList() == B.getObjectXYByList() ]
                check_result = True
        else:
            for A in collsionA:
                x = abs(A.getObjectX() - B.getObjectX())
                y = abs(A.getObjectY() - B.getObjectY())
                # print(str(x) + ", " + str(y))
                # print("X:" + str(-B.getObjectWidth()) + "; Y: " + str(-(B.getObjectHeight() - movy) ))
                # pygame.draw.rect(window, GREEN, (A.getObjectX(), A.getObjectY(), A.getObjectWidth(), A.getObjectHeight()), 5)
                # pygame.draw.rect(window, GREEN, (B.getObjectX(), B.getObjectY(), B.getObjectWidth(), B.getObjectHeight()), 5)
                if ( x < B.getObjectWidth() ) and ( y < B.getObjectHeight() ):
                    collsionA = [ i for i in collsionA if not i.getObjectXYByList() == A.getObjectXYByList() ]
                    collsionB = [ j for j in collsionB if not j.getObjectXYByList() == B.getObjectXYByList() ]
                    check_result = True
    
    return collsionA, collsionB, check_result

# def do_game():
    
#    global game_circle
#    global title_circle



# def do_title():
    # global title_circle
# Main game loop
while not quit:
    # do_title()
    
    
    while title_circle:
        
        for event in pygame.event.get():

            # print(event)
            if event.type == QUIT :
                quit = True
                title_circle = False
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    MENU_SELCETER += 1
                if event.key == K_DOWN:
                    MENU_SELCETER += 1
                if event.key == K_SPACE:
                    if MENU_SELCETER == 0:
                        title_circle = False
                        game_circle = True
                        loss_check = False
                        Player = Item( [200,500], [50,50], [0,0], "sprite/f15.png", True, [0, PLAY_AREA_WIDTH, 0, PLAY_AREA_HEIGHT] )
                        others = []
                        bullets = []
                        shoot_down_count = 0
                        bullet_count = 0
                    if MENU_SELCETER == 1:
                        title_circle = False
                        game_circle = False
                        quit = True
            if MENU_SELCETER > 1:
                MENU_SELCETER -= 2
            if MENU_SELCETER < 0:
                MENU_SELCETER += 2




        window.fill( BLACK )
        label_TITLE             = ARIAL80.render("SHOOTER!!", 1 ,DARK_YELLOW)
        window.blit(label_TITLE, (80,20))

        pygame.draw.circle(window, RED, (250, 410 + MENU_SELCETER * 20), 10)
        label_PLAY              = ARIAL20.render("PLAY", 1 , WHITE)
        label_QUIT              = ARIAL20.render("QUIT", 1 , WHITE)
        window.blit(label_PLAY, (260,400))
        window.blit(label_QUIT, (260,420))


        
        pygame.display.update()
        fps.tick(80)
    while game_circle:
        # Process events
        for event in pygame.event.get():

            # print(event)
            if event.type == QUIT :
                quit = True
                game_circle = True
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
        window.fill( BACKGROUND_COLOR )

        bullets, others, shoot_down_plus = collision_check(bullets, others)
    
        if shoot_down_plus:
            shoot_down_count += 1
        for other in others:
            other.movObjectCoordination()
            if other.getObjectY() > PLAY_AREA_HEIGHT:
                others = [ x for x in others if not (x.getObjectX() == other.getObjectX() and x.getObjectY() == other.getObjectY())]
        if (random.randint(0, 10) == 0) and len(others) <= 5:
            others.append( Item( [random.randint(0, 350),0], [50,50], [0,5], "sprite/su27.png") )
        
        for bullet in bullets:
            bullet.movObjectCoordination()
            if (bullet.getTTL() <= 0) or (bullet.getObjectY() <= 0):
                bullets = [x for x in bullets if not ((x.getObjectY() == bullet.getObjectY()) or x.getTTL() == bullet.getTTL())]
            bullet.doTTL()
            
        Player, other, loss_check = collision_check(Player, others)
        Player.movObjectCoordination([moveX, moveY])
    
        # Draw graphics
        for other in others:
            render_item(other.getObjectSprite(), other.getObjectX(), other.getObjectY() )
            # pygame.draw.rect(window, RED, (other.getObjectX(), other.getObjectY(), other.getObjectWidth(), other.getObjectHeight()), 5)
            # pygame.draw.rect( window, OTHER_COLOR, ((other.x - (other.w / 2)), (other.y - (other.h / 2)), other.w, other.h) )

        for bullet in bullets:
            pygame.draw.circle( window, BULLET_COLOR, ((bullet.getObjectX() - 2), (bullet.getObjectY() - 2)), 4, 4)
        render_item(Player.getObjectSprite(), Player.getObjectX(), Player.getObjectY())
    
        # pygame.draw.rect(window, RED, (Player.getObjectX(), Player.getObjectY(), Player.getObjectWidth(), Player.getObjectHeight()), 5)
        # pygame.draw.rect( window, OUR_COLOR, ( (item1.x - (item1.w / 2) ) , ( item1.y - ( item1.h / 2) ), item1.w, item1.h))
        if not loss_check:
            # SCORE AREA (400,0) to (400, 600)
            pygame.draw.rect(window, BLACK, (400, 0, 200, 600 ))
            # label_coordinates = ARIAL20.render("Shot Down : " + str( shoot_down_count ) + "; Bullets : " + str( bullet_count ) + "; Score : " + str( 100 * shoot_down_count - bullet_count ), 1, WHITE)
            label_SCORE             = ARIAL20.render("SCORE", 1 ,DARK_YELLOW)
            label_SCORE2            = ARIAL20.render(str( 100 * shoot_down_count - bullet_count ).zfill(17), 1 ,DARK_YELLOW)
            label_BULLETS           = ARIAL12.render("BULLETS : " + str( bullet_count ), 1 ,DARK_YELLOW)
            label_SHOOT_DOWN_COUNT  = ARIAL12.render("Shot Down : " + str( shoot_down_count ), 1 ,DARK_YELLOW)
            window.blit(label_SCORE, (405,000))
            window.blit(label_SCORE2, (405,25))
            window.blit(label_BULLETS, (405,580))
            window.blit(label_SHOOT_DOWN_COUNT, (505,580))
            pygame.display.update()
        else:
            window.fill( BLACK )
            label_SCORE             = ARIAL20.render("SCORE : " + str( 100 * shoot_down_count - bullet_count ), 1 ,DARK_YELLOW)
            window.blit(label_SCORE, (200,340))
            pygame.display.update()
            pygame.time.delay(2000)
            game_circle = False
            title_circle = True
            MENU_SELCETER = 0

        fps.tick(80)


pygame.quit()