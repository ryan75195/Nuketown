import ast
from random import random, randint

import numpy as np
import Map as mp

import Player
import pygame
import Map
import main


class graph:
    def __init__(self, filename,win, width, height):
        self.filename = filename
        self.win = win
        self.width = width
        self.height = height
        self.graph = ast.literal_eval(self.loadGraph(filename,win, width, height))
        # print(self.pathfinding)
        # print(self.pathfinding['(230, 70)'])
        # exit(0)

    def getNodeSpacing(self, name):
        if name == "Nuketown-Nodes.txt":
            return 5

    def bfs(self, start, end):
        visited = []

    def displayGrid(self):
        # grid = self.graph
        bg = pygame.image.load("map.png")
        self.win.fill((0, 0, 0))
        self.win.blit(bg, (0, 0))
        for point in (self.graph.keys()):
            print(ast.literal_eval(point)[0])
            pygame.draw.rect(self.win, (255, 0, 0), (ast.literal_eval(point)[0], ast.literal_eval(point)[1], 1, 1))
            pygame.display.update()


    def loadGraph(self,filename,win, width, height):
        try:
            file = open(filename, "r")
            dictstr = file.read()
            # print((ast.literal_eval(dictstr)['(230, 70)']))
        except Exception:
            self.createGraph(filename,win, width, height)
            file = open(filename, "r")
            dictstr = file.read()
            # print((ast.literal_eval(dictstr)['(230, 70)']))


        return dictstr

    def createGraph(self, filename,win, width, height):
        # print(len(walls))
        # exit(0)
        validPositions = [[]]
        position = (230, 70)
        queue = set()
        queue.add(position)
        gridSpacing = 2
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
        moveset = []
        moveset.append(Point1)
        last = Point1
        current = Point1

        checked = 0
        queue = set()
        distances = []
        visited = []
        blacklist = []
        while mp.distance(Point2, current) > 5 or Point2 == current:
            distances = []
            for neighbour in self.graph[f'({current[0]}, {current[1]})']:
                if len(moveset) > 0 and neighbour != current and neighbour not in blacklist:
                    # print(neighbour)
                    distances.append(mp.distance(neighbour,Point2))
                else:
                    distances.append(9999)

            closest = self.graph[f'({current[0]}, {current[1]})'][distances.index(min(distances))]
            print(distances)
            while closest in blacklist:
               if all(x for x in distances if x == 9999):
                   blacklist.append(current)
                   current = visited[-1]
                   print(current)
                   visited = visited[:-1]
                   break
                   # current = closest
                   # break
               else:
                   distances[distances.index(min(distances))] = 9999
                   closest = self.graph[f'({current[0]}, {current[1]})'][distances.index(min(distances))]

            if closest in visited and closest not in blacklist:
                blacklist.append(current)
                # last = current
                current = closest
            # pygame.time.delay(20)


            # else:
            visited.append(closest)
            # current = closest
            print(mp.distance(current,Point2))
            print(blacklist)
            moveset = np.append(moveset, current)

            bg = pygame.image.load("map.png")
            win.fill((0, 0, 0))
            win.blit(bg, (0, 0))
            pygame.draw.rect(win, (255, 0, 0), (current[0], current[1], width, width))
            pygame.display.update()

        return moveset

    def getPath(self, Point1, Point2):
            current = Point1
            moveset = []
            lastMove = None
            blacklist = []

            while mp.distance(Point2, current) > 5 or Point2 == current:
                #STEP1: Check all Points around current position, store in table with position and distance from goal
                options = []
                distances = []

                for neighbour in self.graph[f'({current[0]}, {current[1]})']:
                    if neighbour != lastMove and neighbour not in blacklist:
                       options.append(neighbour)
                       if neighbour not in moveset:
                        distances.append(mp.distance(neighbour,Point2))
                       else:
                        distances.append(999)
                #STEP2: Select point that brings player closest to point 2, with previous point lowest prioroty

                # print(len(options))

                if len(options) > 0:
                    nextMove = options[distances.index(min(distances))]
                else:
                    blacklist.append(current)
                    nextMove = lastMove

                moveset.append(nextMove)
                print(nextMove)
                lastMove = current
                current = nextMove

                #STEP3: if stuck in corner and no valid path, select previous path.



                bg = pygame.image.load("map.png")
                self.win.fill((0, 0, 0))
                self.win.blit(bg, (0, 0))
                pygame.draw.rect(self.win, (255, 0, 0), (moveset[-1][0], moveset[-1][1], self.width, self.width))
                pygame.display.update()
                # pygame.time.delay(20)
            print(len(moveset))
            directions = []
            for i in moveset:
                if moveset.index(i) < len(moveset) - 1:
                    # print(self.getDirection(i, moveset[moveset.index(i) + 1]))
                    directions.append(self.getDirection(i, moveset[moveset.index(i) + 1]))
                    directions.append(self.getDirection(i, moveset[moveset.index(i) + 1]))
            print(directions[:5])
            return directions

    def getDirection(self, currentPoint, nextPoint):
         ##up or down
         if currentPoint[0] == nextPoint[0]:
             if currentPoint[1] < nextPoint[1]:
                 return "down"
             elif currentPoint[1] > nextPoint[1]:
                 return "up"
         ##left or right

         elif currentPoint[1] == nextPoint[1]:
            if currentPoint[0] < nextPoint[0]:
                return "left"
            elif currentPoint[0] > nextPoint[0]:
                return "right"

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
