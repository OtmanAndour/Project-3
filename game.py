#! /usr/bin/env python
# coding: utf-8


import random
import pygame

from pygame import QUIT, KEYDOWN, K_F1, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE

from constants import *


class Map:
    
    def __init__(self,level_file):
        self.level_file=level_file
        self.generate_map()
        self.generate_items()
        self.screen=pygame.display.set_mode(LEVEL_DIMENSION)
        
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
        #self.screen=pygame.display.set_mode(LEVEL_DIMENSION)
        self.screen.blit(pygame.image.load("Images/fond.jpg").convert_alpha(),(0,0))
        for y in range(0,LEVEL_HEIGHT):
            for x in range(0,LEVEL_WIDTH):
                if self.map[y][x] == WALL:
                    self.screen.blit(IMAGES["wall"],(x*SPRITE_SIZE,y*SPRITE_SIZE))
                elif self.map[y][x] == FINISH:
                    self.screen.blit(IMAGES["guardian"],(x*SPRITE_SIZE,y*SPRITE_SIZE))
                elif self.map[y][x] == "NEEDLE":
                    self.screen.blit(IMAGES["needle"],(x*SPRITE_SIZE,y*SPRITE_SIZE))
                elif self.map[y][x] == "TUBE":
                    self.screen.blit(IMAGES["tube"],(x*SPRITE_SIZE,y*SPRITE_SIZE))
                elif self.map[y][x] == "ETHER":
                    self.screen.blit(IMAGES["ether"],(x*SPRITE_SIZE,y*SPRITE_SIZE))
                elif self.map[y][x] == START:
                    self.screen.blit(IMAGES["macgyver"],(x*SPRITE_SIZE,y*SPRITE_SIZE))
                else:
                    self.screen.blit(IMAGES["floor"],(x*SPRITE_SIZE,y*SPRITE_SIZE)) 
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
            if self.y < LEVEL_HEIGHT-1:
                if self.map.map[self.y + 1][self.x] != WALL:
                    self.y +=1
        
        elif direction == "up":
            if self.y != 0:
                if self.map.map[self.y - 1][self.x] != WALL:
                    self.y -=1
        
        elif direction == "left":
            if self.x != 0:
                if self.map.map[self.y][self.x - 1] != WALL:
                    self.x -=1

        elif direction == "right":
            if self.x < LEVEL_WIDTH-1:
                if self.map.map[self.y][self.x + 1] != WALL:
                    self.x +=1

    def is_on_item(self):
        return self.map.map[self.y][self.x] in ITEMS

    def is_on_finish_line(self):
        return self.map.map[self.y][self.x] == FINISH


def main():
    pygame.init()
    map=Map('level')
    map.show_elements()
    hero=Hero(0,0,map)
    play = 1
    while play == 1:
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                play = 0
        
            if event.type == KEYDOWN:
                map.screen.blit(IMAGES["floor"],(hero.x*SPRITE_SIZE,hero.y*SPRITE_SIZE))
                if event.key == K_DOWN:
                    hero.move("down")

                if event.key == K_UP:
                    hero.move("up")

                if event.key == K_LEFT:
                    hero.move("left")

                if event.key == K_RIGHT:
                    hero.move("right")
            
            if hero.is_on_item():
                hero.map.map[hero.y][hero.x]=FLOOR
                hero.items += 1
                map.screen.blit(IMAGES["floor"],(hero.x*SPRITE_SIZE,hero.y*SPRITE_SIZE))
            
            map.screen.blit(IMAGES["macgyver"],(hero.x*SPRITE_SIZE,hero.y*SPRITE_SIZE))
            pygame.display.flip()

            if hero.is_on_finish_line():
                if hero.items != 3:
                    map.screen.blit(lost,(0,0))
                    pygame.display.flip()
                    play=0
                    pygame.time.delay(5000)

                if hero.items == 3:
                    map.screen.blit(victory,(0,0))
                    pygame.display.flip()
                    play=0
                    pygame.time.delay(5000)
    

if __name__=="__main__":
    main()