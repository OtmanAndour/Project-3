import pygame

START="s"
FINISH="f" 
FLOOR="0"
WALL="1"

LEVEL_HEIGHT=15
LEVEL_WIDTH=15
SPRITE_SIZE=40
LEVEL_DIMENSION=(LEVEL_HEIGHT*SPRITE_SIZE,LEVEL_WIDTH*SPRITE_SIZE)
ITEMS=["NEEDLE","TUBE","ETHER"]

pygame.display.set_mode(LEVEL_DIMENSION) 

floor="Images/floor.jpg"
wall="Images/wall.jpg"
guardian="Images/Gardien.png"
needle="Images/aiguille.png"
tube="Images/seringue.png"
ether="Images/ether.png"
macgyver="Images/MacGyver.png"
victory=pygame.transform.scale(pygame.image.load("Images/victory.jpg").convert_alpha(),(LEVEL_HEIGHT*SPRITE_SIZE,LEVEL_WIDTH*SPRITE_SIZE))
lost=pygame.transform.scale(pygame.image.load("Images/lost.jpg").convert_alpha(),(LEVEL_HEIGHT*SPRITE_SIZE,LEVEL_WIDTH*SPRITE_SIZE))

IMAGES={"floor":floor,"wall":wall,"guardian":guardian,"needle":needle,"tube":tube,"ether":ether,"macgyver":macgyver}
for key in IMAGES.keys():
    IMAGES[key]=pygame.image.load(IMAGES[key]).convert_alpha()
    IMAGES[key]=pygame.transform.scale(IMAGES[key],(SPRITE_SIZE,SPRITE_SIZE))
