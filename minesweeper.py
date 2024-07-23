import tkinter as tk
from tkinter import messagebox
import pygame
import sys
import random
import time
from userInterface import get_table_info
class game_object:
    def __init__(self , id = "blank" , status = "unmarked" , neighbour_bomb = 0 , position = (None , None) , isVisiable = False):
        self.id = id 
        self.status = status
        self.neighbourBomb = neighbour_bomb
        self.pos = position
        self.isVisiable = isVisiable

lose = False
size , mines = get_table_info()

print(size , " " , mines)



pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("MineSweeper")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0, 0) # Transparent black
GRAY = (110, 117, 115)
HUD_AREA = 150 
TABLE_SIDE = screen_width - HUD_AREA*2#TODO create a box side size
TABLE_X , TABLE_Y = 150 , 50
BOX_SIDE = TABLE_SIDE / size
flag = pygame.image.load(r'flag.bmp')
question = pygame.image.load(r'question.bmp')
bomb_dised = pygame.image.load(r'bomb_dised.bmp')
bomb_blewup = pygame.image.load(r'bomb_blewup.bmp')

flag = pygame.transform.scale(flag , (BOX_SIDE -BOX_SIDE*0.1 , BOX_SIDE-BOX_SIDE*0.1))
question = pygame.transform.scale(question , (BOX_SIDE -BOX_SIDE*0.1 , BOX_SIDE-BOX_SIDE*0.1))
bomb_dised = pygame.transform.scale(bomb_dised , (BOX_SIDE , BOX_SIDE))
bomb_blewup = pygame.transform.scale(bomb_blewup , (BOX_SIDE , BOX_SIDE))


# Main game loop
left , right = False,False
table_array = [[game_object() for q in range(size)] for q in range(size)]
for i in range(size):
    for j in range(size):
        table_array[i][j].pos = (j,i)

