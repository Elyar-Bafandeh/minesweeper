import pygame
from constants import BOX_SIDE
def loadIcons():
    flag = pygame.image.load(r'flag.bmp')
    question = pygame.image.load(r'question.bmp')
    bomb_dised = pygame.image.load(r'bomb_dised.bmp')
    bomb_blewup = pygame.image.load(r'bomb_blewup.bmp')
    return flag , question , bomb_dised , bomb_blewup

def scaleIcons(flag , question , bomb_dised , bomb_blewup):
    flag = pygame.transform.scale(flag , (BOX_SIDE -BOX_SIDE*0.1 , BOX_SIDE-BOX_SIDE*0.1))
    question = pygame.transform.scale(question , (BOX_SIDE -BOX_SIDE*0.1 , BOX_SIDE-BOX_SIDE*0.1))
    bomb_dised = pygame.transform.scale(bomb_dised , (BOX_SIDE , BOX_SIDE))
    bomb_blewup = pygame.transform.scale(bomb_blewup , (BOX_SIDE , BOX_SIDE))

def getIcons():
    flag , question , bomb_dised , bomb_blewup = loadIcons()
    scaleIcons()
    return flag , question , bomb_dised , bomb_blewup
