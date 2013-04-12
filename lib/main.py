# -*- coding: utf-8 -*

import pygame
from pygame.locals import *
import util
from util import myprint, file_path
import pig
import entity
from myvector import MyVector
from random import randint


class MainGame(object):
    def __init__(self, screen):
        self.screen = screen



    def run(self,  mode):
        GAME_WIDTH = 420
        GAME_HEIGHT = 440
        human = pygame.image.load(file_path("walk.png")).convert_alpha()
        star_img1= pygame.image.load(file_path("star1.png")).convert_alpha()
        star_img2= pygame.image.load(file_path("star2.png")).convert_alpha()
        star_img3= pygame.image.load(file_path("star3.png")).convert_alpha()
        star_img4= pygame.image.load(file_path("star4.png")).convert_alpha()
        star_img5= pygame.image.load(file_path("star5.png")).convert_alpha()
        star_img6= pygame.image.load(file_path("star6.png")).convert_alpha()
        #star_img7= pygame.image.load(file_path("star7.png")).convert_alpha()
        paused = False

        if mode==1:
            self.scoreleft = 600
            DB_COUNT = 10
            init_pig = pig.Pig()
            clock = pygame.time.Clock()
            world = World(self.screen)
            gamespeed = 4.    
            for db in xrange(DB_COUNT):
                db = entity.Dumbbell(world)
                my_random_posi = self.my_random()
                db.location = MyVector(my_random_posi)
                world.add_entity(db)
            me = entity.Me(world, human)
            me.location = MyVector((GAME_WIDTH/2, GAME_HEIGHT/2))
            world.add_entity(me)
            while True:
                for e in pygame.event.get():
                    if e.type == QUIT:
                        return 'quit'
                    if e.type == KEYUP:
                        if e.key == K_SPACE:
                            paused = not paused
                if not paused:
                    past_second = clock.tick(30) / 1000.0
                    self.scoreleft -= 1
                    # 一定几率不断出现星星
                    if randint(1,200) == 1:
                        start_obj1 = entity.Star(world, star_img1, 1)
                        my_random_posi = self.my_random()
                        start_obj1.location = MyVector(my_random_posi)
                        world.add_entity(start_obj1)                
                    if randint(1,200) == 1:
                        start_obj3 = entity.Star(world, star_img3, 3)
                        my_random_posi = self.my_random()
                        start_obj3.location = MyVector(my_random_posi)
                        world.add_entity(start_obj3)
                    if randint(1,300) == 1:
                        start_obj6 = entity.Star(world, star_img6, 6)
                        my_random_posi = self.my_random()
                        start_obj6.location = MyVector(my_random_posi)
                        world.add_entity(start_obj6)
                    #画世界
                    world.render()
                    #世界运行
                    world.process(past_second)
                    #积分区域
                    score_area = self.screen.subsurface(460, 20, 160, 60)
                    score_area.fill((0,0,0))
                    myprint(score_area, 'LEVEL 1', (5,5), color=(255,255,255), size='enl')
                    myprint(score_area, 'To Next Level: ', (5,35), color=(255,255,255), size='dk')
                    myprint(score_area, str(self.scoreleft), (80,35), color=(255,255,255), size='dk')
                    #画猪
                    pig_area = self.screen.subsurface(460, 90, 160, 370)
                    pig_area.fill((0,0,0))
                    if world.left_20:
                        init_pig.shy = False
                        gamespeed = 4.
                        init_pig.dynamic_tra_start1 = (init_pig.dynamic_tra_start1[0]-20, init_pig.dynamic_tra_start1[1])
                        init_pig.dynamic_tra_start2 = (init_pig.dynamic_tra_start2[0]-20, init_pig.dynamic_tra_start2[1])
                        world.left_20 = False
                    if world.right_20:
                        init_pig.shy = False
                        gamespeed = 4.
                        init_pig.dynamic_tra_start1 = (init_pig.dynamic_tra_start1[0]+20, init_pig.dynamic_tra_start1[1])
                        init_pig.dynamic_tra_start2 = (init_pig.dynamic_tra_start2[0]+20, init_pig.dynamic_tra_start2[1])
                        world.right_20 = False
                    if world.left_10:
                        init_pig.shy = False
                        gamespeed = 4.
                        init_pig.dynamic_tra_start1 = (init_pig.dynamic_tra_start1[0]-10, init_pig.dynamic_tra_start1[1])
                        init_pig.dynamic_tra_start2 = (init_pig.dynamic_tra_start2[0]-10, init_pig.dynamic_tra_start2[1])
                        world.left_10 = False             
                    if world.right_10:
                        init_pig.shy = False
                        gamespeed = 4.
                        init_pig.dynamic_tra_start1 = (init_pig.dynamic_tra_start1[0]+10, init_pig.dynamic_tra_start1[1])
                        init_pig.dynamic_tra_start2 = (init_pig.dynamic_tra_start2[0]+10, init_pig.dynamic_tra_start2[1]) 
                        world.right_10 = False
                    if world.speedup: 
                        gamespeed = 20.
                        init_pig.shy = True
                        world.speedup = False
                    if world.handsweat:
                        init_pig.shy = False
                        gamespeed = 4.
                        halfneck = 262-(236-init_pig.dynamic_tra_start1[1]+26)/2
                        init_pig.dynamic_tra_start1 = (init_pig.dynamic_tra_start1[0], halfneck) 
                        init_pig.dynamic_tra_start2 = (init_pig.dynamic_tra_start2[0], halfneck)
                        init_pig.sweat = True 
                        world.handsweat = False
                    if init_pig.sweat:
                        init_pig.draw_dynamic_pig(pig_area, (80,300), 0.)
                    else:
                        init_pig.draw_dynamic_pig(pig_area, (80,300), past_second, neck_speed=gamespeed)
                    #被哑铃砸到
                    if world.ifdead:
                        #死亡讯息
                        game_area = self.screen.subsurface(20, 20, 420, 440)
                        myprint(game_area, u'你被哑铃砸到了！斜方怪非常开心！', (GAME_WIDTH/2-130, GAME_HEIGHT/2), color=(255,127,0))
                        #myprint(game_area, u'斜方肌猛涨', (GAME_WIDTH/2-130, GAME_HEIGHT/2), color=(255,127,0))
                        return 'retry1'
                    #斜方怪锻炼完成
                    if init_pig.pigtootall:
                        #斜方肌太强壮信息
                        game_area = self.screen.subsurface(20, 20, 420, 440)
                        myprint(game_area, u'怎么都让斜方怪长成这样了！', (GAME_WIDTH/2-115, GAME_HEIGHT/2-20), color=(255,127,0))
                        myprint(game_area, u'地球再也打不过斜方星了！', (GAME_WIDTH/2-105, GAME_HEIGHT/2), color=(255,127,0))
                        return 'retry1'
                    #检查是否进入下一关
                    if self.scoreleft == 0:
                        return 'next2'
                    pygame.display.update()
                else:
                    print 'paused'


        if mode == 2:
            paused = False
            self.scoreleft = 1000
            DB_COUNT = 10
            init_pig = pig.Pig()
            clock = pygame.time.Clock()
            world = World(self.screen)
            gamespeed = 6.    
            for db in xrange(DB_COUNT):
                db = entity.Dumbbell(world)
                my_random_posi = self.my_random()
                db.location = MyVector(my_random_posi)
                world.add_entity(db)
            me = entity.Me(world, human)
            me.location = MyVector((GAME_WIDTH/2, GAME_HEIGHT/2))
            world.add_entity(me)
            while True:
                for e in pygame.event.get():
                    if e.type == QUIT:
                        return 'quit'
                    if e.type == KEYUP:
                        if e.key == K_SPACE:
                            paused = not paused
                if not paused:
                    past_second = clock.tick(30) / 1000.0
                    self.scoreleft -= 1
                    # 一定几率不断出现星星
                    if randint(1,400) == 1:
                        start_obj1 = entity.Star(world, star_img1, 1)
                        my_random_posi = self.my_random()
                        start_obj1.location = MyVector(my_random_posi)
                        world.add_entity(start_obj1)                
                    if randint(1,200) == 1:
                        start_obj3 = entity.Star(world, star_img3, 3)
                        my_random_posi = self.my_random()
                        start_obj3.location = MyVector(my_random_posi)
                        world.add_entity(start_obj3)
                    if randint(1,400) == 1:
                        start_obj2 = entity.Star(world, star_img2, 2)
                        my_random_posi = self.my_random()
                        start_obj2.location = MyVector(my_random_posi)
                        world.add_entity(start_obj2) 
                    if randint(1,200) == 1:
                        start_obj4 = entity.Star(world, star_img4, 4)
                        my_random_posi = self.my_random()
                        start_obj4.location = MyVector(my_random_posi)
                        world.add_entity(start_obj4)	
                    if randint(1,300) == 1:
                        start_obj6 = entity.Star(world, star_img6, 6)
                        my_random_posi = self.my_random()
                        start_obj6.location = MyVector(my_random_posi)
                        world.add_entity(start_obj6)
                    #画世界
                    world.render()
                    #世界运行
                    world.process(past_second)
                    #积分区域
                    score_area = self.screen.subsurface(460, 20, 160, 60)
                    score_area.fill((0,0,0))
                    myprint(score_area, u'LEVEL 2', (5,5), color=(255,255,255), size='enl')
                    myprint(score_area, 'To Next Level: ', (5,35), color=(255,255,255), size='dk')
                    myprint(score_area, str(self.scoreleft), (80,35), color=(255,255,255), size='dk')
                    #画猪
                    pig_area = self.screen.subsurface(460, 90, 160, 370)
                    pig_area.fill((0,0,0))
                    if world.left_20:
                        init_pig.shy = False
                        gamespeed = 6.
                        init_pig.dynamic_tra_start1 = (init_pig.dynamic_tra_start1[0]-20, init_pig.dynamic_tra_start1[1])
                        init_pig.dynamic_tra_start2 = (init_pig.dynamic_tra_start2[0]-20, init_pig.dynamic_tra_start2[1])
                        world.left_20 = False
                    if world.right_20:
                        init_pig.shy = False
                        gamespeed = 6.
                        init_pig.dynamic_tra_start1 = (init_pig.dynamic_tra_start1[0]+20, init_pig.dynamic_tra_start1[1])
                        init_pig.dynamic_tra_start2 = (init_pig.dynamic_tra_start2[0]+20, init_pig.dynamic_tra_start2[1])
                        world.right_20 = False
                    if world.left_10:
                        init_pig.shy = False
                        gamespeed = 6.
                        init_pig.dynamic_tra_start1 = (init_pig.dynamic_tra_start1[0]-10, init_pig.dynamic_tra_start1[1])
                        init_pig.dynamic_tra_start2 = (init_pig.dynamic_tra_start2[0]-10, init_pig.dynamic_tra_start2[1])
                        world.left_10 = False             
                    if world.right_10:
                        init_pig.shy = False
                        gamespeed = 6.
                        init_pig.dynamic_tra_start1 = (init_pig.dynamic_tra_start1[0]+10, init_pig.dynamic_tra_start1[1])
                        init_pig.dynamic_tra_start2 = (init_pig.dynamic_tra_start2[0]+10, init_pig.dynamic_tra_start2[1]) 
                        world.right_10 = False
                    if world.speedup: 
                        gamespeed = 20.
                        init_pig.shy = True
                        world.speedup = False
                    if world.handsweat:
                        init_pig.shy = False
                        gamespeed = 6.
                        halfneck = 262-(236-init_pig.dynamic_tra_start1[1]+26)/2
                        init_pig.dynamic_tra_start1 = (init_pig.dynamic_tra_start1[0], halfneck) 
                        init_pig.dynamic_tra_start2 = (init_pig.dynamic_tra_start2[0], halfneck)
                        init_pig.sweat = True 
                        world.handsweat = False
                    if init_pig.sweat:
                        init_pig.draw_dynamic_pig(pig_area, (80,300), 0.)
                    else:
                        init_pig.draw_dynamic_pig(pig_area, (80,300), past_second, neck_speed=gamespeed)
                    #被哑铃砸到
                    if world.ifdead:
                        #死亡讯息
                        game_area = self.screen.subsurface(20, 20, 420, 440)
                        myprint(game_area, u'你被哑铃砸到了！斜方怪非常开心！', (GAME_WIDTH/2-130, GAME_HEIGHT/2), color=(255,127,0))
                        #myprint(game_area, u'斜方肌猛涨', (GAME_WIDTH/2-130, GAME_HEIGHT/2), color=(255,127,0))
                        return 'retry2'
                    #斜方怪锻炼完成
                    if init_pig.pigtootall:
                        #斜方肌太强壮信息
                        game_area = self.screen.subsurface(20, 20, 420, 440)
                        myprint(game_area, u'怎么都让斜方怪长成这样了！', (GAME_WIDTH/2-115, GAME_HEIGHT/2-20), color=(255,127,0))
                        myprint(game_area, u'地球再也打不过斜方星了！', (GAME_WIDTH/2-105, GAME_HEIGHT/2), color=(255,127,0))
                        return 'retry2'
                    #检查是否进入下一关
                    if self.scoreleft == 0:
                        return 'next3'
                    pygame.display.update()
                else:
                    print 'paused'
          
        if mode == 3:
            paused = False
            self.scoreleft = 1000
            DB_COUNT = 20
            init_pig = pig.Pig()
            clock = pygame.time.Clock()
            world = World(self.screen)
            gamespeed = 10.    
            for db in xrange(DB_COUNT):
                db = entity.Dumbbell(world)
                my_random_posi = self.my_random()
                db.location = MyVector(my_random_posi)
                world.add_entity(db)
            me = entity.Me(world, human)
            me.location = MyVector((GAME_WIDTH/2, GAME_HEIGHT/2))
            world.add_entity(me)      
            while True:
                for e in pygame.event.get():
                    if e.type == QUIT:
                        return 'quit'
                    if e.type == KEYUP:
                        if e.key == K_SPACE:
                            paused = not paused
                if not paused:
                    past_second = clock.tick(30) / 1000.0
                    self.scoreleft -= 1
                    # 一定几率不断出现星星
                    if randint(1,400) == 1:
                        start_obj1 = entity.Star(world, star_img1, 1)
                        my_random_posi = self.my_random()
                        start_obj1.location = MyVector(my_random_posi)
                        world.add_entity(start_obj1)                
                    if randint(1,200) == 1:
                        start_obj3 = entity.Star(world, star_img3, 3)
                        my_random_posi = self.my_random()
                        start_obj3.location = MyVector(my_random_posi)
                        world.add_entity(start_obj3)
                    if randint(1,400) == 1:
                        start_obj2 = entity.Star(world, star_img2, 2)
                        my_random_posi = self.my_random()
                        start_obj2.location = MyVector(my_random_posi)
                        world.add_entity(start_obj2) 
                    if randint(1,200) == 1:
                        start_obj4 = entity.Star(world, star_img4, 4)
                        my_random_posi = self.my_random()
                        start_obj4.location = MyVector(my_random_posi)
                        world.add_entity(start_obj4)					
                    if randint(1,400) == 1:
                        start_obj5 = entity.Star(world, star_img5, 5)
                        my_random_posi = self.my_random()
                        start_obj5.location = MyVector(my_random_posi)
                        world.add_entity(start_obj5)
                    if randint(1,300) == 1:
                        start_obj6 = entity.Star(world, star_img6, 6)
                        my_random_posi = self.my_random()
                        start_obj6.location = MyVector(my_random_posi)
                        world.add_entity(start_obj6)
                    #画世界
                    world.render()
                    #世界运行
                    world.process(past_second)
                    #积分区域
                    score_area = self.screen.subsurface(460, 20, 160, 60)
                    score_area.fill((0,0,0))
                    myprint(score_area, u'LEVEL 3', (5,5), color=(255,255,255), size='enl')
                    myprint(score_area, 'To Next Level: ', (5,35), color=(255,255,255), size='dk')
                    myprint(score_area, str(self.scoreleft), (80,35), color=(255,255,255), size='dk')
                    #画猪
                    pig_area = self.screen.subsurface(460, 90, 160, 370)
                    pig_area.fill((0,0,0))
                    if world.left_20:
                        init_pig.shy = False
                        gamespeed = 10.
                        init_pig.dynamic_tra_start1 = (init_pig.dynamic_tra_start1[0]-20, init_pig.dynamic_tra_start1[1])
                        init_pig.dynamic_tra_start2 = (init_pig.dynamic_tra_start2[0]-20, init_pig.dynamic_tra_start2[1])
                        world.left_20 = False
                    if world.right_20:
                        init_pig.shy = False
                        gamespeed = 10.
                        init_pig.dynamic_tra_start1 = (init_pig.dynamic_tra_start1[0]+20, init_pig.dynamic_tra_start1[1])
                        init_pig.dynamic_tra_start2 = (init_pig.dynamic_tra_start2[0]+20, init_pig.dynamic_tra_start2[1])
                        world.right_20 = False
                    if world.left_10:
                        init_pig.shy = False
                        gamespeed = 10.
                        init_pig.dynamic_tra_start1 = (init_pig.dynamic_tra_start1[0]-10, init_pig.dynamic_tra_start1[1])
                        init_pig.dynamic_tra_start2 = (init_pig.dynamic_tra_start2[0]-10, init_pig.dynamic_tra_start2[1])
                        world.left_10 = False             
                    if world.right_10:
                        init_pig.shy = False
                        gamespeed = 10.
                        init_pig.dynamic_tra_start1 = (init_pig.dynamic_tra_start1[0]+10, init_pig.dynamic_tra_start1[1])
                        init_pig.dynamic_tra_start2 = (init_pig.dynamic_tra_start2[0]+10, init_pig.dynamic_tra_start2[1]) 
                        world.right_10 = False
                    if world.speedup: 
                        gamespeed = 20.
                        init_pig.shy = True
                        world.speedup = False
                    if world.handsweat:
                        init_pig.shy = False
                        gamespeed = 10.
                        halfneck = 262-(236-init_pig.dynamic_tra_start1[1]+26)/2
                        init_pig.dynamic_tra_start1 = (init_pig.dynamic_tra_start1[0], halfneck) 
                        init_pig.dynamic_tra_start2 = (init_pig.dynamic_tra_start2[0], halfneck)
                        init_pig.sweat = True 
                        world.handsweat = False
                    if init_pig.sweat:
                        init_pig.draw_dynamic_pig(pig_area, (80,300), 0.)
                    else:
                        init_pig.draw_dynamic_pig(pig_area, (80,300), past_second, neck_speed=gamespeed)
                    #被哑铃砸到
                    if world.ifdead:
                        #死亡讯息
                        game_area = self.screen.subsurface(20, 20, 420, 440)
                        myprint(game_area, u'你被哑铃砸到了！斜方怪非常开心！', (GAME_WIDTH/2-130, GAME_HEIGHT/2), color=(255,127,0))
                        #myprint(game_area, u'斜方肌猛涨', (GAME_WIDTH/2-130, GAME_HEIGHT/2), color=(255,127,0))
                        return 'retry3'
                    #斜方怪锻炼完成
                    if init_pig.pigtootall:
                        #斜方肌太强壮信息
                        game_area = self.screen.subsurface(20, 20, 420, 440)
                        myprint(game_area, u'怎么都让斜方怪长成这样了！', (GAME_WIDTH/2-115, GAME_HEIGHT/2-20), color=(255,127,0))
                        myprint(game_area, u'地球再也打不过斜方星了！', (GAME_WIDTH/2-105, GAME_HEIGHT/2), color=(255,127,0))
                        return 'retry3'
                    #检查是否进入下一关
                    if self.scoreleft == 0:
                        return 'next4'
                    pygame.display.update()
                else:
                    print 'paused'

    def my_random(self):
        GAME_WIDTH = 420
        GAME_HEIGHT = 440
        ran_boolean = randint(1,2)
        if ran_boolean == 1:
            ran_x = randint(10, GAME_WIDTH/2-50)
            ran_y = randint(5, GAME_HEIGHT/2-50)
        elif ran_boolean == 2:
            ran_x = randint(GAME_WIDTH/2+50, GAME_WIDTH-10)
            ran_y = randint(GAME_HEIGHT/2+50, GAME_HEIGHT-5)
        return (ran_x, ran_y)

