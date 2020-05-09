import pygame
import Map as mp
import main as m
import numpy as np
import time

class gun:

    def __init__(self, name, type, ammo, clipSize, damage):
        self.name = name
        self.type = type
        self.ammo = ammo
        self.clipSize = clipSize
        self.bulletsInClip = clipSize
        self.damage = damage
        self.lastShot = pygame.time.get_ticks()

        self.maxammo = ammo

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getAmmo(self):
        return self.ammo

    def getBulletsInClip(self):
        return self.bulletsInClip

    def getClipSize(self):
        return self.clipSize

    def getLastShot(self):
        return self.lastShot

    def reset(self):
        self.ammo = self.maxammo
        self.bulletsInClip = self.clipSize

    def shoot(self,player):
        cooldown = 2000
        if pygame.time.get_ticks() - self.lastShot >= cooldown and self.bulletsInClip > 0:
            player.damage(self.damage)
            self.bulletsInClip -= 1
            if self.getBulletsInClip() == 1 and self.getAmmo() == 1:
                self.bulletsInClip = 0
                self.ammo = 0
            self.lastShot = pygame.time.get_ticks()
        if self.bulletsInClip == 0 and self.ammo > 0:
            self.reload()
        if self.getBulletsInClip() == 0 and self.getAmmo() == 0:
            print("out of ammo")

    def reload(self):
        cooldown = 5000
        if pygame.time.get_ticks() - self.lastShot >= cooldown:
            if self.ammo - self.clipSize >= 0:
                self.ammo -= self.clipSize
                self.bulletsInClip = self.clipSize
            else:
                self.bulletsInClip = self.ammo
            self.lastShot = pygame.time.get_ticks()
