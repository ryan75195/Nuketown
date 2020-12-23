import ast

import numpy as np
import Map as mp

import Player
import pygame
import Map
import main


class graph:
    def __init__(self, graphName):
        self.graph = ast.literal_eval(self.loadGraph(graphName))
        # print(self.pathfinding)
        # print(self.pathfinding['(230, 70)'])
        # exit(0)

    def getNodeSpacing(self, name):
        if name == "Nuketown-Nodes.txt":
            return 5

    def bfs(self, start, end):
        visited = []

    def loadGraph(self,filename):
        file = open(filename, "r")
        dictstr = file.read()
        print((ast.literal_eval(dictstr)['(230, 70)']))
        return dictstr

    def createGraph(self, filename,win, width, height):
        walls = mp.solidObjects()
        print(len(walls))
        # exit(0)
        validPositions = [[]]
        position = (230, 70)
        queue = set()
        queue.add(position)
        gridSpacing = 5
        graph = {}
        file = open(filename, "a")
        solids = np.array(mp.solidObjects())
        while len(queue) > 0:
            node = queue.pop()
            pygame.draw.rect(win, (0, 255, 0), (node[0], node[1], width, height))
            pygame.display.update()
            # print(len(queue))
            neighbours = [[node[0] + gridSpacing, node[1]], [node[0] - gridSpacing, node[1]],
                          [node[0], node[1] + gridSpacing], [node[0], node[1] - gridSpacing]]
            ##                  move right                             move left                            move up                             move down
            if f"{node}" not in graph.keys():
                graph[str(node)] = []
                # print(eval(str(node)))
            for adjacent in neighbours:
                # print(adjacent)
                if mp.canSee(adjacent, [node[0], node[1]], gridSpacing, solids):
                    graph[f"{node}"] += [adjacent]
                    if (adjacent[1], adjacent[1]) not in queue and adjacent not in validPositions:
                        # print(mp.canSee(adjacent, [node[0], node[1]]), (adjacent[0],adjacent[1]) not in queue, adjacent not in validPositions )
                        validPositions.append(adjacent)
                        queue.add((adjacent[0], adjacent[1]))

                    # print(validPositions[1])
        file.write(repr(graph))
        return validPositions

    def Astar(self, Point1, Point2, win, width):
        current = Point1
        # end = Point2
        moveSet = [[]]
        # next = set()
        # pathCost = {}
        #
        #
        # while current != Point2:
        #     current = next.pop()

        blacklisted = []
        last = []
        PathDistances = {}



        # chance to dp where a table is stored with all the distences from all routes and chose a route, if val
        # is already calculated use it if not then calculate it, shortest valued route wins.

        while current != Point2:
            print(mp.distance(current, Point2))
            currentMoves = self.graph[f'({current[0]}, {current[1]})']
            closest = [-999,-999]


            for move in currentMoves:
                if mp.distance(move,Point2) < mp.distance(closest,Point2) and move not in moveSet and move != [] and move not in blacklisted:
                    closest = move
                # else:

            if closest == [-999,-999]:
                blacklisted.append(current)
                # current = last
                rand = np.random.random_integers(0, len(currentMoves) - 1, 1)
                closest = currentMoves[rand[0]]

            moveSet.append(closest)
            last = current
            current = closest



            # print(1)

        return moveSet




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


    # def run():
    #
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             run = False
    #
    #     distance = self.Player1.getDistance(self.Player2)
    #
    #
    #     if keys[pygame.K_s]:
    #         currentPlayer = nextPlayer(currentPlayer, allPlayers)
    #
    #     if keys[pygame.K_q]:
    #         showStats = not showStats
    #
    #     if keys[pygame.K_k]:
    #         cur.kill(next, win)
    #
    #     if keys[pygame.K_LEFT]:
    #         allPlayers[currentPlayer].walk("left")
    #     if keys[pygame.K_RIGHT]:
    #         allPlayers[currentPlayer].walk("right")
    #     if keys[pygame.K_UP]:
    #         allPlayers[currentPlayer].walk("up")
    #     if keys[pygame.K_DOWN]:
    #         allPlayers[currentPlayer].walk("down")

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
