# -*- coding: utf-8 -*
 
import pygame
from pygame.locals import *
import util
from pre import Pre
from main import MainGame
from level import Level
from retry import Retry
from nextlevel import NextLevel
import sound

class Game(object):
    """main loop, switching from different states"""
    def __init__(self):
        self.state = 'pre'
        # init pygame
        pygame.init()
        pygame.mixer.init(44100, 16, 2, 1024*4)
        pygame.display.set_caption("MR. TRAPEZIUS ")
        

        try:
            self.screen = pygame.display.set_mode((640, 480), 
                    HWSURFACE | SRCALPHA, 32)
        except:
            self.screen = pygame.display.set_mode((640, 480), 
                    SRCALPHA, 32)
        
        try:
            pygame.display.set_icon(pygame.image.load(
                util.file_path("Inky.png")).convert_alpha())
        except:
            # some platfom do not allow change icon after shown
            pass

        # init fonts and music lists
        util.init()

        # init sub states objects
        self.pre = Pre(self.screen)
        self.go = MainGame(self.screen)
        self.level_info = Level(self.screen)
        self.re = Retry(self.screen)
        self.next = NextLevel(self.screen)
        sound.load()

    def loop(self):

        
        while self.state != 'quit':
            
            print self.state
            if self.state == 'pre':
                self.state = self.pre.run()
            elif self.state == 'pretending':
                self.state = self.pre.show_pretend_loading()
            elif self.state.startswith('level'):
                info_mode = int(self.state[-1])
                print self.state, info_mode
                self.state = self.level_info.run(info_mode)
            elif self.state.startswith('game'):
                mode = int(self.state[-1])
                self.state = self.go.run(mode)
            elif self.state.startswith('next'):
                nextlevel = int(self.state[-1])
                self.state = self.next.run(nextlevel)
            elif self.state.startswith('retry'):
                retrylevel = int(self.state[-1])
                self.state = self.re.run(retrylevel)
            # pygame.display.update()

        pygame.quit()
        exit()




def run():
	trapezius = Game()
	trapezius.loop()
