import pygame, sys
from pygame.locals import *
class Ball(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > screen.get_width():
            self.speed[0] = -self.speed[0]
            hit_wall.play()
        if self.rect.top <= 0 :
            self.speed[1] = -self.speed[1]
            global score, score_font, score_surf
            score = score + 1
            score_surf = score_font.render(str(score), 1, [0,0,0])
            get_point.play()
class Paddle(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        img_surface = pygame.surface.Surface([100,20])
        img_surface.fill([0,0,0])
        self.image = img_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

pygame.init()
hit_wall = pygame.mixer.Sound("sounds/hit_wall.wav")
hit_wall.set_volume(0.4)
get_point = pygame.mixer.Sound("sounds/get_point.wav")
get_point.set_volume(0.2)
splat = pygame.mixer.Sound("sounds/splat.wav")
splat.set_volume(0.6)
new_life = pygame.mixer.Sound("sounds/new_life.wav")
new_life.set_volume(0.5)
bye = pygame.mixer.Sound("sounds/game_over.wav")
bye.set_volume(0.6)
screen = pygame.display.set_mode([640, 480])
clock = pygame.time.Clock()
ball_speed = [10,5]
myBall = Ball('wackyBall.bmp', ball_speed, [50,50])
ballGroup = pygame.sprite.Group(myBall)
paddle = Paddle([270, 400])
score = 0
score_font = pygame.font.Font(None, 50)
score_surf = score_font.render(str(score), 1, [0,0,0])
score_pos = [10,10]
lives = 3
running = True
done = False
pygame.mixer.music.load("sounds/bg_music.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
while running:
    clock.tick(30)
    screen.fill([255,255,255])
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            paddle.rect.centerx = event.pos[0]

    if pygame.sprite.spritecollide(paddle, ballGroup, False):
        myBall.speed[1] = -myBall.speed[1]

    myBall.move()
    if not done:
        screen.blit(myBall.image, myBall.rect)
        screen.blit(paddle.image, paddle.rect)
        screen.blit(score_surf, score_pos)
        for i in range (lives):
            width = screen.get_width()
            screen.blit(myBall.image, [width - 40 * i, 20])
        pygame.display.flip()
    if myBall.rect.top >= screen.get_rect().bottom:
        splat.play()
        lives = lives - 1
        if lives == 0:
            if not done:
                bye.play()
            final_text1 = "Game Over"
            final_text2 = "Your final score is:  " + str(score)
            ft1_font = pygame.font.Font(None, 70)
            ft1_surf = ft1_font.render(final_text1, 1, (0, 0, 0))
            ft2_font = pygame.font.Font(None, 50)
            ft2_surf = ft2_font.render(final_text2, 1, (0, 0, 0))
            screen.blit(ft1_surf, [screen.get_width()//2 - \
                    ft1_surf.get_width()//2, 100])
            screen.blit(ft2_surf, [screen.get_width()//2 - \
                    ft2_surf.get_width()//2, 200])
            pygame.display.flip()
            done = True
            pygame.mixer.music.fadeout(2000)
            myBall.speed = [0,0]
        else:
            pygame.time.delay(1000)
            if not done:
                new_life.play()
            myBall.rect.topleft = [50, 50]
            pygame.time.delay(1000)
pygame.quit()
