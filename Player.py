from operator import invert
from math import *

import pygame as pg
from GameConf import *
class Player:
    def __init__(self, pos, angle=0, multi=1):
        self.x, self.y, self.angle, self.multi = *pos, angle, multi
        self.mouse_tracking = True
        self.orig_pos = [WIDTH / 2, HEIGHT / 2]
        self.last = None
    @property
    def getPos(self):
        return self.x, self.y

    @property
    def getAngle(self):
        return self.angle

    def moved(self):
        sin_a, cos_a = sin(self.angle), cos(self.angle)
        if self.mouse_tracking:
            pg.mouse.set_visible(False)
        else:
            pg.mouse.set_visible(True)
        button = pg.key.get_pressed()
        if button[pg.K_ESCAPE]:
            self.mouse_tracking = not self.mouse_tracking
        if button[pg.K_w]:
            self.x += self.multi * cos_a
            self.y += self.multi * sin_a
        if button[pg.K_s]:
            self.x -= self.multi * cos_a
            self.y -= self.multi * sin_a
        if button[pg.K_a]:
            self.x += self.multi * sin_a
            self.y -= self.multi * cos_a
        if button[pg.K_d]:
            self.x -= self.multi * sin_a
            self.y += self.multi * cos_a
        pos = pg.mouse.get_pos()

        if pos != self.orig_pos and self.mouse_tracking:
            if pos != self.last:
                self.angle -= (self.orig_pos[0] - pos[0]) / WIDTH * 1.5
            self.last = pos
            pg.mouse.set_pos(self.orig_pos)
