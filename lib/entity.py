# -*- coding: utf-8 -*

import pygame
from pygame.locals import *
from myvector import MyVector
from util import myprint, file_path
from random import randint

class GameEntity(object):
    def __init__(self, world, name, image=None):
        self.world = world
        self.name = name
        self.image = image
        self.location = MyVector((0, 0))
        self.destination = MyVector((0, 0))
        self.speed = 0.
        self.brain = StateMachine()
        self.id = 0

    def render(self, area):
        if self.image:
            x = self.location.x
            y = self.location.y
            w, h = self.image.get_size()
            area.blit(self.image, (x-w/2, y-h/2))

    def process(self, time_passed):
        self.brain.think()
        if self.speed > 0 and (self.location.x != self.destination.x or self.location.y != self.destination.y ):
            vec_to_destination = self.destination - self.location
            #print self.destination.x, self.destination.y, self.location.x, self.location.y
            distance_to_destination = vec_to_destination.get_magnitude()
            heading = vec_to_destination.normalize()
            travel_distance = min(distance_to_destination, time_passed * self.speed)
            self.location += heading * travel_distance 
        

class Dumbbell(GameEntity):
    """docstring for Dumbbell"""
    def __init__(self,world):
        super(Dumbbell, self).__init__(world, 'db')
        #add state
        walking_state = Dumbbell_Walking_State(self)
        hunting_state = Dumbbell_Hunting_State(self)
        dead_state = Dead_State(self)
        self.brain.add_state(walking_state)
        self.brain.add_state(hunting_state)
        self.brain.add_state(dead_state)
        self.brain.set_state('hunting')

    def render(self,area):
        db_rec = (self.location.x -4, self.location.y -1, 8, 2)
        pygame.draw.rect(area, (255,127,0), db_rec, 0)

        ball_rec1 = (self.location.x -5, self.location.y -4, 3, 6)
        ball_rec2 = (self.location.x +5, self.location.y -4, 3, 6)
        pygame.draw.ellipse(area, (255,255,255), ball_rec1, 0)
        pygame.draw.ellipse(area, (255,255,255), ball_rec2, 0)

class Me(GameEntity):
    """docstring for Me"""
    def __init__(self, world, human):
       super(Me, self).__init__(world, 'me')
       self.speed = 70.
       self.shadow = pygame.image.load(file_path("am_mask.png")).convert_alpha()
       self.shadow = pygame.transform.scale(self.shadow, (150, 150))
       self.human = human

    def process(self, past_second):
        pressed_keys = pygame.key.get_pressed()
        head_x = 0
        head_y = 0
        if pressed_keys[K_a]:
            head_x += -1
        if pressed_keys[K_d]:
            head_x += 1
        if pressed_keys[K_w]:
            head_y += -1 
        if pressed_keys[K_s]:
            head_y += 1
        if head_x != 0 or head_y != 0:
            heading = MyVector((head_x, head_y)).normalize()
            dest = heading * self.speed * past_second + self.location
            if (-10 < dest.x < 410) and (-10 < dest.y < 430):
                self.location = dest
            elif dest.x >= 410:
                self.location = MyVector((0, dest.y))
            elif dest.x <= -10:
                self.location = MyVector((402, dest.y))
            elif dest.y >= 430:
                self.location = MyVector((dest.x, 0))
            elif dest.y <= -10:
                self.location = MyVector((dest.x, 422))

    def render(self, area):
        shadow_area = (self.location.x-150/2, self.location.y-150/2)
        area.blit(self.shadow, shadow_area)
        #左上
        if (self.location.x-150/2<=0) and (self.location.y-150/2<=0):   
            area.fill((0,0,0), (0,self.location.y+150/2,self.location.x+150/2,440))
            area.fill((0,0,0), (self.location.x+150/2,0,420,440)) 
        #左下     
        if (self.location.x-150/2<=0) and (self.location.y+150/2>=440):
            area.fill((0,0,0), (0,0,420,self.location.y-150/2))         
            area.fill((0,0,0), (self.location.x+150/2,self.location.y-150/2,420,150))
        #左
        if (self.location.x-150/2<=0) and (150/2<self.location.y<440-150/2):
            area.fill((0,0,0), (0,0,420,self.location.y-150/2))
            area.fill((0,0,0), (0,self.location.y+150/2,420,400))
            area.fill((0,0,0), (self.location.x+150/2,self.location.y-150/2,420,150))
        #上
        if (self.location.y-150/2<=0) and (150/2<self.location.x<420-150/2):
            area.fill((0,0,0), (0,0,self.location.x-150/2,440))
            area.fill((0,0,0), (self.location.x+150/2,0,420,440))
            area.fill((0,0,0), (self.location.x-150/2,self.location.y+150/2,150,420))           
        #下
        if (self.location.y+150/2>=440) and (150/2<self.location.x<420-150/2):
            area.fill((0,0,0), (0,0,self.location.x-150/2,440))
            area.fill((0,0,0), (self.location.x+150/2,0,420,440))
            area.fill((0,0,0), (self.location.x-150/2,0,150,self.location.y-150/2)) 
        #右上
        if (self.location.x+150/2>=420) and (self.location.y-150/2<=0):   
            area.fill((0,0,0), (0,0,self.location.x-150/2,150))
            area.fill((0,0,0), (0, self.location.y+150/2,420,440)) 
        #右下     
        if (self.location.x+150/2>=420) and (self.location.y+150/2>=440):
            area.fill((0,0,0), (0,0,420,self.location.y-150/2))         
            area.fill((0,0,0), (0,self.location.y-150/2,self.location.x-150/2,150))
        #右
        if (self.location.x+150/2>=420) and (150/2<self.location.y<440-150/2):
            area.fill((0,0,0), (0,0,420,self.location.y-150/2))
            area.fill((0,0,0), (0,self.location.y+150/2,420,400))
            area.fill((0,0,0), (0,self.location.y-150/2,self.location.x-150/2,150))
        #中
        if (150/2<self.location.y<440-150/2) and (150/2<self.location.x<420-150/2):
            area.fill((0,0,0), (0,0,420,self.location.y-150/2))
            area.fill((0,0,0), (0,self.location.y+150/2,420,400))
            area.fill((0,0,0), (0,self.location.y-150/2,self.location.x-150/2,150)) 
            area.fill((0,0,0), (self.location.x+150/2,self.location.y-150/2,420,150))

        x = self.location.x
        y = self.location.y
        w, h = self.human.get_size()
        area.blit(self.human, (self.location.x,self.location.y))

