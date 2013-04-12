# -*- coding: utf-8 -*
 
import pygame
from pygame.locals import *
from util import myprint, file_path
import pig
from sound import play_sound

class NextLevel(object):
    def __init__(self, screen):
        self.screen = screen
        orig_bac = pygame.image.load(file_path("background.jpg")).convert()
        self.background = pygame.transform.scale(orig_bac, (640, 480)) 
    def run(self,nextlevel):
        WIDTH = 420
        HEIGHT = 440
        game_area = self.screen.subsurface(20, 20, WIDTH, HEIGHT)
        score_area = self.screen.subsurface(460, 20, 160, 60)
        pig_area = self.screen.subsurface(460, 90, 160, 370)
        if nextlevel == 1:
            while True:
                for e in pygame.event.get():
                    if e.type == QUIT:
                        return 'quit'
                    if e.type == MOUSEBUTTONUP:
                        if self.is_over(e.pos, (WIDTH/2-20, HEIGHT/2+60)) and e.button == 1:
                            play_sound('go')
                            pygame.mixer.music.play(-1)
                            return 'game1'

                self.screen.blit(self.background, (0,0))                       
                game_area.fill((0,0,0))
                score_area.fill((0,0,0))
                pig_area.fill((0,0,0))
                mouse_position = pygame.mouse.get_pos()
                myprint(game_area, u'Next Level: 1', (WIDTH/2-65, HEIGHT/2-20))
                myprint(game_area, u'还是健身菜鸟的斜方怪', (WIDTH/2-90, HEIGHT/2))
                if self.is_over(mouse_position, (WIDTH/2-20, HEIGHT/2+60)):
                    pygame.draw.rect(game_area, (255,127,0), (WIDTH/2-40, HEIGHT/2+40, 80, 30))
                    pygame.draw.rect(game_area, (255,255,255), (WIDTH/2-40, HEIGHT/2+40, 80, 30), 2)
                    myprint(game_area, u'Go', (WIDTH/2-12, HEIGHT/2+45))
                else:
                    pygame.draw.rect(game_area, (0,0,0), (WIDTH/2-40, HEIGHT/2+40, 80, 30))
                    pygame.draw.rect(game_area, (255,255,255), (WIDTH/2-40, HEIGHT/2+40, 80, 30), 2)
                    myprint(game_area, u'Go', (WIDTH/2-12, HEIGHT/2+45))
                pygame.display.update()
        if nextlevel == 2:
            while True:
                for e in pygame.event.get():
                    if e.type == QUIT:
                        return 'quit'
                    if e.type == MOUSEBUTTONUP:
                        if self.is_over(e.pos, (WIDTH/2-20, HEIGHT/2+60)) and e.button == 1:
                            play_sound('go')
                            pygame.mixer.music.play(-1)
                            return 'game2'
                game_area.fill((0,0,0))
                mouse_position = pygame.mouse.get_pos()
                myprint(game_area, u'Next Level: 2', (WIDTH/2-65, HEIGHT/2-20))
                myprint(game_area, u'斜方怪变得强大了', (WIDTH/2-70, HEIGHT/2))
                if self.is_over(mouse_position, (WIDTH/2-20, HEIGHT/2+60)):
                    pygame.draw.rect(game_area, (255,127,0), (WIDTH/2-40, HEIGHT/2+40, 80, 30))
                    pygame.draw.rect(game_area, (255,255,255), (WIDTH/2-40, HEIGHT/2+40, 80, 30), 2)
                    myprint(game_area, u'Go', (WIDTH/2-12, HEIGHT/2+45))
                else:
            	    pygame.draw.rect(game_area, (0,0,0), (WIDTH/2-40, HEIGHT/2+40, 80, 30))
            	    pygame.draw.rect(game_area, (255,255,255), (WIDTH/2-40, HEIGHT/2+40, 80, 30), 2)
                    myprint(game_area, u'Go', (WIDTH/2-12, HEIGHT/2+45))
                pygame.display.update()
        if nextlevel == 3:
            while True:
                for e in pygame.event.get():
                    if e.type == QUIT:
                        return 'quit'
                    if e.type == MOUSEBUTTONUP:
                        if self.is_over(e.pos, (WIDTH/2-20, HEIGHT/2+60)) and e.button == 1:
                            play_sound('go')
                            pygame.mixer.music.play(-1)
                            return 'game3'

                game_area.fill((0,0,0))
                mouse_position = pygame.mouse.get_pos()
                myprint(game_area, u'Next Level: 3', (WIDTH/2-65, HEIGHT/2-20))
                myprint(game_area, u'斜方怪大怒：噩梦来临', (WIDTH/2-85, HEIGHT/2))
                if self.is_over(mouse_position, (WIDTH/2-20, HEIGHT/2+60)):
                    pygame.draw.rect(game_area, (255,127,0), (WIDTH/2-40, HEIGHT/2+40, 80, 30))
                    pygame.draw.rect(game_area, (255,255,255), (WIDTH/2-40, HEIGHT/2+40, 80, 30), 2)
                    myprint(game_area, u'Go', (WIDTH/2-12, HEIGHT/2+45))
                else:
                    pygame.draw.rect(game_area, (0,0,0), (WIDTH/2-40, HEIGHT/2+40, 80, 30))
                    pygame.draw.rect(game_area, (255,255,255), (WIDTH/2-40, HEIGHT/2+40, 80, 30), 2)
                    myprint(game_area, u'Go', (WIDTH/2-12, HEIGHT/2+45))
                pygame.display.update()
        if nextlevel == 4:
            pygame.mixer.music.stop()
            while True:
                for e in pygame.event.get():
                    if e.type == QUIT:
                        return 'quit'
                game_area.fill((0,0,0))
                mouse_position = pygame.mouse.get_pos()
                myprint(game_area, u'斜方怪练不出满意的斜方肌，抑郁而终', (WIDTH/2-155, HEIGHT/2-20))
                myprint(game_area, u'CONGRATULATIONS', (WIDTH/2-105, HEIGHT/2))
                pygame.display.update()


    def is_over(self, point, item_topleft):
        if item_topleft[0] < point[0] < (item_topleft[0] + 80):
            if item_topleft[1] < point[1] < (item_topleft[1] + 30):
                return True
        else:
            return False

        