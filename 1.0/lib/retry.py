# -*- coding: utf-8 -*
 
import pygame
from pygame.locals import *
from util import myprint

class Retry(object):
    """docstring for Retry"""
    def __init__(self, screen):
        super(Retry, self).__init__()
        self.screen = screen
    def run(self, level):
        WIDTH = 420
        HEIGHT = 440
        game_area = self.screen.subsurface(20, 20, 420, 440)
        while True:
            for e in pygame.event.get():
                if e.type == QUIT:
                    return 'quit'
                if e.type == MOUSEBUTTONUP:
                    if self.is_over(e.pos, (WIDTH/2-20, HEIGHT/2+60)) and e.button == 1:
                    	if level == 1:
                            return 'game1'
                        elif level == 2:
                            return 'game2'
                        elif level == 3:
                            return 'game3'
            
            mouse_position = pygame.mouse.get_pos()
            if self.is_over(mouse_position, (WIDTH/2-20, HEIGHT/2+60)):
                pygame.draw.rect(game_area, (255,127,0), (WIDTH/2-40, HEIGHT/2+40, 80, 30))
                pygame.draw.rect(game_area, (255,255,255), (WIDTH/2-40, HEIGHT/2+40, 80, 30), 2)
                myprint(game_area, u'Retry', (WIDTH/2-28, HEIGHT/2+45))
            else:
            	pygame.draw.rect(game_area, (0,0,0), (WIDTH/2-40, HEIGHT/2+40, 80, 30))
            	pygame.draw.rect(game_area, (255,255,255), (WIDTH/2-40, HEIGHT/2+40, 80, 30), 2)
                myprint(game_area, u'Retry', (WIDTH/2-28, HEIGHT/2+45))
            
            
            pygame.display.update()
    def is_over(self, point, item_topleft):
        if item_topleft[0] < point[0] < (item_topleft[0] + 80):
            if item_topleft[1] < point[1] < (item_topleft[1] + 30):
                return True
        else:
            return False

        