class Star(GameEntity):
    """docstring for Star"""
    def __init__(self, world, star_image, starnumber):
        super(Star, self).__init__(world, starnumber, star_image)
        self.image = pygame.transform.scale(self.image, (20, 20))
        s_walking_state = Star_Walking_State(self)
        s_enable_state = Star_Equipped_State(self)
        self.brain.add_state(s_walking_state)
        self.brain.add_state(s_enable_state)
        self.brain.set_state('walkingstar')
        

class State(object):
    def __init__(self, name):
        self.name = name
    def do_actions(self):
        pass
    def check_conditions(self):
        pass
    def entry_actions(self):
        pass
    def exit_actions(self):
        pass

class Dumbbell_Walking_State(State):
    """docstring for Dumbbell_Walking_State"""
    def __init__(self, db):
        super(Dumbbell_Walking_State, self).__init__('walking')
        self.db = db
    def random_destination(self):
        GAME_WIDTH = 420
        GAME_HEIGHT = 440
        self.db.destination = MyVector((randint(10, GAME_WIDTH-10), randint(5, GAME_HEIGHT-5)))
    def do_actions(self):
        if randint(1, 80) == 1:
            self.random_destination()
    def entry_actions(self):
        self.db.speed = 30. + randint(-10, 10)
        self.random_destination()
    def check_conditions(self):
        if self.db.location.get_distance_to(self.db.world.get_me_location()) < 60:
            return 'hunting'
        return None

class Dumbbell_Hunting_State(State):
    """docstring for Dumbbell_Hunting_State"""
    def __init__(self, db):
        super(Dumbbell_Hunting_State, self).__init__('hunting')
        self.db = db
    def do_actions(self):
        self.db.destination = self.db.world.get_me_location()
        #print self.db.destination
    def entry_actions(self):
        self.db.speed = 20. + randint(-5, 5)
    def check_conditions(self):
        mylocation = MyVector((self.db.world.get_me_location().x+5, self.db.world.get_me_location().y+5))
        if self.db.location.get_distance_to(self.db.world.get_me_location()) > 70:
            return 'walking'
        if self.db.location.get_distance_to(mylocation) < 10:
            return 'dead'
        return None

class Dead_State(State):
    """docstring for Dead_State"""
    def __init__(self, db):
        super(Dead_State, self).__init__('dead')
        self.db = db
    def do_actions(self):
        #print 'dead'
        self.db.world.ifdead = True
    def entry_actions(self):
        pass
    def check_conditions(self):
        pass

class Star_Walking_State(State):
    """docstring for Dumbbell_Walking_State"""
    def __init__(self, st):
        super(Star_Walking_State, self).__init__('walkingstar')
        self.st = st
    def random_destination(self):
        GAME_WIDTH = 420
        GAME_HEIGHT = 440
        self.st.destination = MyVector((randint(-10, GAME_WIDTH-30), randint(-10, GAME_HEIGHT-30)))
    def do_actions(self):
        if randint(1, 80) == 1:
            self.random_destination()
    def entry_actions(self):
        self.st.speed = 30. + randint(-5, 15)
        self.random_destination()
    def check_conditions(self):
        starlocation = MyVector((self.st.location.x-5, self.st.location.y-5,))
        if starlocation.get_distance_to(self.st.world.get_me_location()) < 15:
            return 'enable_star'
        return None

class Star_Equipped_State(State):
    """docstring for Star_Equipped_State"""
    def __init__(self, st):
        super(Star_Equipped_State, self).__init__('enable_star')
        self.st = st
        #print self.st.name
    def do_actions(self):
        #print str(self.st.name)+'is enabled'
        if self.st.name == 1:
            self.st.world.left_20 = True
        elif self.st.name == 2:
            self.st.world.right_20 = True
        elif self.st.name == 3:
            self.st.world.left_10 = True
        elif self.st.name == 4:
            self.st.world.right_10 = True
        elif self.st.name == 5:
            self.st.world.speedup = True
        elif self.st.name == 6:
            self.st.world.handsweat = True   
        self.st.world.remove_entity(self.st)     
        

class StateMachine(object):
    def __init__(self):
        self.states = {}    # 存储状态
        self.active_state = None    # 当前有效状态
    def add_state(self, state):
        # 增加状态
        self.states[state.name] = state
    def think(self):
        if self.active_state is None:
            return
        # 执行有效状态的动作，并做转移检查
        #print self.active_state.name
        self.active_state.do_actions()
        new_state_name = self.active_state.check_conditions()
        if new_state_name is not None:
            self.set_state(new_state_name)
    def set_state(self, new_state_name):
        # 更改状态，执行进入/退出动作
        if self.active_state is not None:
            self.active_state.exit_actions()
        self.active_state = self.states[new_state_name]
        self.active_state.entry_actions()
        