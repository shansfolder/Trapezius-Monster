#!/usr/bin/env python
# -*- coding: utf-8 -*
 
import sys, os
 
#sys.setdefaultencoding('utf-8')
try:
    libdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib')
    sys.path.insert(0, libdir)
except:
    # in py2exe, __file__ is gone...
    pass
 
import game
game.run()