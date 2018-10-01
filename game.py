#! /usr/bin/env python
# coding: utf-8


import random

START="s"
FINISH="f"
FLOOR="0"
WALL="1"

LEVEL_HEIGHT=15
LEVEL_WIDTH=15
OBJECTS=["NEEDLE","TUBE","ETHER"]



class Map:
    
    def __init__(self,level_file):
        self.level_file=level_file
        self.generate_map()
        
    def generate_map(self):
        with open(self.level_file,'r') as f:
            self.map=[list(x)[:-1] for x in f]
        return self.map


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


class Object:
   
    def __init__(self,map):
        #self.x_obj=x_obj
        #self.y_obj=y_obj
        self.map=map
        self.generate_objects()

    def __repr__(self):
        return self.map

    def generate_objects(self):
        #for obj in OBJECTS:
        #    self.x_obj=random.randint(0,LEVEL_WIDTH)
        #    self.y_obj=random.randint(0,LEVEL_HEIGHT)
        #    while self.map[self.x_obj][self.y_obj] != FLOOR:
        #       self.x_obj=random.randint(0,LEVEL_WIDTH)
        #       self.y_obj=random.randint(0,LEVEL_HEIGHT)
        #    self.map[self.x_obj][self.y_obj]=obj
        return self.map


def main():
    map=Map('level')
    objects=Object(map)
    



if __name__=="__main__":
    main()