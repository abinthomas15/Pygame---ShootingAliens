import pygame
import os

from pygame.constants import KEYDOWN
pygame.init

WIDTH = 900
HEIGHT = 500
FPS = 60
WHITE = (255,255,255)

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('ShootingBlocks')
SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
SPACESHIP = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_IMAGE,(80,50)),180)
BACKGROUND = pygame.image.load(os.path.join('Assets','space.png'))

def draw_window(ship,bullet):
    WIN.blit(BACKGROUND,(0,0))
    WIN.blit(SPACESHIP,(ship.x,ship.y))
    pygame.display.update()

    for bullets in bullet:
        pygame.draw(WIN,(255,255,0),bullets)

def spaceship_pressed(key_pressed,ship):
    if key_pressed [pygame.K_LEFT] and ship.x > 20:
        ship.x -= 5
    if key_pressed [pygame.K_RIGHT] and ship.x < WIDTH - 100:
        ship.x += 5

def handle_bullets(bullet):
    for bullets in bullet:
        bullets.y -= 7

def main():
    ship = pygame.Rect(400,450,80,40)
    clock = pygame.time.Clock() 
    ship_bullet = []
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_RCTRL:
                    bullet = pygame.Rect(ship.x + ship.width, ship.y+ship.height//2 - 2, 10,5)
                    ship_bullet.append(bullet)
        key_pressed = pygame.key.get_pressed()
        spaceship_pressed(key_pressed,ship)
        handle_bullets(ship_bullet)
        draw_window(ship,ship_bullet)
    pygame.quit()


if __name__ == '__main__':
    main()