blank_cluster = [[]]
first_press = True
def get_index(click_pos , size):
    return ((click_pos[0]-HUD_AREA)//(BOX_SIDE)  , (click_pos[1]-50)//(BOX_SIDE))

def is_in_2dArray(array , obj):
    for i in array:
        for j in i:
            if j.pos == obj.pos:
                return True 
    return False
start_time = time.time()
visiable_boxes = 0
while True:
    click_pos = (None , None)
    clcik_index = (-1 , -1)
    for event in pygame.event.get():
        buttons = pygame.mouse.get_pressed()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            

            click_pos = (pygame.mouse.get_pos())
            clcik_index = tuple(map(lambda n:int(n), get_index(click_pos , size)))
            
            if first_press and clcik_index[0] >= 0 and clcik_index[1] >= 0:
                first_press = False
                bomb_list = []
                while len(bomb_list) != mines:
                    bomb = (random.randint(0,size-1) , random.randint(0,size-1))
                    if not bomb in bomb_list and not bomb[0] in [clcik_index[0] , clcik_index[0] - 1 , clcik_index[0] +1] and not bomb[1] in [clcik_index[1] , clcik_index[1] - 1 , clcik_index[1] +1] :
                        bomb_list.append(bomb)
                print(bomb_list)
                for b in bomb_list:
                    
                    table_array[b[1]][b[0]].id = "bomb"
                    for x in range(-1 , 2):
                        for y in range(-1 , 2):
                            if b[1]+y < 0 or b[0]+x < 0 or b[1]+y > size-1 or b[0]+x >size-1 :
                                continue
                            if (x!=0 or y!=0) and table_array[b[1]+y][b[0]+x].id != "bomb" :
                                table_array[b[1]+y][b[0]+x].id = "number"
                                table_array[b[1]+y][b[0]+x].neighbourBomb += 1
                for i in table_array:
                    print(list(map(lambda n:n.id[-1]+str(n.neighbourBomb) , i)))
                
                for row in table_array:
                    for box in row:
                        if box.id == "blank" and not is_in_2dArray(blank_cluster , box):
                            cluster = [box]
                            next_cluster = []

                            while True:
                                for obj in cluster:
                                    blank_cluster[-1].append(obj)
                                    if obj.id == "number":
                                        continue
                                
                                    for x in range(-1 , 2):
                                        for y in range(-1 , 2):
                                            if abs(x) != abs(y) and not obj.pos[0]+x  < 0 and not  obj.pos[1]+y  < 0 and not obj.pos[0]+x  > size-1 and not  obj.pos[1]+y  >size-1:
                                                new_obj = table_array[obj.pos[1] + y][obj.pos[0]+x]
                                                if new_obj.id != "bomb" and not is_in_2dArray(blank_cluster , new_obj) and not new_obj in next_cluster:
                                                    next_cluster.append(new_obj)
                                cluster = [q for q in next_cluster]
                                
                                if len(next_cluster) == 0 :
                                    
                                    break
                                next_cluster = []
                            blank_cluster.append([])
                
                blank_cluster.pop(-1)

            if  buttons[0]:
                left = True
            elif buttons[2]:
                right = True


    screen.fill(WHITE)
    game_table = pygame.Rect(TABLE_X,TABLE_Y,TABLE_SIDE,TABLE_SIDE)
    pygame.draw.rect(screen , GRAY , game_table)
    for x in range(size+1):
        pygame.draw.line(screen, BLACK, (x*(BOX_SIDE)+HUD_AREA,550), (x*(BOX_SIDE)+HUD_AREA,50), width=3)
    for y in range(size+1):
        pygame.draw.line(screen, BLACK, (150,y*(BOX_SIDE)+50), (650,y*(BOX_SIDE)+50), width=3)
    #color_list = [(255,0,0) , (0,255,0) , (0,0,255) , (0,0,0)]
    for row in table_array:
            for obj in row:
                pos_x = obj.pos[0]*(BOX_SIDE) + HUD_AREA +BOX_SIDE*0.1
                pos_y = obj.pos[1]*(BOX_SIDE) + TABLE_Y +BOX_SIDE*0.1
                if obj.status == "flag":
                    
                    
                    screen.blit(flag , (pos_x,pos_y))
                elif obj.status == "question":
                    
                    
                    screen.blit(question , (pos_x,pos_y))
                elif obj.isVisiable:#TODO fix
                    visiable_boxes+=1 
                    
                    blank_box = pygame.Rect(pos_x - 0.05 * BOX_SIDE , pos_y- 0.05 * BOX_SIDE ,BOX_SIDE ,BOX_SIDE)
                    pygame.draw.rect(screen , WHITE , blank_box)
                    if obj.id == "number":
                        color_list = [(0,0,255) , (0,255,0) , (255,0,0) , (255,0,255) , (45,98,2) , (12,25,89)]
                        font = pygame.font.SysFont("Arial", int((BOX_SIDE) * 36/50) )
                        txtsurf = font.render(f"{obj.neighbourBomb}", True, color_list[obj.neighbourBomb-1])
                        screen.blit(txtsurf,(pos_x+BOX_SIDE/3.5 , pos_y))
                    for x in range(size+1):
                        pygame.draw.line(screen, BLACK, (x*(BOX_SIDE)+HUD_AREA,550), (x*(BOX_SIDE)+HUD_AREA,50), width=3)
                    for y in range(size+1):
                        pygame.draw.line(screen, BLACK, (150,y*(BOX_SIDE)+50), (650,y*(BOX_SIDE)+50), width=3)
    
    if clcik_index[0] >= 0 and clcik_index[1] >= 0:
        clicked_obj = table_array[clcik_index[1]][clcik_index[0]]
        if right:
            proirity_list = ["unmarked" , "flag" , "question"]
            
            clicked_obj.status =proirity_list[(proirity_list.index(clicked_obj.status)+1) %3]
        if left and clicked_obj.status != "flag":
            if clicked_obj.id == "bomb":
                lose = True 
            else:
                clicked_obj.isVisiable = True
                for cluster in blank_cluster:
                    for box in cluster:
                        if box.pos[0] == clicked_obj.pos[0] and box.pos[1] == clicked_obj.pos[1]:
                            for item in cluster:
                                item.isVisiable = True
    font = pygame.font.SysFont("Arial",  36)
    seconds = str(int((time.time()-start_time)%60))
    minutes = str(int((time.time()-start_time) // 60))
    if int(seconds) < 10:
        seconds = "0" + seconds
    txtsurf = font.render(f"{minutes} :{seconds}", True, (0,0,0))
    screen.blit(txtsurf,(50 , 300))


    if lose or (size**2) - visiable_boxes == mines:
        for bomb in bomb_list:
            x = bomb[0]*(BOX_SIDE) + HUD_AREA +BOX_SIDE*0.1- 0.05 * BOX_SIDE
            y = bomb[1]*(BOX_SIDE) + TABLE_Y +BOX_SIDE*0.1- 0.05 * BOX_SIDE
                
                
            if table_array[bomb[1]][bomb[0]].status == "flag":
                screen.blit(bomb_dised , (x,y))
            else:
                screen.blit(bomb_blewup , (x,y))
            for x in range(size+1):
                pygame.draw.line(screen, BLACK, (x*(BOX_SIDE)+HUD_AREA,550), (x*(BOX_SIDE)+HUD_AREA,50), width=3)
            for y in range(size+1):
                pygame.draw.line(screen, BLACK, (150,y*(BOX_SIDE)+50), (650,y*(BOX_SIDE)+50), width=3)

    pygame.display.flip()
    left , right = False,False
    if lose:
        messagebox.showerror("", "you lost :(")
        break
    elif (size**2) - visiable_boxes == mines:
        messagebox.showerror("", "you won :)")
        break
    visiable_boxes = 0




