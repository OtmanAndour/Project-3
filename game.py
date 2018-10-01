#! /usr/bin/env python
# coding: utf-8


import random
import pygame

from pygame.locals import QUIT, KEYDOWN, K_F1, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE

from constants import *


class Map:
    
    def __init__(self,level_file):
        self.level_file=level_file
        self.generate_map()
        self.generate_items()
        
    def generate_map(self):
        with open(self.level_file,'r') as f:
            self.map=[list(x)[:-1] for x in f]
        return self.map

    def generate_items(self):
        for item in ITEMS:
            self.x_item=random.randint(0,LEVEL_WIDTH-1)
            self.y_item=random.randint(0,LEVEL_HEIGHT-1)
            while self.map[self.x_item][self.y_item] != FLOOR:
               self.x_item=random.randint(0,LEVEL_WIDTH-1)
               self.y_item=random.randint(0,LEVEL_HEIGHT-1)
            self.map[self.x_item][self.y_item]=item
        return self.map

    def show_elements(self):
        screen=pygame.display.set_mode(LEVEL_DIMENSION)
        screen.blit(pygame.image.load("Images/fond.jpg").convert_alpha(),(0,0))
        for y in range(0,LEVEL_HEIGHT):
            for x in range(0,LEVEL_WIDTH):
                if self.map[y][x] == WALL:
                    screen.blit(wall,(x*SPRITE_SIZE,y*SPRITE_SIZE))
                elif self.map[y][x] == FINISH:
                    screen.blit(guardian,(x*SPRITE_SIZE,y*SPRITE_SIZE))
                elif self.map[y][x] == "NEEDLE":
                    screen.blit(needle,(x*SPRITE_SIZE,y*SPRITE_SIZE))
                elif self.map[y][x] == "TUBE":
                    screen.blit(tube,(x*SPRITE_SIZE,y*SPRITE_SIZE))
                elif self.map[y][x] == "ETHER":
                    screen.blit(ether,(x*SPRITE_SIZE,y*SPRITE_SIZE))
                elif self.map[y][x] == START:
                    screen.blit(macgyver,(x*SPRITE_SIZE,y*SPRITE_SIZE))
        pygame.display.flip()
        
    


class Hero:
    def __init__(self,x_pos,y_pos,map):
        self.x=x_pos
        self.y=y_pos
        self.items=0
        self.map=map #Here, map will be set in the main function, using : map=Map("level")

    def move(self,direction):
#This is how MacGiver is going to be moved, but i still need to figure out how to define down,up,left and right with pygame probably
        if direction == "down":
            if self.y <= LEVEL_HEIGHT:
                if self.map[self.y + 1][self.x] != WALL:
                    self.y +=1
        
        elif direction == "up":
            if self.y <= LEVEL_HEIGHT:
                if self.map[self.y - 1][self.x] != WALL:
                    self.y -=1
        
        elif direction == "left":
            if self.x <= LEVEL_WIDTH:
                if self.map[self.y][self.x - 1] != WALL:
                    self.x -=1

        elif direction == "right":
            if self.y <= LEVEL_WIDTH:
                if self.map[self.y][self.x + 1] != WALL:
                    self.x +=1



def main():
    pygame.init()
    map=Map('level')
    map.show_elements()
    play = 1
    while play == 1:
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
    


if __name__=="__main__":
    main()