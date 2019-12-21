#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 16:50:33 2019

@author: Danny Meier
"""

import pygame
from SpriteLoader import SpriteLoader

class Map:
    def __init__(self, width, height, checkpoints):
        """
        (0,0)
        +-------------> x, width
        |
        |
        |
        |
        |
        \/
        y, height
        
        width: Spielfeldbreite
        height: Spielfeldhöhe
        checkpoints: Wegpunkte denen die Gegner folgen
            [ (x1,y1), (x2,y2), ... ]
        """
        self.width = width
        self.height = height
        self.checkpoints = checkpoints
        
    def draw(self, screen):
        pygame.draw.rect(screen, [255,255,255], (0, 0, self.width, self.height))
        
    def isBuildPlace(x,y):
        """
        Gibt Auskunft darüber, ob auf dem übergebenen Punkt gebaut werden kann.
        
        """
        pass