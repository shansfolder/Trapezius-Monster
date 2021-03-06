# -*- coding: utf-8 -*

import pygame
from pygame.locals import *
from util import myprint, file_path
import pig
import util
from myvector import MyVector
from sound import play_sound

class Level(object):
    def __init__(self, screen):
        self.screen = screen
        orig_bac = pygame.image.load(file_path("background.jpg")).convert()
        self.background = pygame.transform.scale(orig_bac, (640, 480))
        self.show_star = False
        # 1是最初的神展开介绍画面 2是操作方法 3，4，5，6道具介绍
        self.show_info = 1
        self.angle = 0.

    def run(self, info_mode):

        if info_mode==1:
            
            mypig = pig.Pig()
            star_pig = pig.Pig((140,220))
            clock = pygame.time.Clock()
            grey = (139, 129, 76)

            while True:
                
                for e in pygame.event.get():
                    if e.type == QUIT:
                        return 'quit'
                    if e.type == MOUSEBUTTONUP:
                        # print 'up'
                        if self.is_over(e.pos, (120,395)) and e.button == 1:
                            play_sound('menu')
                            self.show_star = not self.show_star
                        if self.is_over(e.pos, (550,395)) and e.button == 1:
                            play_sound('go')
                            return 'next1'
                        if self.is_over(e.pos, (40,395)) and e.button == 1:
                            play_sound('menu')
                            if self.show_info == 2:
                                self.show_info = 1
                            else:
                                self.show_info = 2
                        if self.is_over(e.pos, (180,399), 32) and e.button == 1:
                            play_sound('menu')
                            self.show_info = 3     #左加20
                        if self.is_over(e.pos, (220,403), 26) and e.button == 1:
                            play_sound('menu')
                            self.show_info = 4     #右加20
                        if self.is_over(e.pos, (250,403), 26) and e.button == 1:
                            play_sound('menu')
                            self.show_info = 5     #左加10
                        if self.is_over(e.pos, (280,399), 32) and e.button == 1:
                            play_sound('menu')
                            self.show_info = 6     #右加10
                        if self.is_over(e.pos, (320,400), 32) and e.button == 1:
                            play_sound('menu')
                            self.show_info = 7     #表扬 speed*2
                        if self.is_over(e.pos, (360,403), 26) and e.button == 1:
                            play_sound('menu')
                            self.show_info = 8     #手汗
                            star_pig.sweat = True
                        
                        # if star
                        # show info = 3,4,5,6,7,


                past_second = clock.tick(30) / 1000.0
                mouse_position = pygame.mouse.get_pos()

                self.screen.blit(self.background, (0,0))
                


                pig_area = self.screen.subsurface(20, 20, 290, 340)
                pig_area.fill((0,0,0))

                if self.show_info == 2:
                    star_pig.shy = False
                    star_pig.draw_dynamic_pig(pig_area, (140,220), past_second)
                    if star_pig.info_area_restart:
                        star_pig.dynamic_tra_start1 = (133, 156)
                        star_pig.dynamic_tra_start2 = (147, 156)
                        star_pig.info_area_restart = False
                elif self.show_info == 3:
                    star_pig.shy = False
                    if star_pig.dynamic_tra_start1[0] != 113:
                        star_pig.dynamic_tra_start1 = (133-20, 156)
                        star_pig.dynamic_tra_start2 = (147-20, 156)
                    star_pig.draw_dynamic_pig(pig_area, (140,220), past_second)
                    if star_pig.info_area_restart:
                        star_pig.dynamic_tra_start1 = (133, 156)
                        star_pig.dynamic_tra_start2 = (147, 156)
                        star_pig.info_area_restart = False
                elif self.show_info == 4:
                    star_pig.shy = False
                    if star_pig.dynamic_tra_start1[0] != 153:
                        star_pig.dynamic_tra_start1 = (133+20, 156)
                        star_pig.dynamic_tra_start2 = (147+20, 156)
                    star_pig.draw_dynamic_pig(pig_area, (140,220), past_second)
                    if star_pig.info_area_restart:
                        star_pig.dynamic_tra_start1 = (133, 156)
                        star_pig.dynamic_tra_start2 = (147, 156)
                        star_pig.info_area_restart = False
                elif self.show_info == 5:
                    star_pig.shy = False
                    if star_pig.dynamic_tra_start1[0] != 123:
                        star_pig.dynamic_tra_start1 = (133-10, 156)
                        star_pig.dynamic_tra_start2 = (147-10, 156)
                    star_pig.draw_dynamic_pig(pig_area, (140,220), past_second)
                    if star_pig.info_area_restart:
                        star_pig.dynamic_tra_start1 = (133, 156)
                        star_pig.dynamic_tra_start2 = (147, 156)
                        star_pig.info_area_restart = False
                elif self.show_info == 6:
                    star_pig.shy = False
                    if star_pig.dynamic_tra_start1[0] != 143:
                        star_pig.dynamic_tra_start1 = (133+10, 156)
                        star_pig.dynamic_tra_start2 = (147+10, 156)
                    star_pig.draw_dynamic_pig(pig_area, (140,220), past_second)
                    if star_pig.info_area_restart:
                        star_pig.dynamic_tra_start1 = (133, 156)
                        star_pig.dynamic_tra_start2 = (147, 156)
                        star_pig.info_area_restart = False
                elif self.show_info == 7:
                    star_pig.shy = True
                    star_pig.draw_dynamic_pig(pig_area, (140,220), past_second, hand_speed = 1000., neck_speed = 60.)
                    if star_pig.info_area_restart:
                        star_pig.dynamic_tra_start1 = (133, 156)
                        star_pig.dynamic_tra_start2 = (147, 156)
                        star_pig.info_area_restart = False
                elif self.show_info == 8:
                    star_pig.shy = False
                    if star_pig.dynamic_tra_start1[1] < 100:
                        star_pig.sweat = True
                        halfneck = 182-(156-star_pig.dynamic_tra_start1[1]+26)/2
                        star_pig.dynamic_tra_start1 = (133, halfneck)
                        star_pig.dynamic_tra_start2 = (147, halfneck)
                    if star_pig.sweat:
                        star_pig.draw_dynamic_pig(pig_area, (140,220), 0.)
                    else:
                        star_pig.draw_dynamic_pig(pig_area, (140,220), past_second)
                    if star_pig.info_area_restart:
                        star_pig.dynamic_tra_start1 = (133, 156)
                        star_pig.dynamic_tra_start2 = (147, 156)
                        star_pig.info_area_restart = False
                else:
                    mypig.drawpig(pig_area, (140,220), past_second)
                    self.draw_arrow(pig_area, (190,205), (220,220))
                    myprint(pig_area, u'左手举不动了', (200,225), size='c1ss')
                    myprint(pig_area, u'斜方怪还在坚持！', (190,240), size='c1ss')
                    self.draw_arrow(pig_area, (170,165), (202,150))
                    myprint(pig_area, u'斜方怪拥有', (202,130), size='c1ss')
                    myprint(pig_area, u'傲人的斜方肌', (208,145), size='c1ss')
                    self.draw_arrow(pig_area, (110,215), (80, 220))
                    myprint(pig_area, u'只用粉色肚兜', (10,225), size='c1ss')
                    myprint(pig_area, u'是他的原则', (15,240), size='c1ss')




                info_area = self.screen.subsurface(330, 20, 290, 340)
                info_area.fill((0,0,0))              
                if self.show_info == 1:
                    myprint(info_area, u'“一二一二,唔噢噢哦～～”', (10, 10), color=(255,127,0))
                    myprint(info_area, u'!!这里原本是猪哥的房间...', (10, 40))
                    myprint(info_area, u'...怎么变成了一头怪兽！等等，最', (10, 60))
                    myprint(info_area, u'近猪哥整天举哑铃，难，难道说！', (10, 80))
                    myprint(info_area, u'“唔噢噢哦～愚蠢的人类。我是沉', (10, 110), color=(255,127,0))
                    myprint(info_area, u'睡了很久的斜方怪。这个人对于斜', (10, 130), color=(255,127,0))
                    myprint(info_area, u'方肌的执着唤醒了我。他的意识已', (10, 150), color=(255,127,0))
                    myprint(info_area, u'经被我吞噬。从此这副身体由我来', (10, 170), color=(255,127,0))
                    myprint(info_area, u'控制。我会锻炼出更强壮的斜方肌', (10, 190), color=(255,127,0))
                    myprint(info_area, u'不久的将来，地球将会被我们斜方', (10, 210), color=(255,127,0))
                    myprint(info_area, u'星彻底占领！唔噢噢哦～～', (10, 230), color=(255,127,0))
                    myprint(info_area, u'要抓紧练起来了！一二一二......”', (10, 250), color=(255,127,0))
                    myprint(info_area, u'...我是认真想的设定。总之猪哥，', (10, 280))
                    myprint(info_area, u'我不会让你白白牺牲的。地球就', (10, 300))
                    myprint(info_area, u'交给我来保护吧！', (10, 320))
                elif self.show_info == 2:
                    myprint(info_area, u'随着时间，斜方肌会越来越长。', (10, 40))
                    myprint(info_area, u'你要躲避斜方怪的哑铃攻击，同时', (10, 60))
                    myprint(info_area, u'不断寻找星星，防止斜方怪锻炼出', (10, 80))
                    myprint(info_area, u'自豪的斜方肌。', (10, 100))
                    myprint(info_area, u'移动：上下左右', (10, 130), color=(255,127,0))
                    myprint(info_area, u'暂停：空格', (10, 150),color=(255,127,0))
                    myprint(info_area, u'星星对斜方肌的影响：', (10, 180))
                    myprint(info_area, u'向左长', (10, 200))
                    self.drawitem(info_area, 'star1.png', (100,201), angle=-1, s=True)
                    self.drawitem(info_area, 'star3.png', (120,201), angle=-1, s=True)
                    myprint(info_area, u'向右长', (10, 220))
                    self.drawitem(info_area, 'star2.png', (100,221), angle=-1, s=True)
                    self.drawitem(info_area, 'star4.png', (120,221), angle=-1, s=True)
                    myprint(info_area, u'加速长', (10, 240))
                    self.drawitem(info_area, 'star5.png', (100,241), angle=-1, s=True)
                    myprint(info_area, u'降低一半', (10, 260))
                    self.drawitem(info_area, 'star6.png', (100,261), angle=-1, s=True)
                    myprint(info_area, u'点击下方星星图标查看具体效果。', (10, 290))
                elif self.show_info == 3:
                    myprint(info_area, u'“斜方怪，右边的斜方肌还不行”', (10, 40))
                    myprint(info_area, u'“soga”', (10, 70), color=(255,127,0))
                    myprint(info_area, u'黄色星星效果：', (10, 120))
                    myprint(info_area, u'使右边一边的斜方肌大涨', (10, 140))
                    myprint(info_area, u'一旦一边的斜方肌大出另一边很多，', (10, 180))
                    myprint(info_area, u'斜方肌失去平衡回归原点，', (10, 200))
                    myprint(info_area, u'斜方怪就得重新练起拉。', (10, 220))
                elif self.show_info == 4:
                    myprint(info_area, u'“斜方怪，左边的斜方肌搞起”', (10, 40))
                    myprint(info_area, u'“专攻左边！”', (10, 70), color=(255,127,0))
                    myprint(info_area, u'灰色星星效果：', (10, 120))
                    myprint(info_area, u'使左边一边的斜方肌大涨', (10, 140))
                elif self.show_info == 5:
                    myprint(info_area, u'“右边还差一点点哦”', (10, 40))
                    myprint(info_area, u'“没问题！一二一二...”', (10, 70), color=(255,127,0))
                    myprint(info_area, u'绿色星星效果：', (10, 120))
                    myprint(info_area, u'使右边一边的斜方肌小涨', (10, 140))
                elif self.show_info == 6:
                    myprint(info_area, u'“太帅了斜方怪！左边再一点点...”', (10, 40))
                    myprint(info_area, u'“ok”', (10, 70), color=(255,127,0))
                    myprint(info_area, u'冰冻星星效果：', (10, 120))
                    myprint(info_area, u'使左边一边的斜方肌小涨', (10, 140))
                elif self.show_info == 7:
                    myprint(info_area, u'“斜方肌已经完美了”', (10, 40))
                    myprint(info_area, u'“还，还好。谢谢。”', (10, 70), color=(255,127,0))
                    myprint(info_area, u'没想到斜方怪竟然害羞了，反而练', (10, 100))
                    myprint(info_area, u'得更快了', (10, 120))
                    myprint(info_area, u'象棋星星效果：', (10, 160))
                    myprint(info_area, u'使斜方肌增长速度加倍，', (10, 180))
                    myprint(info_area, u'持续时间到下一个星星', (10, 200))
                elif self.show_info == 8:
                    myprint(info_area, u'“啊啊啊手汗手汗，都是手汗。”', (10, 40), color=(255,127,0))
                    myprint(info_area, u'火焰星星效果：', (10, 80))
                    myprint(info_area, u'斜方怪手汗太多抓不住哑铃。', (10, 100))
                    myprint(info_area, u'回到一半的斜方肌长度，斜方怪在', (10, 120))
                    myprint(info_area, u'原地不动等汗干。', (10, 140))







                item_area = self.screen.subsurface(20, 380, 600, 70)
                item_area.fill((0,0,0))
                if self.is_over(mouse_position, (40,395)):
                    self.drawitem(item_area, 'home2.png', (20,15))
                else:
                    self.drawitem(item_area, 'home.png', (20,15))
                myprint(item_area, u'操作介绍', (19, 5), size='c1ss')
                if self.is_over(mouse_position, (120,395)):
                    item_area.fill(grey, (100,17,48,45))

                self.drawitem(item_area, 'box48.png', (100,15))
                myprint(item_area, u'道具介绍', (99, 4), size='c1ss')

                if self.show_star:
                    speed = 600.
                    self.angle += past_second * speed
                    self.try_draw_star('star1.png', mouse_position, (180,399), 32, self.angle, item_area)
                    self.try_draw_star('star2.png', mouse_position, (220,403), 26, self.angle, item_area)
                    self.try_draw_star('star3.png', mouse_position, (250,403), 26, self.angle, item_area)
                    self.try_draw_star('star4.png', mouse_position, (280,399), 32, self.angle, item_area)
                    self.try_draw_star('star5.png', mouse_position, (320,400), 32, self.angle, item_area)
                    self.try_draw_star('star6.png', mouse_position, (360,403), 26, self.angle, item_area)
                    #self.try_draw_star('star7.png', mouse_position, (390,400), 32, self.angle, item_area)
                else:
                    myprint(item_area, 'click to open', (200, 50), size='dk')
                    self.draw_arrow(item_area, (154, 45), (195, 55))

                if self.is_over(mouse_position, (550,395)):
                    self.drawitem(item_area, 'play2.png', (530,15))
                else:
                    self.drawitem(item_area, 'play.png', (538,23))
                myprint(item_area, u'准备好了', (529, 4), size='c1ss')



                pygame.display.update()

    def drawitem(self, screen, itemname, item_posi, angle=-1, s=False):
        if angle == -1:
            item = pygame.image.load(file_path(itemname)).convert_alpha()
            if s:
                item = pygame.transform.scale(item, (15, 15))
            screen.blit(item, item_posi)
        else:          
            ori_item = pygame.image.load(file_path(itemname)).convert_alpha()
            item = pygame.transform.rotate(ori_item, angle)
            w, h = ori_item.get_size()
            w2, h2 = item.get_size()
            draw_posi = (item_posi[0]+(w-w2)/2., item_posi[1]+(h-h2)/2.)
            screen.blit(item, draw_posi)

    def is_over(self, point, item_topleft, width=48):
        if item_topleft[0] < point[0] < (item_topleft[0] + width):
            if item_topleft[1] < point[1] < (item_topleft[1] + width):
                return True
        else:
            return False
    
    def try_draw_star(self, starname, mouse_position, draw_posi, starwidth, past_second, area):
        if self.is_over(mouse_position, draw_posi, starwidth):
            self.drawitem(area, starname, (draw_posi[0]-20, draw_posi[1]-380), self.angle)
        else:
            self.drawitem(area, starname, (draw_posi[0]-20, draw_posi[1]-380))
    
    def draw_arrow(self, screen, arrow_pos, end_pos):
        pygame.draw.line(screen, (255,255,255), arrow_pos, end_pos, 1)
        top_p = MyVector(arrow_pos)
        vector_arrow = MyVector((end_pos[0] - arrow_pos[0], end_pos[1] -arrow_pos[1])).normalize()
        vector1 = MyVector((-vector_arrow.y, vector_arrow.x))
        vector2 = MyVector((vector_arrow.y, -vector_arrow.x))   
        point1 = (top_p + vector_arrow*8 + vector1*3).totuple()
        point2 = (top_p + vector_arrow*8 + vector2*3).totuple()    
        pygame.draw.line(screen, (255,255,255), arrow_pos, point1, 1)
        pygame.draw.line(screen, (255,255,255), arrow_pos, point2, 1)


def test():
    pygame.init()
    s = pygame.display.set_mode((640, 480), HWSURFACE | SRCALPHA, 32)
    a = Level(s)
    util.init()
    a.run(1)


#test()
               