import pygame
from block import Block

class grid:
    def __init__(self, block, color):
        self.block = block
        self.left = None
        self.right = None
        self.top = None
        self.bot = None
        self.color = color
        #True == white, False == black

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def set_top(self, top):
        self.top = top

    def set_bot(self, bot):
        self.bot = bot

    def get_left(self, left):
        return self.left

    def get_right(self, right):
        return self.right

    def get_top(self, top):
        return self.top

    def get_bot(self, bot):
        return self.bot

    def draw(self):
        self.block.draw()

    def set_self(self, blcok):
        self.block = blcok

    def get_self(self):
        return self.block

    def change_color(self):
        black = (0,0,0)
        white = (255,255,255)
        if self.color:
            self.block.set_color(black)
            self.color = False
        else:
            self.block.set_color(white)
            self.color = True

    def get_rect(self):
        return self.block.get_rect()

    def click(self):
        self.change_color()
        if self.right != None:
            self.right.change_color()
        if self.left != None:
            self.left.change_color()
        if self.top != None:
            self.top.change_color()
        if self.bot != None:
            self.bot.change_color()
    
    def get_color(self):
        return self.color