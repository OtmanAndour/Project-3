#! /usr/bin/env python
# coding: utf-8

"""Main file for the MacGyver game."""

import random
import pygame
from pygame import QUIT, KEYDOWN, K_F1, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE
from constants import *


class Map:
    
    def __init__(self, level_file):
        self.level_file = level_file
        self.generate_map()
        self.generate_items()
        self.screen = pygame.display.set_mode(LEVEL_DIMENSION)
        
    def generate_map(self):
        with open(self.level_file, 'r') as f:
            self.map = [list(x)[:-1] for x in f]
        return self.map

    def generate_items(self):
        for item in ITEMS:
            self.x_item = random.randint(0, LEVEL_WIDTH-1)
            self.y_item = random.randint(0, LEVEL_HEIGHT-1)
            while self.map[self.x_item][self.y_item] != FLOOR:
               self.x_item = random.randint(0, LEVEL_WIDTH-1)
               self.y_item = random.randint(0, LEVEL_HEIGHT-1)
            self.map[self.x_item][self.y_item] = item
        return self.map

    def show_elements(self):
        for y in range(0, LEVEL_HEIGHT):
            for x in range(0, LEVEL_WIDTH):
                self.screen.blit(PICTURES["floor"], (x*SPRITE_SIZE, y*SPRITE_SIZE)) 
                if self.map[y][x] == WALL:
                    self.screen.blit(PICTURES["wall"], (x*SPRITE_SIZE, y*SPRITE_SIZE))
                elif self.map[y][x] == FINISH:
                    self.screen.blit(PICTURES["guardian"], (x*SPRITE_SIZE, y*SPRITE_SIZE))
                elif self.map[y][x] == "NEEDLE":
                    self.screen.blit(PICTURES["needle"], (x*SPRITE_SIZE, y*SPRITE_SIZE))
                elif self.map[y][x] == "TUBE":
                    self.screen.blit(PICTURES["tube"], (x*SPRITE_SIZE, y*SPRITE_SIZE))
                elif self.map[y][x] == "ETHER":
                    self.screen.blit(PICTURES["ether"], (x*SPRITE_SIZE, y*SPRITE_SIZE))
                elif self.map[y][x] == START:
                    self.screen.blit(PICTURES["macgyver"], (x*SPRITE_SIZE, y*SPRITE_SIZE))
        pygame.display.flip()
        

class Hero:
    
    def __init__(self, x_pos, y_pos, map):
        self.x = x_pos
        self.y = y_pos
        self.items = 0
        self.map = map 

    def move(self, direction):
        if direction == "down":
            if self.y < LEVEL_HEIGHT-1:
                if self.map.map[self.y + 1][self.x] != WALL:
                    self.y += 1
        
        elif direction == "up":
            if self.y != 0:
                if self.map.map[self.y - 1][self.x] != WALL:
                    self.y -= 1
        
        elif direction == "left":
            if self.x != 0:
                if self.map.map[self.y][self.x - 1] != WALL:
                    self.x -= 1

        elif direction == "right":
            if self.x < LEVEL_WIDTH-1:
                if self.map.map[self.y][self.x + 1] != WALL:
                    self.x += 1

    def is_on_item(self):
        return self.map.map[self.y][self.x] in ITEMS

    def is_on_finish_line(self):
        return self.map.map[self.y][self.x] == FINISH


def gameplay():
    map = Map('level')
    map.show_elements()
    hero = Hero(0, 0, map)
    play = 1
    while play == 1:
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                play = 0
        
            if event.type == KEYDOWN:
                map.screen.blit(PICTURES["floor"], (hero.x*SPRITE_SIZE, hero.y*SPRITE_SIZE))
                if event.key == K_DOWN:
                    hero.move("down")

                if event.key == K_UP:
                    hero.move("up")

                if event.key == K_LEFT:
                    hero.move("left")

                if event.key == K_RIGHT:
                    hero.move("right")
            
            if hero.is_on_item():
                hero.map.map[hero.y][hero.x] = FLOOR
                hero.items += 1
                map.screen.blit(PICTURES["floor"], (hero.x*SPRITE_SIZE, hero.y*SPRITE_SIZE))
            
            map.screen.blit(PICTURES["macgyver"], (hero.x*SPRITE_SIZE, hero.y*SPRITE_SIZE))
            pygame.display.flip()

            if hero.is_on_finish_line():
                if hero.items != 3:
                    map.screen.blit(lost, (0, 0))
                    map.screen.blit(restart, (50, 50))
                    pygame.display.flip()
                    play = 0

                if hero.items == 3:
                    map.screen.blit(victory, (0, 0))
                    map.screen.blit(restart, (50, 50))
                    pygame.display.flip()
                    play = 0

def main():
    pygame.init()
    screen = pygame.display.set_mode(LEVEL_DIMENSION)
    screen.blit(intro, (0 ,0))
    screen.blit(start, (100, 50))
    pygame.display.flip()
    game = 1
    while game == 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_F1:
                gameplay()
            elif event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                game = 0
    
if __name__=="__main__":
    main()