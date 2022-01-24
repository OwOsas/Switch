from block import Block
from grid import grid
from text import Text
from button import button
import pygame
import random

pygame.init()

def mouse_intersect(mouse_po, rect) :
    if ((mouse_po[0] > rect.x) and (mouse_po[0] < rect.x + rect.width) and (mouse_po[1] > rect.y) and (mouse_po[1] < rect.y + rect.height)):
        return True
    return False

def generate(size, surface, r):
    i = 0
    y = 0
    w, h = pygame.display.get_surface().get_size()
    w = w / size
    h = h / size
    black = (0,0,0)
    white = (255,255,255)
    line_w = int(h * 0.05)
    line = []
    if r:
        while i < size:
            c = 0
            x = 0
            roll = []
            while c < size:
                random_bool = bool(random.getrandbits(1))
                if random_bool:
                    color = white
                else:
                    color = black
                roll.append(grid(Block(surface,(x,y), w, h, line_w, color), random_bool))
                x += w
                c += 1
            line.append(roll)
            y += h
            i += 1
    else:
        while i < size:
            c = 0
            x = 0
            roll = []
            while c < size:
                roll.append(grid(Block(surface,(x,y), w, h, line_w), False))
                x += w
                c += 1
            line.append(roll)
            y += h
            i += 1
    
    for l in range(size):
        for g in range(size):
            #set right
            if g != size-1:
                line[l][g].set_right(line[l][g+1])
            #set left
            if g != 0:
                line[l][g].set_left(line[l][g-1])
            #set top
            if l != 0:
                line[l][g].set_top(line[l-1][g])
            #set bot
            if l != size-1:
                line[l][g].set_bot(line[l+1][g])
    return line




run = True

while run:
    display = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("v 0.0.1")
    size = 5
    delay = 17
    frame = 0
    w, h = pygame.display.get_surface().get_size()
    #menu objects
    choose = Text(display,"Choose your difficulty", (w/2-170, h/4), 50)
    three = button(display, ((w/2-50, h/2-50)),100,50,"3x3",47, 10)
    five = button(display, ((w/2-50, h/2+10)),100,50,"5x5",47, 10)
    eight = button(display, ((w/2-50, h/2+70)),100,50,"8x8",47, 10)

    in_menu = True
    while in_menu and run:
        pygame.time.delay(delay)
        #display update
        display.fill((125,125,125))
        #title
        choose.draw()
        three.draw()
        five.draw()
        eight.draw()
        pygame.display.update()
        #event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    in_menu = False
                    run = False
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_intersect(mouse_pos, three.get_rect()):
                    size = 3
                    in_menu = False
                elif mouse_intersect(mouse_pos, five.get_rect()):
                    size = 5
                    in_menu = False
                elif mouse_intersect(mouse_pos, eight.get_rect()):
                    size = 8
                    in_menu = False

    refernceBlock = generate(size,display, True)
    preping = True
    start_ticks = pygame.time.get_ticks()
    while preping and run:
        pygame.time.delay(delay)
        #display update
        display.fill((255,255,255))
        for i in refernceBlock:
            for l in i:
                l.draw()
        pygame.display.update()

        seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
        if seconds > 5:
            preping = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    preping = False
                    run = False
                    pygame.quit()



    blocks = generate(size,display, False)

    play = True
    while play and run:
        pygame.time.delay(delay)
        #display update
        display.fill((255,255,255))
        for i in blocks:
            for l in i:
                l.draw()

        pygame.display.update()
        #runtime event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    play = False
                    run = False
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for l in blocks:
                    for g in l:
                        if mouse_intersect(mouse_pos, g.get_rect()):
                            g.click()

        complete = True
        for x in range(size):
            for y in range(size):
                if blocks[x][y].get_color() != refernceBlock[x][y].get_color():
                    complete = False
        if complete:
            play = False

        frame += 1

    end = True
    end_text = Text(display,"COMPLETE!", (w/3-55, h/2-100), 70)
    restart = button(display, ((w/2-90, h/2)),175,50,"Restart?",50, 0, (10, 5))
    while end and run:
        pygame.time.delay(delay)
        display.fill((125,125,125))
        end_text.draw()
        restart.draw()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    end = False
                    run = False
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if mouse_intersect(mouse_pos, restart.get_rect()):
                        end = False

pygame.quit()