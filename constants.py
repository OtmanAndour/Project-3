"""File containing all the constants used by the game.py file"""

import pygame

START = "s"
FINISH = "f" 
FLOOR = "0"
WALL = "1"

LEVEL_HEIGHT = 15
LEVEL_WIDTH = 15
SPRITE_SIZE = 40
LEVEL_DIMENSION = (LEVEL_HEIGHT*SPRITE_SIZE, LEVEL_WIDTH*SPRITE_SIZE)
ITEMS = ["NEEDLE","TUBE","ETHER"]

pygame.display.set_mode(LEVEL_DIMENSION) 
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

start = myfont.render('Press F1 to start the game', False, (0, 0, 0))
restart = myfont.render('Press F1 to play again or ESC to quit', False, (0, 0, 0))

floor = "Images/floor.jpg"
wall = "Images/wall.jpg"
guardian = "Images/Gardien.png"
needle = "Images/aiguille.png"
tube = "Images/seringue.png"
ether = "Images/ether.png"
macgyver = "Images/MacGyver.png"
intro = pygame.image.load("Images/Intro.jpg").convert_alpha()
intro = pygame.transform.scale(intro, (LEVEL_HEIGHT*SPRITE_SIZE,LEVEL_WIDTH*SPRITE_SIZE))
victory = pygame.image.load("Images/victory.jpg").convert_alpha()
victory = pygame.transform.scale(victory,(LEVEL_HEIGHT*SPRITE_SIZE,LEVEL_WIDTH*SPRITE_SIZE))
lost = pygame.image.load("Images/lost.jpg").convert_alpha()
lost = pygame.transform.scale(lost,(LEVEL_HEIGHT*SPRITE_SIZE,LEVEL_WIDTH*SPRITE_SIZE))

PICTURES = {
    "floor": floor, "wall": wall, "guardian": guardian, 
    "needle": needle, "tube": tube, "ether": ether, "macgyver": macgyver
}
for key in PICTURES.keys():
    PICTURES[key] = pygame.image.load(PICTURES[key]).convert_alpha()
    PICTURES[key] = pygame.transform.scale(PICTURES[key],(SPRITE_SIZE,SPRITE_SIZE))