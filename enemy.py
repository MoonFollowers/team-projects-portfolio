import pygame
from run import *

class Enemy:
    def __init__(self):
        self.enemy = pygame.image.load('img/Enemy.png')
        self.enemy_size = enemy.get_size()
        self.enemy_width = enemy_size[0]
        self.enemy_height = enemy_size[1]
        self.enemy_x = margin_dashboard + (enemy_location[0] * cell) + (cell - enemy_width) / 2
        self.enemy_y = (enemy_location[1] * cell) + (cell - enemy_height) / 2
        self.enemy_button = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)

    def set_location_enemy(self, x, y):
        global enemy_location
        enemy_location = [x, y]
        enemy_x = margin_dashboard + (enemy_location[0] * cell) + (cell - enemy_width) / 2
        enemy_y = (enemy_location[1] * cell) + (cell - enemy_height) / 2

        return enemy_x, enemy_y