import pygame
from text import Text
from block import Block

class button:
    def __init__(self, surface, position = (0,0), width = 50, height = 50, msg = "", font_size = 20, line_w = 10, div = (5,4), color = (0,0,0), visible = True, line_only = False):
        self.rect = Block(surface, position,width, height, line_w, color, visible, line_only)
        self.text = Text(surface, msg, (position[0]+width/div[0], position[1]+height/div[1]), font_size, (255,255,255))

    def draw(self):
        self.rect.draw()
        self.text.draw()

    def get_rect(self):
        return self.rect.get_rect()