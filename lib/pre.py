# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from util import myprint, file_path

class Pre(object):
    """starting info. for the game"""
    counter = 0
    

    def __init__(self, surface):
        self.screen = surface
        self.original_icon = pygame.image.load(file_path("Inky.png")).convert_alpha()
        self.loading_icon = pygame.transform.scale(self.original_icon, (30, 30))
        self.angle = 0.

    def run(self):
        self.show_info_author()
        self.cleanscreen()
        pygame.display.update()
        #self.show_info_game()
        return 'pretending'

    def show_info_author(self):
        h = myprint(self.screen, u"本游戏只为测试用，非完成版。", (50,120))
        myprint(self.screen, u"游戏内的背景音乐(暂时)是Sehnsucht，存在版权也是很有可能的。", (50,125+h))
        myprint(self.screen, u"不过在天朝大家都是免费听歌的，我暂时也就不管了。", (50,130+2*h))
        myprint(self.screen, u"有一些图标非原创，但找的都属于commerical allowed", (50,135+3*h))
        myprint(self.screen, u"Copyright (c) 2013 HuangShan", (50,160+5*h), size='en')
        myprint(self.screen, u"Version Beta 1.0", (50,165+6*h), size='en')
        pygame.display.update()
        myprint(self.screen, u"PRESS ENTER TO START...", (450,400), size='en')
        pygame.display.update()
        while True:
            for e in pygame.event.get():
                if e.type == QUIT:
                    exit()
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[K_RETURN]:
                break

    def show_info_game(self):
    	self.cleanscreen()       
        h = myprint(self.screen, u"控制方向：上下左右", (230,150))
        myprint(self.screen, u"使用道具：空格", (250,160+h))
        myprint(self.screen, u"暂停：p", (275,170+2*h))
        pygame.display.update()
        pygame.time.wait(1000)
        myprint(self.screen, u"PRESS ENTER TO START...", (450,400), size='en')
        pygame.display.update()
        while True:
            for e in pygame.event.get():
                if e.type == QUIT:
                    exit()
            pressed_keys = pygame.key.get_pressed()
            #pressed_mouse = pygame.mouse.get_pressed()
            if pressed_keys[K_RETURN]:
                break

    def show_pretend_loading(self):
        clock = pygame.time.Clock()
        while True:
            past_second = clock.tick(30) / 1000.0
            for e in pygame.event.get():
                if e.type == QUIT:
                    exit()
            speed = 1200.
        
            self.cleanscreen()
            bar_length = 240
            total_time = 150
            myprint(self.screen, u"PRETEND TO BE LOADING", (148,200), size='enl',color=(255, 255, 255))
            self.angle += past_second*speed
            rotated_icon = pygame.transform.rotate(self.loading_icon, self.angle)
            w, h = rotated_icon.get_size()
            draw_posi = (170-w/2, 255-h/2)
            self.screen.blit(rotated_icon, draw_posi)
            if Pre.counter < total_time:
                #print Pre.counter
                pygame.draw.rect(self.screen, (255,255,255), (200, 250, bar_length, 10), 2)
                self.screen.fill((255, 255, 255), (200, 250, Pre.counter*bar_length/total_time, 10))
                percent_str = (str)(Pre.counter*100/total_time)+'%'
                myprint(self.screen, percent_str, (215+bar_length,248), color=(255, 255, 255),size='arial')
                Pre.counter += 1
            pygame.display.update()

            if Pre.counter >= total_time:
                break
        return 'level1'

    def cleanscreen(self):
        self.screen.fill((0,0,0))

