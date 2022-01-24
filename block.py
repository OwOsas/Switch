import pygame

class Block:
    def __init__(self, surface, position = (0,0), width = 50, height = 50, line_w = 10, color = (0,0,0), visible = True, line_only = False):
        self.position = position
        self.visible = visible
        self.surface = surface
        self.color = color
        self.width = width
        self.height = height
        self.line_w = line_w
        self.line_only = line_only

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def draw(self):
        if self.line_only:
            self.r = pygame.draw.rect(self.surface, (0,0,0), (self.position[0], self.position[1], self.width, self.height), 2)
        else:
            if self.visible == True:
                self.r = pygame.draw.rect(self.surface, self.color, (self.position[0], self.position[1], self.width, self.height))
                if self.line_w > 0:
                    self.r = pygame.draw.rect(self.surface, (125,125,125), (self.position[0], self.position[1], self.width, self.height), self.line_w)
            else:
                self.r = pygame.draw.rect(self.surface, (0,0,0), (self.position[0], self.position[1], self.width, self.height), -1)

    def get_rect(self):
        return self.r