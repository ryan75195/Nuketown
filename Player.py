import math

import pygame

import Brain
import Map as mp
import main
import main as m
import numpy as np
import gun

class player:

    def spawn(self, team):
        if team == "red":
            return [230,70,0]
        if team == "green":
            return [266,455,0]

    def respawn(self, team):
        self.health = 100
        self.gun.reset()
        if team == "red":
            self.position = [230,70,0]
        if team == "green":
            self.position = [266,455,0]

    def __init__(self, name, team, gun, win, width):
        self.name = name
        self.team = team
        self.gun = gun
        self.position = self.spawn(self.team)
        self.health = 100
        self.killCount = 0
        self.deathCount = 0
        self.win = win
        self.width = width
        self.solids = mp.solidObjects()
        # self.pathfinding = graph

    def getX(self):
        return self.position[0]

    def getY(self):
        return self.position[1]

    def getZ(self):
        return self.position[2]

    def getPosition(self):
        return [self.getX(),self.getY(),self.getZ()]

    def getWidth(self):
        return m.width

    def getHeight(self):
        return m.height

    def getName(self):
        return self.name

    def getTeam(self):
        return self.team

    def getAmmo(self):
        return self.gun.getAmmo()

    def getAmmoInClip(self):
        return self.gun.getBulletsInClip()

    def getKillCount(self):
        return self.killCount

    def getHealth(self):
        return self.health

    def getDeathCount(self):
        return self.deathCount

    def damage(self, amount):
        self.health -= amount

    def walk(self, direction):
        if direction == "left" and self.position[0] > m.vel and [self.position[0] - m.vel, self.position[1]] not in self.solids:
            self.position[0] -= m.vel
        if direction == "right" and (self.position[0] < m.screenWidth - m.width - m.vel) and [self.position[0] + m.vel, self.position[1]] not in self.solids:
            self.position[0] += m.vel
        if direction == "up" and self.position[1] > m.vel and [self.position[0], self.position[1] - m.vel] not in self.solids:
            self.position[1] -= m.vel
        if direction == "down" and self.position[1] < m.screenHeight - m.height - m.vel and [self.position[0], self.position[1] + m.vel] not in self.solids:
            self.position[1] += m.vel

    def isDead(self):
        if self.health <= 0:
            return True
        else:
            return False

    def getDistance(self,player):
        return int(((player.getX() - self.getX())**2 + (player.getY() - self.getY())**2)**0.5)

    def walkTo(self, Position, breakCondition,spacing, solids, AI):

        directions = AI.getPath(self.getPosition()[:2], Position)
        # print(len(directions))
        counter = 0
        for point in directions:
            # print(counter)
            counter += 1
            if point:
                print(point)
                # print(point)
                # self.walk(point)
                self.walk(point)


                self.win.fill((0, 0, 0))
                self.win.blit(main.bg, (0, 0))
                pygame.draw.rect(self.win, (0, 255, 0), (self.getX(), self.getY(), self.width, self.width))
                pygame.display.update()
                pygame.time.delay(200)



    def canSee(self, player):
        solids = np.array(self.solids)
        m = ((player.getY() - self.getY())/(player.getX() - self.getX()))
        b = player.getY()
        a = player.getX()
        visible = True
        lineCoords = []
        for point in solids:
            y = int(m * (point[0] - a) + b)
            if point[1] == y and ((y <= max(self.getY(), player.getY())) and (y >= min(self.getY(), player.getY()))) and ((point[0] >= min(self.getX(), player.getX())) and (point[0] <= max(self.getX(), player.getX()))):
                visible = False
        return visible

    def kill(self, player, win):
        if self.canSee(player, win):
            pygame.draw.line(win,(0,0,255), (self.getX(), self.getY()), (player.getX(), player.getY()))
            pygame.display.flip()
            self.gun.shoot(player)

        if player.isDead():
            player.respawn(player.getTeam())
            self.killCount += 1
            player.deathCount += 1
