# -*- coding: utf-8 -*

import pygame
from pygame.locals import *
from util import myprint, file_path
from math import pi, cos, sin

class Pig(object):
    """the normal Pig for 80*120"""
    def __init__(self, center_posi = (80,300)):
        #self.orig_inky = pygame.image.load(file_path("Inky.png")).convert_alpha()
        #self.inky = pygame.transform.scale(self.orig_inky, (60, 60))
        self.control = 0.
        self.sigh = 1
        self.pigtootall = False
        self.info_area_restart = False
        self.shy = False
        self.sweat = False
        self.sweat_control = 0
        self.dynamic_tra_start1 = (center_posi[0]-7, center_posi[1]-64)
        self.dynamic_tra_start2 = (center_posi[0]+7, center_posi[1]-64)

    def drawpig (self, screen, center_posi, past_second, hand_speed = 400.):
        darkpink = (255,182,193)
        darkorange = (255,144,0)
        
        #head
        head_rec = (center_posi[0]-30, center_posi[1]-120, 60 , 60)
        pygame.draw.arc(screen, (255,255,255), head_rec, -pi/6., pi*7/6.)

        #hat
        l_1 = (head_rec[0]+15, head_rec[1])
        r_1 = (head_rec[0]+45, head_rec[1])
        l_2 = (l_1[0] + (r_1[0]-l_1[0])/4*cos(pi/3.), l_1[1] - (r_1[0]-l_1[0])/4*sin(pi/3.))
        r_2 = (r_1[0] - (r_1[0]-l_1[0])/4*cos(pi/3.), l_1[1] - (r_1[0]-l_1[0])/4*sin(pi/3.))
        l_3 = (l_2[0] + (r_1[0]-l_1[0])/4*cos(pi/3.), l_2[1] - (r_1[0]-l_1[0])/4*sin(pi/3.))
        r_3 = (r_2[0] - (r_1[0]-l_1[0])/4*cos(pi/3.), l_2[1] - (r_1[0]-l_1[0])/4*sin(pi/3.))
        l_4 = (l_3[0] + (r_1[0]-l_1[0])/4*cos(pi/3.), l_3[1] - (r_1[0]-l_1[0])/4*sin(pi/3.))
        r_4 = (r_3[0] - (r_1[0]-l_1[0])/4*cos(pi/3.), l_3[1] - (r_1[0]-l_1[0])/4*sin(pi/3.))
        top = (l_1[0] + (r_1[0]-l_1[0])/2, l_4[1] - (r_1[0]-l_1[0])/4*sin(pi/3.))
        pointlist1 = (l_1, r_1, r_2, l_2)
        pointlist2 = (l_2, r_2, r_3, l_3)
        pointlist3 = (l_3, r_3, r_4, l_4)
        pointlist4 = (l_4, r_4, top)
        pointlist5 = (l_1, r_1, top)
        pygame.draw.polygon(screen, darkorange, pointlist1)
        pygame.draw.polygon(screen, (255,255,255), pointlist2)
        pygame.draw.polygon(screen, darkorange, pointlist3)
        pygame.draw.polygon(screen, (255,255,255), pointlist4)
        #pygame.draw.polygon(screen, (255,255,255), pointlist5, 2)

        #hat ball line
        hatball_rec_low = (top[0]-20, top[1], 40, 20)
        hatball_rec_high = (top[0]-30, top[1], 60, 20)
        
        #hat ball
        hat_ball_low = (int(hatball_rec_low[0]+42), int(hatball_rec_low[1]+15))
        hat_ball_high = (int(hatball_rec_high[0]+62), int(hatball_rec_high[1]+15))

        #触须
        chux_x = center_posi[0] - (30 * cos(pi/6.)) 
        step = 30 * cos(pi/6.) * 2 / 3
        cx_posi = (chux_x, head_rec[1]+30)
        cx_posi2 = (cx_posi[0]+ step, cx_posi[1])
        cx_posi3 = (cx_posi2[0]+ step, cx_posi[1])
        self.draw_chuxu(screen, cx_posi)
        self.draw_chuxu(screen, cx_posi2)
        self.draw_chuxu(screen, cx_posi3)
        
        #eye
        pygame.draw.circle(screen, (255,255,255), (head_rec[0]+18, head_rec[1]+25), 9)
        pygame.draw.circle(screen, (255,255,255), (head_rec[0]+42, head_rec[1]+25), 9)

        #neck
        #neck_position_start1 = (center_posi[0]-5, center_posi[1]-60)
        #neck_position_start2 = (center_posi[0]+5, center_posi[1]-60)
        #neck_position_end1 = (center_posi[0]-5, center_posi[1]-40)
        #neck_position_end2 = (center_posi[0]+5, center_posi[1]-40)
        #pygame.draw.line(screen, (255,255,254), neck_position_start1, neck_position_end1)
        #pygame.draw.line(screen, (255,255,255), neck_position_start2, neck_position_end2)
        
        #trapezius
        trapezius_position_start1 = (center_posi[0]-7, center_posi[1]-64)
        trapezius_position_start2 = (center_posi[0]+7, center_posi[1]-64)
        trapezius_position_end1 = (center_posi[0]-23, center_posi[1]-38)
        trapezius_position_end2 = (center_posi[0]+23, center_posi[1]-38)
        pygame.draw.line(screen, (255,255,255), trapezius_position_start1, trapezius_position_end1)
        pygame.draw.line(screen, (255,255,255), trapezius_position_start2, trapezius_position_end2)

        #body
        body_rec = (trapezius_position_end1[0]-8, trapezius_position_end1[1]-15, 62, 70)
        #pygame.draw.rect(screen, (255,255,255), body_rec, 2)
        pygame.draw.ellipse(screen, (255,255,255), body_rec, 2)

        #口袋（暂时取消这个设计）
        #pocket_rec = (center_posi[0]+5, center_posi[1]-15, 5, 8)
        #pygame.draw.rect(screen, (255,255,255), pocket_rec, 0)
        #pocket_arc_rec = (pocket_rec[0], pocket_rec[1]-2, pocket_rec[2], 4)
        #pocket_angle = pi
        #pygame.draw.arc(screen, (255,255,255), pocket_arc_rec, 0, pocket_angle)

        #肚兜
        pocket_rec = (body_rec[0]+13, body_rec[1]+25, 36, 30)
        pygame.draw.ellipse(screen, darkpink, pocket_rec, 2)
        pocket_start = (pocket_rec[0], pocket_rec[1]+15)
        pocket_end = (pocket_rec[0]+36, pocket_rec[1]+15)
        pygame.draw.line(screen, (255,182,193), pocket_start, pocket_end, 2)
        fill_rec = (body_rec[0]+13, body_rec[1]+25, 36, 15)
        screen.fill((0,0,0), fill_rec)

        #hand
        hand_left_p1_low = (trapezius_position_end1[0], trapezius_position_end1[1]+15)
        hand_left_p2_low = (hand_left_p1_low[0]-10, hand_left_p1_low[1]+1)
        hand_left_p3_low = (hand_left_p2_low[0]-1, hand_left_p2_low[1]-13)

        hand_left_p1_high = (trapezius_position_end1[0], trapezius_position_end1[1]+15)
        hand_left_p2_high = (hand_left_p1_high[0]-11, hand_left_p1_high[1]-11)
        hand_left_p3_high = (hand_left_p2_high[0]-1, hand_left_p2_high[1]-17)

        hand_right_p1_low = (trapezius_position_end2[0], trapezius_position_end2[1]+15)
        hand_right_p2_low = (hand_right_p1_low[0]+5, hand_right_p1_low[1]+10)
        hand_right_p3_low = (hand_right_p2_low[0]+3, hand_right_p2_low[1]-10)

        hand_right_p1_high = (trapezius_position_end2[0], trapezius_position_end2[1]+15)
        hand_right_p2_high = (hand_right_p1_high[0]+10, hand_right_p1_high[1]+1)
        hand_right_p3_high = (hand_right_p2_high[0]+12, hand_right_p2_high[1]-10)
        
        #control hand position with time
        self.control += past_second * hand_speed * self.sigh
        #print self.control
        if self.control < 0. :  #low
            self.control = 0
            self.sigh = -self.sigh
            lefthand_pointlist = (hand_left_p1_low, hand_left_p2_low, hand_left_p3_low)
            righthand_pointlist = (hand_right_p1_low, hand_right_p2_low, hand_right_p3_low)
            #eyeball_low
            #pygame.draw.circle(screen, (0,0,255), (head_rec[0]+19, head_rec[1]+26), 4)
            #pygame.draw.circle(screen, (0,0,255), (head_rec[0]+41, head_rec[1]+26), 4)
            #eyeball_high
            pygame.draw.circle(screen, (0,0,255), (head_rec[0]+22, head_rec[1]+27), 4)
            pygame.draw.circle(screen, (0,0,255), (head_rec[0]+38, head_rec[1]+27), 4)
            #hatball_line
            pygame.draw.arc(screen, (255,255,255), hatball_rec_low, 0, pi/2.)
            #hatball
            pygame.draw.circle(screen, darkorange, hat_ball_low, 5)
        elif (0. <= self.control < 100.):  #low
            lefthand_pointlist = (hand_left_p1_low, hand_left_p2_low, hand_left_p3_low)
            righthand_pointlist = (hand_right_p1_low, hand_right_p2_low, hand_right_p3_low)
            #eyeball_low
            #pygame.draw.circle(screen, (0,0,255), (head_rec[0]+19, head_rec[1]+26), 4)
            #pygame.draw.circle(screen, (0,0,255), (head_rec[0]+41, head_rec[1]+26), 4)
            #eyeball_high
            pygame.draw.circle(screen, (0,0,255), (head_rec[0]+22, head_rec[1]+27), 4)
            pygame.draw.circle(screen, (0,0,255), (head_rec[0]+38, head_rec[1]+27), 4)
            #hatball_line
            pygame.draw.arc(screen, (255,255,255), hatball_rec_low, 0, pi/2.)
            #hatball
            pygame.draw.circle(screen, darkorange, hat_ball_low, 5)
        elif (100. <= self.control < 200.):     #high
            lefthand_pointlist = (hand_left_p1_high, hand_left_p2_high, hand_left_p3_high)
            righthand_pointlist = (hand_right_p1_high, hand_right_p2_high, hand_right_p3_high)
            #eyeball
            pygame.draw.circle(screen, (0,0,255), (head_rec[0]+22, head_rec[1]+27), 4)
            pygame.draw.circle(screen, (0,0,255), (head_rec[0]+38, head_rec[1]+27), 4)
            #hatball_line
            pygame.draw.arc(screen, (255,255,255), hatball_rec_high, 0, pi/2.)
            #hatball
            pygame.draw.circle(screen, darkorange, hat_ball_high, 5)
        elif self.control >= 200. :    #high
            self.control = 200.
            self.sigh = -self.sigh
            lefthand_pointlist = (hand_left_p1_high, hand_left_p2_high, hand_left_p3_high)
            righthand_pointlist = (hand_right_p1_high, hand_right_p2_high, hand_right_p3_high)
            #eyeball
            pygame.draw.circle(screen, (0,0,255), (head_rec[0]+22, head_rec[1]+27), 4)
            pygame.draw.circle(screen, (0,0,255), (head_rec[0]+38, head_rec[1]+27), 4)
            #hatball_line
            pygame.draw.arc(screen, (255,255,255), hatball_rec_high, 0, pi/2.)
            #hatball
            pygame.draw.circle(screen, darkorange, hat_ball_high, 5)

        pygame.draw.lines(screen, (255,255,255), False, lefthand_pointlist)
        pygame.draw.lines(screen, (255,255,255), False, righthand_pointlist)

        #dumbbell
        self.draw_dumbbell(screen, righthand_pointlist[2])
        self.draw_dumbbell(screen, lefthand_pointlist[2])
        
        #leg
        leg_start1 = (trapezius_position_end1[0]+15, trapezius_position_end1[1]+50)
        leg_end1 = (leg_start1[0], leg_start1[1]+20)
        leg_start2 = (trapezius_position_end2[0]-15, trapezius_position_end1[1]+50)
        leg_end2 = (leg_start2[0]+1, leg_start2[1]+20)
        pygame.draw.line(screen, (255,255,255), leg_start1, leg_end1)
        pygame.draw.line(screen, (255,255,255), leg_start2, leg_end2)

        # foot
        foot_1 = (leg_end1[0]-3, leg_end1[1]+3)
        pygame.draw.line(screen, (255,255,255), leg_end1, foot_1, 3)
        foot_2 = (leg_end2[0]-3, leg_end2[1]+3)
        pygame.draw.line(screen, (255,255,255), leg_end2, foot_2, 3)


    def draw_dumbbell(self, screen, db_position):
        darkpink = (255,182,193)
        db_rec = (db_position[0]-3, db_position[1]-2, 8, 2)
        pygame.draw.rect(screen, (255,255,255), db_rec, 0)

        ball_rec1 = (db_position[0]-5, db_position[1]-4, 3, 6)
        ball_rec2 = (db_position[0]+5, db_position[1]-4, 3, 6)
        pygame.draw.ellipse(screen, (255,255,255), ball_rec1, 0)
        pygame.draw.ellipse(screen, (255,255,255), ball_rec2, 0)

    def draw_chuxu(self, screen, cx_posi):
        w = 30 * cos(pi/6.) * 2 / 3
        rect = (cx_posi[0], cx_posi[1], w, w+10)
        pygame.draw.arc(screen, (255,255,255), rect, pi, 2*pi)        

        
    def draw_dynamic_pig(self, screen, center_posi, past_second, hand_speed = 400., neck_speed = 25.):
        darkpink = (255,182,193)
        darkorange = (255,144,0)
        shypink = (238,169,184)
        #print self.dynamic_tra_start1[1]
        #trapezius
        self.dynamic_tra_start1 = (self.dynamic_tra_start1[0], self.dynamic_tra_start1[1]-past_second*neck_speed)
        self.dynamic_tra_start2 = (self.dynamic_tra_start2[0], self.dynamic_tra_start1[1]-past_second*neck_speed)

        trapezius_position_start1 = self.dynamic_tra_start1
        trapezius_position_start2 = self.dynamic_tra_start2
        trapezius_position_end1 = (center_posi[0]-23, center_posi[1]-38)
        trapezius_position_end2 = (center_posi[0]+23, center_posi[1]-38)
        pygame.draw.line(screen, (255,255,255), trapezius_position_start1, trapezius_position_end1)
        pygame.draw.line(screen, (255,255,255), trapezius_position_start2, trapezius_position_end2)

        #head
        head_rec = (trapezius_position_start1[0]-23, trapezius_position_start1[1]-56, 60 , 60)
        pygame.draw.arc(screen, (255,255,255), head_rec, -pi/6., pi*7/6.)

        #触须
        chux_x = self.dynamic_tra_start1[0] + 7 - (30 * cos(pi/6.)) 
        step = 30 * cos(pi/6.) * 2 / 3
        cx_posi = (chux_x, head_rec[1]+30)
        cx_posi2 = (cx_posi[0]+ step, cx_posi[1])
        cx_posi3 = (cx_posi2[0]+ step, cx_posi[1])
        self.draw_chuxu(screen, cx_posi)
        self.draw_chuxu(screen, cx_posi2)
        self.draw_chuxu(screen, cx_posi3)

        #eye
        if self.sweat:
            pygame.draw.circle(screen, (255,255,255), (head_rec[0]+18, int(head_rec[1]+25)), 12)
            pygame.draw.circle(screen, (255,255,255), (head_rec[0]+42, int(head_rec[1]+25)), 12)
        else:
            pygame.draw.circle(screen, (255,255,255), (head_rec[0]+18, int(head_rec[1]+25)), 9)
            pygame.draw.circle(screen, (255,255,255), (head_rec[0]+42, int(head_rec[1]+25)), 9)

        #eyeball
        if self.sweat:
            pygame.draw.circle(screen, (0,0,255), (head_rec[0]+20, int(head_rec[1]+25)), 2)
            pygame.draw.circle(screen, (0,0,255), (head_rec[0]+40, int(head_rec[1]+25)), 2)
        else:
            pygame.draw.circle(screen, (0,0,255), (head_rec[0]+22, int(head_rec[1]+27)), 4)
            pygame.draw.circle(screen, (0,0,255), (head_rec[0]+38, int(head_rec[1]+27)), 4)

        #hat
        l_1 = (head_rec[0]+15, head_rec[1])
        r_1 = (head_rec[0]+45, head_rec[1])
        l_2 = (l_1[0] + (r_1[0]-l_1[0])/4*cos(pi/3.), l_1[1] - (r_1[0]-l_1[0])/4*sin(pi/3.))
        r_2 = (r_1[0] - (r_1[0]-l_1[0])/4*cos(pi/3.), l_1[1] - (r_1[0]-l_1[0])/4*sin(pi/3.))
        l_3 = (l_2[0] + (r_1[0]-l_1[0])/4*cos(pi/3.), l_2[1] - (r_1[0]-l_1[0])/4*sin(pi/3.))
        r_3 = (r_2[0] - (r_1[0]-l_1[0])/4*cos(pi/3.), l_2[1] - (r_1[0]-l_1[0])/4*sin(pi/3.))
        l_4 = (l_3[0] + (r_1[0]-l_1[0])/4*cos(pi/3.), l_3[1] - (r_1[0]-l_1[0])/4*sin(pi/3.))
        r_4 = (r_3[0] - (r_1[0]-l_1[0])/4*cos(pi/3.), l_3[1] - (r_1[0]-l_1[0])/4*sin(pi/3.))
        top = (l_1[0] + (r_1[0]-l_1[0])/2, l_4[1] - (r_1[0]-l_1[0])/4*sin(pi/3.))
        pointlist1 = (l_1, r_1, r_2, l_2)
        pointlist2 = (l_2, r_2, r_3, l_3)
        pointlist3 = (l_3, r_3, r_4, l_4)
        pointlist4 = (l_4, r_4, top)
        pointlist5 = (l_1, r_1, top)
        pygame.draw.polygon(screen, darkorange, pointlist1)
        pygame.draw.polygon(screen, (255,255,255), pointlist2)
        pygame.draw.polygon(screen, darkorange, pointlist3)
        pygame.draw.polygon(screen, (255,255,255), pointlist4)

        #hat ball line
        hatball_rec_low = (top[0]-20, top[1], 40, 20)
        hatball_rec_high = (top[0]-30, top[1], 60, 20)
        
        #hat ball
        hat_ball_low = (int(hatball_rec_low[0]+42), int(hatball_rec_low[1]+15))
        hat_ball_high = (int(hatball_rec_high[0]+62), int(hatball_rec_high[1]+15))

        #body
        body_rec = (center_posi[0]-31, center_posi[1]-53, 62, 70)
        #pygame.draw.rect(screen, (255,255,255), body_rec, 2)
        pygame.draw.ellipse(screen, (255,255,255), body_rec, 2)

        #口袋（暂时取消这个设计）
        #pocket_rec = (center_posi[0]+5, center_posi[1]-15, 5, 8)
        #pygame.draw.rect(screen, (255,255,255), pocket_rec, 0)
        #pocket_arc_rec = (pocket_rec[0], pocket_rec[1]-2, pocket_rec[2], 4)
        #pocket_angle = pi
        #pygame.draw.arc(screen, (255,255,255), pocket_arc_rec, 0, pocket_angle)

        #肚兜
        pocket_rec = (body_rec[0]+13, body_rec[1]+25, 36, 30)
        pygame.draw.ellipse(screen, darkpink, pocket_rec, 2)
        pocket_start = (pocket_rec[0], pocket_rec[1]+15)
        pocket_end = (pocket_rec[0]+36, pocket_rec[1]+15)
        pygame.draw.line(screen, (255,182,193), pocket_start, pocket_end, 2)
        fill_rec = (body_rec[0]+13, body_rec[1]+25, 36, 15)
        screen.fill((0,0,0), fill_rec)

        #hand
        hand_left_p1_low = (center_posi[0]-23, center_posi[1]-23)
        hand_left_p2_low = (hand_left_p1_low[0]-10, hand_left_p1_low[1]+1)
        hand_left_p3_low = (hand_left_p2_low[0]-1, hand_left_p2_low[1]-13)

        hand_left_p1_high = (center_posi[0]-23, center_posi[1]-23)
        hand_left_p2_high = (hand_left_p1_high[0]-11, hand_left_p1_high[1]-11)
        hand_left_p3_high = (hand_left_p2_high[0]-1, hand_left_p2_high[1]-17)

        hand_right_p1_low = (center_posi[0]+23, center_posi[1]-23)
        hand_right_p2_low = (hand_right_p1_low[0]+5, hand_right_p1_low[1]+10)
        hand_right_p3_low = (hand_right_p2_low[0]+3, hand_right_p2_low[1]-10)

        hand_right_p1_high = (center_posi[0]+23, center_posi[1]-23)
        hand_right_p2_high = (hand_right_p1_high[0]+10, hand_right_p1_high[1]+1)
        hand_right_p3_high = (hand_right_p2_high[0]+12, hand_right_p2_high[1]-10)
        
        #control hand position with time
        self.control += past_second * hand_speed * self.sigh
        #print self.control
        if self.control < 0. :  #low
            self.control = 0
            self.sigh = -self.sigh
            lefthand_pointlist = (hand_left_p1_low, hand_left_p2_low, hand_left_p3_low)
            righthand_pointlist = (hand_right_p1_low, hand_right_p2_low, hand_right_p3_low)
            #hatball_line
            pygame.draw.arc(screen, (255,255,255), hatball_rec_low, 0, pi/2.)
            #hatball
            pygame.draw.circle(screen, darkorange, hat_ball_low, 5)
        elif (0. <= self.control < 100.):  #low
            lefthand_pointlist = (hand_left_p1_low, hand_left_p2_low, hand_left_p3_low)
            righthand_pointlist = (hand_right_p1_low, hand_right_p2_low, hand_right_p3_low)
            #hatball_line
            pygame.draw.arc(screen, (255,255,255), hatball_rec_low, 0, pi/2.)
            #hatball
            pygame.draw.circle(screen, darkorange, hat_ball_low, 5)
        elif (100. <= self.control < 200.):     #high
            lefthand_pointlist = (hand_left_p1_high, hand_left_p2_high, hand_left_p3_high)
            righthand_pointlist = (hand_right_p1_high, hand_right_p2_high, hand_right_p3_high)
            #hatball_line
            pygame.draw.arc(screen, (255,255,255), hatball_rec_high, 0, pi/2.)
            #hatball
            pygame.draw.circle(screen, darkorange, hat_ball_high, 5)
        elif self.control >= 200. :    #high
            self.control = 200.
            self.sigh = -self.sigh
            lefthand_pointlist = (hand_left_p1_high, hand_left_p2_high, hand_left_p3_high)
            righthand_pointlist = (hand_right_p1_high, hand_right_p2_high, hand_right_p3_high)
            #hatball_line
            pygame.draw.arc(screen, (255,255,255), hatball_rec_high, 0, pi/2.)
            #hatball
            pygame.draw.circle(screen, darkorange, hat_ball_high, 5)

        pygame.draw.lines(screen, (255,255,255), False, lefthand_pointlist)
        pygame.draw.lines(screen, (255,255,255), False, righthand_pointlist)

        #dumbbell
        if self.sweat:
            self.draw_dumbbell(screen, (center_posi[0]-40, center_posi[1]+32))
            self.draw_dumbbell(screen, (center_posi[0]+35, center_posi[1]+32))
        else:
            self.draw_dumbbell(screen, righthand_pointlist[2])
            self.draw_dumbbell(screen, lefthand_pointlist[2])
        
        #leg
        leg_start1 = (center_posi[0]-8, center_posi[1]+12)
        leg_end1 = (leg_start1[0], leg_start1[1]+20)
        leg_start2 = (center_posi[0]+8, center_posi[1]+12)
        leg_end2 = (leg_start2[0]+1, leg_start2[1]+20)
        pygame.draw.line(screen, (255,255,255), leg_start1, leg_end1)
        pygame.draw.line(screen, (255,255,255), leg_start2, leg_end2)

        # foot
        foot_1 = (leg_end1[0]-3, leg_end1[1]+3)
        pygame.draw.line(screen, (255,255,255), leg_end1, foot_1, 3)
        foot_2 = (leg_end2[0]-3, leg_end2[1]+3)
        pygame.draw.line(screen, (255,255,255), leg_end2, foot_2, 3)
        
        if self.shy:
            # 脸红
            # print 'I am shy'
            red_rect1 = (head_rec[0]+9, head_rec[1]+34, 18, 10)
            red_rect2 = (head_rec[0]+33, head_rec[1]+34, 18, 10)
            pygame.draw.ellipse(screen, shypink, red_rect1)
            pygame.draw.ellipse(screen, shypink, red_rect2)

        if self.sweat:
            #print self.sweat_control
            # 手汗了之后停顿一阵子
            self.sweat_control += 1
            if self.sweat_control > 100:
                self.sweat_control = 0
                self.sweat = False

        #print top[1]
        if top[1] < 0:
            self.pigtootall = True
            self.info_area_restart = True

        if (self.dynamic_tra_start1[0] < center_posi[0]-7-35) or (self.dynamic_tra_start2[0] > center_posi[0]+7+35):
            self.dynamic_tra_start1 = (center_posi[0]-7, center_posi[1]-64)
            self.dynamic_tra_start2 = (center_posi[0]+7, center_posi[1]-64)

    