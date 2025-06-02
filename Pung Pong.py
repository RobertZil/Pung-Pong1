from pygame import *
from random import randint

init()
font.init()

LIGHT_BLUE = (173, 216, 230)
WHITE = (255, 255, 255)

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Pung Pong")

clock = time.Clock()
FPS = 60

font1 = font.Font(None, 35)
lose1 = font1.render("Player 1 LOSES!", True, (180, 0, 0))
lose2 = font1.render("Player 2 LOSES!", True, (180, 0, 0))

finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - self.rect.height - 5:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - self.rect.height - 5:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, player_image, x, y, width, height, speed_x, speed_y):
        super().__init__(player_image, x, y, width, height, 0)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= win_height:
            self.speed_y *= -1

        if self.rect.colliderect(player1.rect) or self.rect.colliderect(player2.rect):
            self.speed_x *= -1


img_hero = "ruby-red.png"    
img_ball = "Pung Pong.png"    

player1 = Player1(img_hero, 30, win_height / 2 - 50, 20, 100, 7)
player2 = Player2(img_hero, win_width - 50, win_height / 2 - 50, 20, 100, 7)
ball = Ball(img_ball, win_width / 2 - 15, win_height / 2 - 15, 30, 30, 5, 5)

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.fill(LIGHT_BLUE)

        player1.update()
        player2.update()
        ball.update()

        
        if ball.rect.left <= 0:
            finish = True
            window.blit(lose1, (200, 200))
        elif ball.rect.right >= win_width:
            finish = True
            window.blit(lose2, (200, 200))

        player1.reset()
        player2.reset()
        ball.reset()
    else:
       
        if ball.rect.left <= 0:
            window.blit(lose1, (200, 200))
        elif ball.rect.right >= win_width:
            window.blit(lose2, (200, 200))
            
    display.update()
    clock.tick(FPS)

quit()
