import pygame
import random
import Player

pygame.init()



screenWidth = 512
screenHeight = 512

bg = pygame.image.load("map.png")

x = 230
y = 70
width = 2.5
height = 2.5
vel = 0.5

def draw():
    win.fill((0,0,0))
    win.blit(bg,(0,0))
    pygame.draw.rect(win,(255,0,0), (x,y,width,height))
    pygame.display.update()


win = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Nuketown")

run = True

while run:
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screenWidth - width - vel:
        x += vel
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y < screenHeight - height - vel:
        y += vel
    draw()
pygame.quit()
