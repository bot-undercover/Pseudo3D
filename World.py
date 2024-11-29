import pygame as pg


class World:
    def __init__(self, screen, file):
        self.screen, self.map = screen, eval(file)
        self.corrected_map = None

    def update_map(self):
        self.corrected_map = self.map
    def get_collisions(self):
        if self.corrected_map:
            return self.corrected_map