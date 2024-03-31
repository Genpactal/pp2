import pygame
import sys

pygame.init()

width = 1280
height = 800

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Red Ball')
fps = pygame.time.Clock()

x = 25
y = 25
radius = 25

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('White')

    pygame.draw.circle(screen, 'Red', (x, y), radius)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and x + radius < width: 
        x += 20
    if keys[pygame.K_LEFT] and x - radius > 0: 
        x -= 20
    if keys[pygame.K_DOWN] and y + radius < height:
        y += 20
    if keys[pygame.K_UP] and y - radius > 0:
        y -= 20

    pygame.display.update()
    fps.tick(60)