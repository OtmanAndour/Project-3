#! /usr/bin/env python
# coding: utf-8

class Map:
    def __init__(self,level_file):
        self.level_file=level_file



    def generate_map(self,level_file):
        with open(level_file,'r') as f:
            self.map=[ list(x)[:-1] for x in f  ]
            print (self.map)

class Hero:
    def __init__(self):
        pass


class Object:
    def __init__(self):
        pass

def main():
    map=Map("level")
    map.generate_map("level")


if __name__=="__main__":
    main()