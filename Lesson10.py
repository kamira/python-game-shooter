# 載入外部資源
import pygame
import random, sys 
from os import path


# 宣告
## 顏色
RED     = (255,0,0)
GREEN   = (0,255,0)
BLUE    = (153, 204, 255)
BLACK   = (0,0,0)
WHITE   = (255,255,255)
YELLO   = (255,255,0)
## assets folders
game_folder = path.dirname(__file__)
sprite_folder = path.join(game_folder, "sprite")
sound_folder = path.join(game_folder, "sound")


## 參數及變數
WINDOW_WIDTH  = 600
WINDOW_HEIGHT = 600
WIDTH  = WINDOW_WIDTH - 200
HEIGHT = 600
WINDOW_TITLE  = "我的第一個射擊遊戲"
FPS = 120
shoot_count = 0
shoot_down = 0
### 迴圈
running = True


# Pygame 初始化
## 初始化
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
## 混音初始化
pygame.mixer.init()
## 設定視窗參數
### 設定視窗
screen = pygame.display.set_mode(( WINDOW_WIDTH , WINDOW_HEIGHT ))
### 設定視窗標題
pygame.display.set_caption( WINDOW_TITLE )
## 設定計時器
clock = pygame.time.Clock()

# 聲音
shoot_sound = pygame.mixer.Sound(path.join(sound_folder, "machinegun_5.wav"))
shoot_sound.set_volume(0.4)
explosion_sound = pygame.mixer.Sound(path.join(sound_folder, "explosion_16.wav"))
explosion_sound.set_volume(0.4)
wind_sound = pygame.mixer.Sound(path.join(sound_folder, "wind.wav"))
wind_sound.set_volume(0.4)
afterburn_sound = pygame.mixer.Sound(path.join(sound_folder, "afterburner_1.wav"))
afterburn_sound.set_volume(0.4)
pygame.mixer.music.load(path.join(sound_folder, "Two Steps From Hell - Dragon Rider (Extended Remake).mp3"))
pygame.mixer.music.set_volume(0.8)

# 字體
font_name = pygame.font.match_font("Segoe UI")

# Sprite
player_img = pygame.image.load( path.join(sprite_folder, "f15.png") ).convert_alpha()
mob_img = pygame.image.load( path.join( sprite_folder, "su27.png" ) ).convert_alpha()
bullet_img = pygame.image.load( path.join( sprite_folder, "bullet.png" ) ).convert_alpha()
bullet_rect = bullet_img.get_rect()

# Bool
menu = True
game = False
menu_selector = 0
# Def
def draw_text(surf, text, color, size, bold, x, y):
    font = pygame.font.Font(font_name, size)
    if bold:
        font.set_bold(bold)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
    # print(text + str(text_rect.midtop))


# Class
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load( path.join(sprite_folder, image_file))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Player(pygame.sprite.Sprite):
    # 玩家圖像
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale( player_img, ( int(player_img.get_width() * 0.8), int(player_img.get_height() * 0.8) ) )
        self.rect  = self.image.get_rect()
        print(self.image.get_rect())
        # self.radius = 20
        self.radius = int(self.rect.height * .9 / 2)
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.center = (WIDTH / 2 , HEIGHT - 50)
        self.shoot_delay = 150
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        # 方向
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.rect.x -= 2
        if keystate[pygame.K_RIGHT]:
            self.rect.x += 2
        if keystate[pygame.K_UP]:
            self.rect.y -= 2
        if keystate[pygame.K_DOWN]:
            self.rect.y += 2
        if keystate[pygame.K_SPACE]:
            self.shoot()

        # 確認是否超出邊界
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
    
    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay :
            shoot_sound.play()
            shoot_sound.fadeout(200)
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
            global shoot_count
            shoot_count += 1




class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale( mob_img, ( int(mob_img.get_width() * 0.8), int(mob_img.get_height() * 0.8) ) )
        self.rect  = self.image.get_rect()
        self.radius = int(self.rect.height * .9 / 2)
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.bottom = 0
        self.rect.x = random.randrange( WIDTH - self.rect.width )
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.kill()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale( bullet_img, (int(bullet_img.get_width() * 0.5), int(bullet_img.get_height() * 0.5) ) )
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -4
        self.kill_timer = 100
    
    def update(self):
        self.rect.y += self.speedy
        self.kill_timer -= 1
        if self.kill_timer <= 0 or self.rect.bottom <= 0:
            self.kill()

Background_class = Background("Ocean_SpriteSheet.png", [0,0])
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
# player = Plyaer()



# 主程式開始
while running:
    # 保持特定更新率
    clock.tick(FPS)
    while menu:
        
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                # 視窗運作結束
                running = False
                pygame.quit()
                sys.exit(0)
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_UP]:
                menu_selector -= 1
            if keystate[pygame.K_DOWN]:
                menu_selector += 1
            if keystate[pygame.K_SPACE]:
                if menu_selector == 0:
                    menu = False
                    game = True
                    shoot_count = 0
                    shoot_down = 0
                    all_sprites.empty()
                    mobs.empty()
                    bullets.empty()
                    player = Player()
                    all_sprites.add(player)
                    pygame.mixer.music.play(loops=-1)
                        
                if menu_selector == 1:
                    menu = False
                    game = False
                    running = False
            if menu_selector > 1:
                menu_selector -= 2
            if menu_selector < 0:
                menu_selector += 2
        screen.fill(BLUE)
        draw_text(screen, "A Game", RED, 60, True, 300, 10)
        draw_text(screen, "about", RED, 40, True, 300, 70)
        draw_text(screen, "How to shoot Down Enemy", RED, 40, True, 300, 100)
        if menu_selector == 0:
            draw_text(screen, ">> Start <<", BLACK, 20, True, 300 , 400)
            draw_text(screen, "Exit", BLACK, 20, True, 300 , 450)
        if menu_selector == 1:
            draw_text(screen, "Start", BLACK, 20, True, 300 , 400)
            draw_text(screen, ">> Exit <<", BLACK, 20, True, 300 , 450)
        pygame.display.flip()
    while game:
        # 輸入
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                # 視窗運作結束
                running = False
                pygame.quit()
                sys.exit(0)

        if (random.randint(0, 100) == 0) and len(mobs) < 30:
            m = Mob()
            all_sprites.add(m)
            mobs.add(m)

        hits = pygame.sprite.groupcollide(mobs, bullets, True, True, pygame.sprite.collide_mask)
        if hits :
            shoot_down += 1
            explosion_sound.play()
            explosion_sound.fadeout(500)

        hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_mask)
        if hits :
            game = False
            menu = True
            pygame.mixer.music.fadeout(500)
        
        # 更新
        all_sprites.update()
        # 顯示
        screen.fill(BLUE)
        # draw_background(screen, Background_class)
        # screen.blit(Background_class.image, Background_class.rect)
        all_sprites.draw(screen)
        pygame.draw.rect(screen, BLACK, (400, 0, 200, 600))
        draw_text(screen, str(shoot_down * 100 - shoot_count), WHITE, 18, True, 500 , 10)
        draw_text(screen, "Shots", WHITE, 16, True, 450 , 540)
        draw_text(screen, str(shoot_count), WHITE, 16, False, 450 , 570)
        draw_text(screen, "Splash", WHITE, 16, True, 550 , 540)
        draw_text(screen, str(shoot_down), WHITE, 16, False, 550 , 570)
        # *AFTER* 
        pygame.display.flip()


# Pygame 結束
pygame.quit()
sys.exit(0)
# 

