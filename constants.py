from minesweeper import screen_width,screen_height,size
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0, 0) # Transparent black
GRAY = (110, 117, 115)
HUD_AREA = 150 
TABLE_SIDE = screen_width - HUD_AREA*2#TODO create a box side size
TABLE_X , TABLE_Y = 150 , 50
BOX_SIDE = TABLE_SIDE / size
