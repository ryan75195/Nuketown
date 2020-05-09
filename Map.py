import cv2
import numpy as np

# import pygame
#
# map = cv2.imread("mapped.jpg", 0)
# cv2.imshow("image", map)
# cv2.waitKey(5000)


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