class World(object):
    def __init__(self, screen):
        self.screen = screen
        self.ifdead = False
        self.entities = {} # Store all the entities
        self.entity_id = 0 # Last entity id assigned
        orig_bac = pygame.image.load(file_path("background.jpg")).convert()
        self.background = pygame.transform.scale(orig_bac, (640, 480))  
        self.left_20 = False
        self.left_10 = False
        self.right_20 = False
        self.right_10 = False
        self.speedup = False
        self.handsweat = False   
        #self.gym_background = pygame.image.load(file_path("gym.jpg")).convert()
        
    
    def add_entity(self, entity):
        # 增加一个新的实体
        self.entities[self.entity_id] = entity
        entity.id = self.entity_id
        self.entity_id += 1
        print self.entity_id

    def remove_entity(self, entity):
        del self.entities[entity.id]

    def get_me_location(self):
        for entity in self.entities.itervalues():
            if entity.name == 'me':
                #print entity.location
                return entity.location

    def process(self, past_second):
        # 处理世界中的每一个实体
        for entity in self.entities.values():
            entity.process(past_second)

    def render(self):
        # 绘制背景和每一个实体
        self.screen.blit(self.background, (0,0))
        game_area = self.screen.subsurface(20, 20, 420, 440)
        game_area.fill((0,0,0))
        for entity in self.entities.values():
            entity.render(game_area)




def test():
    pygame.init()
    s = pygame.display.set_mode((640, 480), HWSURFACE | SRCALPHA, 32)
    util.init()
    m = MainGame(s)
    m.run(1)

#test()