import pygame
from SpriteLoader import SpriteLoader


class BaseEnemy:
    def __init__(self, x, y, width=100, height=100):
        self.sprite_basename = "enemies"
        self.sprite_name = "base"
        self.sprite_loader = SpriteLoader()
        # self.sprite = self.sprite_loader.load_sprite(self.sprite_basename, self.sprite_name)
        self.color = [255, 0, 0]

        self.heigth = height
        self.width = width
        self.x = x
        self.y = y

    def update(self):
        if self.y < (800 - self.heigth):
            self.y += 0.25

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.heigth))
