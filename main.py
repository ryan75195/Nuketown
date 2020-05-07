import pygame
import random
import Player
import Map as mp
import numpy as np

pygame.init()



screenWidth = 512
screenHeight = 512
width = 3.5
height = 3.5
vel = 1

bg = pygame.image.load("map.png")


def showCoordinates(window, player):

    white = (255, 255, 255)
    black = (0,0,0)

    font = pygame.font.Font('freesansbold.ttf', 10)
    text = font.render('x={},y={},z={}'.format(player.getX(),player.getY(),0), True, white, black)
    textRect = text.get_rect()
    textRect.center = (50, 10)
    window.blit(text, textRect)

# 171,93
def drw(win, players, currentPlayer = None):
    win.fill((0,0,0))
    win.blit(bg,(0,0))

    if currentPlayer != None:
        showCoordinates(win, currentPlayer)
    # pygame.draw()
    for player in players:
        # showCoordinates(win, player)
        if player.getTeam() == "red":
            pygame.draw.rect(win,(255,0,0), (player.getX(),player.getY(),player.getWidth(),player.getHeight()))
        else:
            pygame.draw.rect(win,(0,255,0), (player.getX(),player.getY(),player.getWidth(),player.getHeight()))



    pygame.display.update()


def runGame():
    # global x
    # global y
    # global vel



    win = pygame.display.set_mode((screenWidth,screenHeight))
    pygame.display.set_caption("Nuketown")

    allPlayers = np.array([])
    allPlayers = np.append(allPlayers,Player.player("Player1", "red", "DSR"))
    allPlayers = np.append(allPlayers,Player.player("Player2", "green", "DSR"))
    currentPlayer = 0

    run = True

    while run:
        # print()
        cur = allPlayers[currentPlayer]
        next = allPlayers[nextPlayer(currentPlayer,allPlayers)]
        pygame.draw.line(win,(0,0,0), (cur.getX(), cur.getY()), (next.getX(), next.getY()))
        pygame.display.flip()
        pygame.time.delay(20)
        print(cur.canSee(next, win))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            keys = pygame.key.get_pressed()


        if keys[pygame.K_s]:
            currentPlayer = nextPlayer(currentPlayer, allPlayers)

        if keys[pygame.K_LEFT]:
            allPlayers[currentPlayer].walk("left")
        if keys[pygame.K_RIGHT]:
            allPlayers[currentPlayer].walk("right")
        if keys[pygame.K_UP]:
            allPlayers[currentPlayer].walk("up")
        if keys[pygame.K_DOWN]:
            allPlayers[currentPlayer].walk("down")
        drw(win, allPlayers, cur)
    pygame.quit()

def nextPlayer(currentPlayer, allPlayers):
    if currentPlayer == len(allPlayers) - 1:
        currentPlayer = 0
    else:
        currentPlayer += 1
    return currentPlayer
