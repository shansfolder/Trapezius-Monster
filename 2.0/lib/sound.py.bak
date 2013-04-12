import pygame
import util

_SOUNDS = {}
_MUSIC = {}
def load():
    _SOUNDS['go'] = pygame.mixer.Sound(util.file_path('go.ogg'))
    _SOUNDS['menu'] = pygame.mixer.Sound(util.file_path('menu.ogg'))
    pygame.mixer.music.load(util.file_path('sehnsucht.ogg'))

def play_sound(name):
    try:
        _SOUNDS[name].play()
    except KeyError:
        raise