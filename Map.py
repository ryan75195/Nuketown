from datetime import datetime, timedelta

import cv2
import numpy as np

# import pygame
#
# map = cv2.imread("mapped.jpg", 0)
# cv2.imshow("image", map)
# cv2.waitKey(5000)
import math


def formatString(obj):
    ret = []
    x = []
    y = []
    onY = False

    for i in obj:

        if i == "[":
            onY = False
        if i == ",":
            onY = True

        if i.isdigit():
            if not onY:
                x.append(i)
            elif onY:
                y.append(i)

        if i == "]":
            add = []
            x1 = ''.join(x)
            y1 = ''.join(y)
            # print(x1)
            if x1 != '':
                add.append(int(x1))
            if y1 != '':
                add.append(int(y1))
            ret.append(add)
            add = []
            x = []
            y = []

    return ret


coords = open("Coordinates.txt").read().splitlines()
coordinates = {}
objects = ["walls", "buildings", "stairs", "ujs", "djs", "exits"]

for i in range(len(coords)):
    coordinates[objects[i]] = coords[i]

walls = formatString(coordinates["walls"])
buildings = formatString(coordinates["buildings"])
stairs = formatString(coordinates["stairs"])
ujs = formatString(coordinates["ujs"])
djs = formatString(coordinates["djs"])
exits = formatString(coordinates["exits"])



def solidObjects():
    ret = []
    for i in walls:
        ret += [i]
    for i in buildings:
        ret += [i]

    return [x for x in ret if x != []]
# def createMap():

def lineEqn(point1, point2):
    if point1[0] - point2[0] != 0:
        m = (point1[1] - point2[1]) / (point1[0] - point2[0])
        y = (m * (point2[0] - point1[0]) + point1[1])
        c = m * (point2[0] - point1[0]) + y
        return m, c
    else:
        return 0

    print(f"y = {m}x + {c}")

def canSee(point1, point2, spacing, solids):
    currentTime = datetime.now()
    m = ((point1[1] - point2[1])/(point1[0]-point2[0]+0.001))
    b = point1[1]
    a = point1[0]
    visible = True
    lineCoords = []
    for point in solids:
        # print(point)
        y = int(m * (point[0] - a) + b)
        if distance([0,y], [0,point[1]]) <= spacing and ((y <= max(point1[1],point2[1])) and (y >= min(point1[1],point2[1]))) and ((point[0] >= min(point1[0],point2[0])) and (point[0] <= max(point1[0],point2[0]))):
            visible = False
    return visible

# def collision(point1, point2, objects):
#     m,c = lineEqn(point1, point2)
#     for point in objects:
#         for i in range(round(((point1[0]-point2[0])**2)**0.5)):
#             # print(i)
#             x = point1[0] + i
#             y = m * x + c
#             if(math.floor(distance([x,y],point)) == 0):
#                 # print("ya")
#                 # exit(0)
#                 return True
#     return False

def distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5
    # y = m(x-point1[0]) + point1[1]