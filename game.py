import pygame, sys


class Game:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.size = width, height
        self.screen = pygame.display.set_mode(self.size)

        # TODO Initialize all class veriables here
        self.enemies = []
        self.towers = []

    def start(self):
        while 1:
            self.update()
            self.draw()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw(self):
        self.screen.fill([0, 0, 0])
        pygame.display.flip()
