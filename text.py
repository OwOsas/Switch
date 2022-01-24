import pygame

class Text:
    def __init__(self, surface, msg, position = (0,0), font_size = 20, color = (255,255,255), visible = True):
        self.position = position
        self.visible = visible
        self.msg = msg
        self.surface = surface
        self.color = color
        self.font_size = font_size

    def draw(self):
        if self.visible:
            self.surface.blit(pygame.font.SysFont(None, self.font_size).render(self.msg, True, self.color), self.position)
            
    def set_pos(self, pos):
        self.position = pos

    #set message
    def set_msg(self, msg):
        self.msg = msg