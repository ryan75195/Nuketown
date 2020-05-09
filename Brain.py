import numpy
import Player
import pygame
import Map



class hardcoded:
    def __init__(self, allPlayers):
        self.allPlayers = allPlayers
        self.Player1 = allPlayers[0]
        self.Player2 = allPlayers[1]

    def detectWalls(self,Player):
        objects = Map.solidObjects()
        dy_l = ["up", "down"]
        dx_l = ["left", "right"]
        dy_v = [Player.getY() - 1, Player.getY() + 1]
        dx_v = [Player.getX() - 1, Player.getX() + 1]
        d_t = [False,False,False,False]

        x = Player.getX()
        y = Player.getY()
        count = 0
        for i in dy_v:
            if [x,i] in objects:
                d_t[count] = True
            count+=1
        for i in dx_v:
            if [i,y] in objects:
                d_t[count] = True
            count+=1
        return d_t


    def run():

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        distance = self.Player1.getDistance(self.Player2)


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

# class Neuron
#
#     def __init__(feature, weight):
#         self.feature = feature
#         self.weight = weight
#
#     def step_function():
#         activate = 0
#         if feature*weight > 0:
#             activate = 1
#         return activate
#
#     def fire(activate):
#         if activate == 1:
#             return True
#         else:
#             return False
