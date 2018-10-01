#! /usr/bin/env python
# coding: utf-8


import random
import pygame

START="s"
FINISH="f" 
FLOOR="0"
WALL="1"

LEVEL_HEIGHT=15
LEVEL_WIDTH=15
ITEMS=["NEEDLE","TUBE","ETHER"]



class Map:
    
    def __init__(self,level_file):
        self.level_file=level_file
        self.generate_map()
        #self.generate_objects()
        
    def generate_map(self):
        with open(self.level_file,'r') as f:
            self.map=[list(x)[:-1] for x in f]
        print(self.map)

    def generate_items(self):
        for item in ITEMS:
            self.x_item=random.randint(0,LEVEL_WIDTH-1)
            self.y_item=random.randint(0,LEVEL_HEIGHT-1)
            while self.map[self.x_item][self.y_item] != FLOOR:
               self.x_item=random.randint(0,LEVEL_WIDTH-1)
               self.y_item=random.randint(0,LEVEL_HEIGHT-1)
            self.map[self.x_item][self.y_item]=item
        print(self.map)

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
    screen=pygame.display.set_mode(LEVEL_HEIGHT,LEVEL_WIDTH)
    map=Map('level')
    

if __name__=="__main__":
    main()