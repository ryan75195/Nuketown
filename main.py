import pygame
import random
import Player
import Map as mp
import numpy as np
import gun
import Brain

pygame.init()



screenWidth = 512
screenHeight = 512
width = 3.5
height = 3.5
vel = 1

bg = pygame.image.load("map.png")

def showScore(window, players):
    white = (255, 255, 255)
    black = (0,0,0)
    y = 10
    font = pygame.font.Font('freesansbold.ttf', 10)

    for player in players:
        text = font.render('Player: {}, Kills: {}, Deaths: {}, Team: {}'.format(player.getName(),player.getKillCount(), player.getDeathCount(), player.getTeam() ,0), True, white, black)
        y += 10
        window.blit(text, (10,y))

def showStats(window, player, x, y):
    white = (255, 255, 255)
    black = (0,0,0)
    font = pygame.font.Font('freesansbold.ttf', 10)
    strings = ['Name','Health','Ammo','Clip','Position']
    functions = [player.getName(),player.getHealth(), player.getAmmo(), player.getAmmoInClip(), player.getPosition()]

    for i in range(len(strings)):
        text = font.render('{}: {}'.format(strings[i], functions[i],0), True, white, black)
        window.blit(text, (x,y))
        y += 10



# 171,93
def drw(win, players, Stats, currentPlayer = None):
    win.fill((0,0,0))
    win.blit(bg,(0,0))
    showScore(win,players)
    for player in players:
        # showCoordinates(win, player)
        # if Stats == True:

        if player.getTeam() == "red":
            showStats(win,player, 400,10)
            pygame.draw.rect(win,(255,0,0), (player.getX(),player.getY(),player.getWidth(),player.getHeight()))
        else:
            showStats(win,player, 400, 450)
            pygame.draw.rect(win,(0,255,0), (player.getX(),player.getY(),player.getWidth(),player.getHeight()))

    pygame.display.update()


def setupPlayers():
    DSR1 = gun.gun("DSR", "Sniper", 50, 7, 50)
    DSR2 = gun.gun("DSR", "Sniper", 50, 7, 50)

    allPlayers = np.array([])
    allPlayers = np.append(allPlayers,Player.player("Player1", "red", DSR1))
    allPlayers = np.append(allPlayers,Player.player("Player2", "green", DSR2))
    return allPlayers

def runGame():

    win = pygame.display.set_mode((screenWidth,screenHeight))
    pygame.display.set_caption("Nuketown")
    allPlayers = setupPlayers()
    currentPlayer = 0
    run = True
    showStats = False

    while run:

        cur = allPlayers[currentPlayer]
        next = allPlayers[nextPlayer(currentPlayer,allPlayers)]
        # pygame.draw.line(win,(0,0,0), (cur.getX(), cur.getY()), (next.getX(), next.getY()))
        # pygame.display.flip()
        pygame.time.delay(20)

        AI = Brain.hardcoded(allPlayers)
        print(AI.detectWalls(cur))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            keys = pygame.key.get_pressed()

        if keys[pygame.K_s]:
            currentPlayer = nextPlayer(currentPlayer, allPlayers)

        if keys[pygame.K_q]:
            showStats = not showStats

        if keys[pygame.K_k]:
            cur.kill(next, win)

        if keys[pygame.K_LEFT]:
            allPlayers[currentPlayer].walk("left")
        if keys[pygame.K_RIGHT]:
            allPlayers[currentPlayer].walk("right")
        if keys[pygame.K_UP]:
            allPlayers[currentPlayer].walk("up")
        if keys[pygame.K_DOWN]:
            allPlayers[currentPlayer].walk("down")

        drw(win, allPlayers, showStats, cur)
    pygame.quit()

def nextPlayer(currentPlayer, allPlayers):
    if currentPlayer == len(allPlayers) - 1:
        currentPlayer = 0
    else:
        currentPlayer += 1
    return currentPlayer
