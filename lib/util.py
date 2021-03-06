# -*- coding: utf-8 -*-

import os, sys
import pygame

if hasattr(sys, 'frozen'):
    _ME_PATH = sys._MEIPASS
    DATA_PATH = os.path.normpath(os.path.join(_ME_PATH, 'data'))
else:
    _ME_PATH = os.path.abspath(os.path.dirname(__file__))
    DATA_PATH = os.path.normpath(os.path.join(_ME_PATH, '..', 'data'))

_FONTS = {}
# 血红色 (177, 17, 22)

def file_path(filename=None):
    """ give a file(img, sound, font...) name, return full path name. """
    if filename is None:
        raise ValueError, 'must supply a filename'


    file_path = os.path.join(_ME_PATH, filename)
    #print 'Will read', file_path

    if os.path.abspath(file_path):
        return file_path
    else:
        raise ValueError, "Cant open file `%s'." % file_path

def myprint(screen, string, pos, size='c1s', color=(255, 255, 255)):
    """ Print text to game display
        screen: display screen
        string: the text want to display
        pos:    the position of text
        size:   size of text(can be l, m, s)
        color:  the color of text
    """
    fs = _FONTS[size].render(string, True, color)
    screen.blit(fs, pos)
    #w = fs.get_width()
    h = fs.get_height()
    return h

def init():
    """ init some pygame objects, such as font """
    #print "DATA PATH is: ", DATA_PATH
    global _FONTS
    _FONTS['c1l'] = pygame.font.Font(file_path('ch1.ttf'), 48)
    _FONTS['c1m'] = pygame.font.Font(file_path('ch1.ttf'), 24)
    _FONTS['c1s'] = pygame.font.Font(file_path('ch1.ttf'), 18)
    _FONTS['c1ss'] = pygame.font.Font(file_path('ch1.ttf'), 12)
    _FONTS['en'] = pygame.font.Font(file_path('en2.ttf'), 12)
    _FONTS['enl'] = pygame.font.Font(file_path('en2.ttf'), 24)
    _FONTS['arial'] = pygame.font.Font(file_path('en1.ttf'), 12)
    _FONTS['dk'] = pygame.font.Font(file_path('DK.ttf'), 16)
