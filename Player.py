import pygame
import Map as mp
import main as m
import numpy as np

class player:

    def Spawn(self, team):
        if team == "red":
            return [230,70,0]
        if team == "green":
            return [266,455,0]

    def __init__(self, name, team, gun):
        self.name = name
        self.team = team
        self.gun = gun
        self.position = self.Spawn(self.team)
        self.health = 100

    def getX(self):
        return self.position[0]

    def getY(self):
        return self.position[1]

    def getZ(self):
        return self.position[2]

    def getWidth(self):
        return m.width

    def getHeight(self):
        return m.height

    def getTeam(self):
        return self.team

    def walk(self, direction):
        if direction == "left" and self.position[0] > m.vel and [self.position[0] - m.vel, self.position[1]] not in mp.solidObjects():
            self.position[0] -= m.vel
        if direction == "right" and (self.position[0] < m.screenWidth - m.width - m.vel) and [self.position[0] + m.vel, self.position[1]] not in mp.solidObjects():
            self.position[0] += m.vel
        if direction == "up" and self.position[1] > m.vel and [self.position[0], self.position[1] - m.vel] not in  mp.solidObjects():
            self.position[1] -= m.vel
        if direction == "down" and self.position[1] < m.screenHeight - m.height - m.vel and [self.position[0], self.position[1] + m.vel] not in  mp.solidObjects():
            self.position[1] += m.vel

    def isDead(self):
        if health <= 0:
            return True
        else:
            return False

    def getDistance(self,player):
        return int(((player.getX() - self.getX())**2 + (player.getY() - self.getY())**2)**0.5)
    #
    def canSee(self, player, win):
        solids = np.array(mp.solidObjects())
        m = ((player.getY() - self.getY())/(player.getX() - self.getX()))
        b = player.getY()
        a = player.getX()
        visible = True
        lineCoords = []
        for point in solids if point[1] == m*point[0] - m*a + b:
             print("wall at {}".format(point))
             pygame.draw.rect(win,(0,255,255), (point[0],point[1],1,1))
             visible = False
        return visible

        # def draw(self,x,y):
