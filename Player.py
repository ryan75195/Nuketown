import pygame


class Player:

    def __init__(self, name, team, position, health, gun):
        self.name = name
        self.team = team
        self.position = position
        self.health = health
        self.gun = gun
