import pygame


class SpriteLoader:
    def __init__(self):
        self.resource_path = "/resources/images/"

    def load_sprite(self, base_path, sprite):
        return pygame.image.load(self.resource_path + base_path + "/" + sprite)
