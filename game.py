import sys
import pygame
from enemies.BaseEnemy import BaseEnemy
from map.Map import Map


class Game:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.size = width, height
        self.screen = pygame.display.set_mode(self.size)

        # TODO Initialize all class veriables here
        self.enemies = []
        self.towers = []
        self.map = Map(500,500, [])
        self.base_enemy = BaseEnemy(10, 10)

    def start(self):
        while 1:
            self.update()
            self.draw()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.base_enemy.update()

    def draw(self):
        self.screen.fill([0, 0, 0])
        self.map.draw(self.screen)
        self.base_enemy.draw(self.screen)
        pygame.display.update()

    def spawn_enemy(self):
        self.enemies.append()
