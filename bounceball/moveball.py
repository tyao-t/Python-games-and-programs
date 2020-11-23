import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640, 480])
background = pygame.Surface(screen.get_size())
background.fill([255, 255, 255])
clock = pygame.time.Clock()

class Ball(pygame.sprite.Sprite):
    def __init__(self, img_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        if self.rect.left <= screen.get_rect().left or \
                self.rect.right >= screen.get_rect().right:
            self.speed[0] = -self.speed[0]
        newpos = self.rect.move(self.speed)
        self.rect = newpos

myball = Ball('beach_ball.png', [10,0], [20,20])
pygame.time.set_timer(pygame.USEREVENT, 1000)
direction = 1
running = True
pygame.key.set_repeat(100, 50)
held_down = False
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            held_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            held_down = False
        elif event.type == pygame.MOUSEMOTION: 
            if held_down:
                myball.rect.center = event.pos
        elif event.type == pygame.USEREVENT:
            myball.rect.centery = myball.rect.centery + (30*direction)
            if myball.rect.top <= 0 or \
                    myball.rect.bottom >= screen.get_rect().bottom:
                direction = -direction 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                myball.rect.top = myball.rect.top - 10
            elif event.key == pygame.K_DOWN:
                myball.rect.top = myball.rect.top + 10
    clock.tick(30)
    screen.blit(background, [0,0])
    myball.move()
    screen.blit(myball.image, myball.rect)
    pygame.display.flip()
pygame.quit()
