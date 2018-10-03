import pygame


START="s"
FINISH="f" 
FLOOR="0"
WALL="1"

LEVEL_HEIGHT=15
LEVEL_WIDTH=15
SPRITE_SIZE=30
LEVEL_DIMENSION=(LEVEL_HEIGHT*SPRITE_SIZE,LEVEL_WIDTH*SPRITE_SIZE)
ITEMS=["NEEDLE","TUBE","ETHER"]

pygame.display.set_mode(LEVEL_DIMENSION)


wall=pygame.image.load("Images/wall.jpg").convert_alpha()
wall=pygame.transform.scale(wall,(SPRITE_SIZE,SPRITE_SIZE))
guardian=pygame.image.load("Images/Gardien.png").convert_alpha()
guardian=pygame.transform.scale(guardian,(SPRITE_SIZE,SPRITE_SIZE))
needle=pygame.image.load("Images/aiguille.png").convert_alpha()
needle=pygame.transform.scale(needle,(SPRITE_SIZE,SPRITE_SIZE))
tube=pygame.image.load("Images/seringue.png").convert_alpha()
tube=pygame.transform.scale(tube,(SPRITE_SIZE,SPRITE_SIZE))
ether=pygame.image.load("Images/ether.png").convert_alpha()
ether=pygame.transform.scale(ether,(SPRITE_SIZE,SPRITE_SIZE))
macgyver=pygame.image.load("Images/MacGyver.png").convert_alpha()
macgyver=pygame.transform.scale(macgyver,(SPRITE_SIZE,SPRITE_SIZE))
