import pygame as pg
from World import World
from Player import Player
from Render import ray
import GameConf
from math import *


def show_Player():
    playerXY = player.getPos
    # pg.draw.line(screen, pg.Color('red'), playerXY,
    #              [playerXY[0] + 25 * cos(player.getAngle),
    #               playerXY[1] + 25 * sin(player.getAngle)])
    # pg.draw.line(screen, pg.Color('red'), playerXY, ray(pos, player.getAngle, map))
    # pg.draw.circle(screen, pg.Color('green'), playerXY, GameConf.World["multiplier"] * 0.25)


pg.init()
screen = pg.display.set_mode((GameConf.WIDTH, GameConf.HEIGHT))
clock = pg.time.Clock()
world = World(screen, open("Levels/Adventure0/main.map", "r").read())
player = Player((int(GameConf.WIDTH / 2), int(GameConf.HEIGHT / 2)))
while True:
    [exit() for i in pg.event.get() if i.type == pg.QUIT]
    screen.fill("black")
    world.update_map()
    pg.display.set_caption(f" Player POS: {list(map(int, player.getPos))} Player ROT: {str(round((player.getAngle * 180 / pi) % 360, 0))[:-2].rjust(3, '0')} FPS: {round(clock.get_fps(), 2)}")
    player.moved()
    pos, pl_angle = player.getPos, player.getAngle
    game_map = world.get_collisions()
    count = 0
    half_height = GameConf.HEIGHT // 2
    size = 10
    for angle in range(-GameConf.FOV // 2, +GameConf.FOV // 2):
        for a in range(1):
            angle += a
            try:
                d = 1 / ray(pos, pl_angle + asin(angle * pi / 180), game_map, True) * 10000
            except:
                d = half_height
            # pg.draw.line(screen, pg.Color('white'), [count, half_height - d], [count, half_height + d])
            try:
                pg.draw.polygon(screen, (int(230 * int(d) / 300), int(250 * int(d) / 300), int(250 * int(d) / 300)),
                                [[count, half_height - d], [count, half_height + d], [count + size, half_height + d],
                                 [count + size, half_height - d]])
            except:
                pg.draw.polygon(screen, (255, 255, 255),
                                [[count, half_height - d], [count, half_height + d], [count + size, half_height + d],
                                 [count + size, half_height - d]])
            # pg.draw.line(screen, pg.Color('white'), pos, ray(pos, pl_angle + asin(angle * pi / 180), map))
            count += size
    # show_Player()

    pg.display.update()
    clock.tick(GameConf.FPS)
