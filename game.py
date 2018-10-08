#! /usr/bin/env python
# coding: utf-8

"""Main file for the MacGyver game."""

import random
import sys
import pygame
from pygame import QUIT, KEYDOWN, K_F1, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE
from constants import *


class Map:
    """Class creating the map and displaying it on the Pygame window """
    def __init__(self, level_file):
        self.level_file = level_file
        self.generate_map()
        self.generate_items()
        self.screen = pygame.display.set_mode(LEVEL_DIMENSION)
        
    def generate_map(self):
        """ Create a matrix from the level file """
        with open(self.level_file, 'r') as f:
            self.map = [list(x)[:-1] for x in f]
        if not self.check_height():
            print("Map height does not match set level height. Please change the value of LEVEL_HEIGHT accordingly.")
            sys.exit()
        elif not self.check_width():
            print("Map width does not match set level width. Please change the value of LEVEL_WIDTH accordingly.")
            sys.exit()
        else:
            return self.map

    def check_height(self):
        "Checks if map height matches the level height"
        return len(self.map) == LEVEL_HEIGHT

    def check_width(self):
        "Checks if map widht matches the level width"
        return len(self.map[0]) == LEVEL_WIDTH

    def generate_items(self):
        """Places the items randomly in the map level"""
        for item in ITEMS:
            self.x_item = random.randint(0, LEVEL_WIDTH-1)
            self.y_item = random.randint(0, LEVEL_HEIGHT-1)
            while self.map[self.x_item][self.y_item] != FLOOR:
               self.x_item = random.randint(0, LEVEL_WIDTH-1)
               self.y_item = random.randint(0, LEVEL_HEIGHT-1)
            self.map[self.x_item][self.y_item] = item
        return self.map

    def show_elements(self):
        """Display all the elements in the map as the game starts"""
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
    "Class representing MacGyver"
    def __init__(self, x_pos, y_pos, map):
        self.x = x_pos
        self.y = y_pos
        self.items = 0
        self.map = map 

    def move(self, direction):
        """Allows MacGyver to move according to the chosen direction"""
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
        """Checks if MacGyver is on an item or not"""
        return self.map.map[self.y][self.x] in ITEMS

    def is_on_finish_line(self):
        """Checks if MacGyver reached the guardian"""
        return self.map.map[self.y][self.x] == FINISH


def gameplay():
    """Function that sets up the game and makes it run"""
    map = Map('level')
    map.show_elements()
    hero = Hero(0, 0, map)
    play = 1
    while play == 1:
        """Loop for the game"""
        for event in pygame.event.get():
            """If ESC is pressed, exit the game and close the program"""
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit()

            if event.type == KEYDOWN:
                """Moves MacGyver according to key pressed"""
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
                """Increments item counter if walked on an item"""
                hero.items += 1
                hero.map.map[hero.y][hero.x] = FLOOR
                map.screen.blit(PICTURES["floor"], (hero.x*SPRITE_SIZE, hero.y*SPRITE_SIZE))
            
            map.screen.blit(PICTURES["macgyver"], (hero.x*SPRITE_SIZE, hero.y*SPRITE_SIZE))
            pygame.display.flip()

            if hero.is_on_finish_line():
                """Display win or lose screen according to items picked"""
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
    screen = pygame.display.set_mode((LEVEL_DIMENSION))
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