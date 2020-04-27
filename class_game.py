#! /usr/bin/env python3
# coding: utf-8

import pygame
import random

#constantes
ROWS = 25
COLUMNS = 25
SPRITE_SIZE = 20

class Map:

    def __init__(self, filename):
        pygame.init()                         
        logo_image = pygame.image.load("ressource/MacGyver.jpg")
        self.filename = filename
        self.window = pygame.display.set_mode((ROWS * SPRITE_SIZE, COLUMNS * SPRITE_SIZE), pygame.RESIZABLE) # windows build
        pygame.display.set_icon(logo_image) #two add for the windows icon and title
        pygame.display.set_caption("Aidez MacGyver à s'échapper !")



    def lab(self): #labyrinth structure from the txt file
        self.structure = [] #initialization empty list
        with open(self.filename, "r") as f: #opening file.txt in reading mode
            for line in f:                     #reading each line in file.txt
                line_level = list(line)        #line .txt into list
                line_level = line_level[:-1]    #remove "\n" character from line_level list
                self.structure.append(line_level)   #append line to structure

    
    def pos_items(self):    # define 3 random positions for items"""
        self.items_poss = [] #Create an empty list for items positions
        for y, col in enumerate(self.structure): #run throught .structure[]
            for x, case in enumerate(col):
                if case == "0":
                    position_items = (x, y) #tuple positions items throught .structure[]
                    self.items_poss.append(position_items) # Append possible position on labyrinth
        self.pos_items = random.sample(self.items_poss, 3) # Create a list of possible random positions
    
    
    def display(self, hero_x, hero_y):                              #Display labyrinth and elements
        self.window.fill((0, 0, 0))
        wall_img = pygame.image.load('ressource/wall.png').convert()             #loading all image with pygame
        backgr_img = pygame.image.load('ressource/backgr.jpg').convert()           #convert() -> optimization
        macgyver_img = pygame.image.load('ressource/MacGyver.png').convert_alpha()  #convert_alpha() -> transparency
        guardian_img = pygame.image.load('ressource/Gardien.png').convert_alpha()
        stairsway_out_image = pygame.image.load('ressource/stairsway_out.png').convert_alpha()
        needle_img = pygame.image.load('ressource/needle.png').convert_alpha()
        ether_img = pygame.image.load('ressource/ether.png').convert_alpha()
        syringe_img = pygame.image.load('ressource/seringue.png').convert_alpha()

        self.window.blit(backgr_img, (0, 0))

        for y, col in enumerate(self.structure): #run throught .structure[]
            for x, case in enumerate(col):
                pos_x = x * SPRITE_SIZE
                pos_y = y * SPRITE_SIZE
                if case == "W":
                    self.window.blit(wall_img, (pos_x, pos_y))       #Display wall sprit
                elif case == "M":
                    self.window.blit(macgyver_img, (hero_x, hero_y)) #Display Macgyver
                elif case == "O":
                    self.window.blit(stairsway_out_image, (pos_x, pos_y)) #Display Stairsway out
                elif case == "G":
                    self.window.blit(guardian_img, (pos_x, pos_y))   #Display the guardian


        needle, syringe, ether = self.pos_items
        self.window.blit(needle_img, (needle[0] * SPRITE_SIZE,
                                      needle[1] * SPRITE_SIZE))
        self.window.blit(syringe_img, (syringe[0] * SPRITE_SIZE,
                                       syringe[1] * SPRITE_SIZE))
        self.window.blit(ether_img, (ether[0] * SPRITE_SIZE,
                                     ether[1] * SPRITE_SIZE))


        pygame.display.flip()

class Macgyver:
    def __init__(self, map):
        self.map = map
        self.case_x = 2     #location of start in structure (x,y)
        self.case_y = 4
        self.x = 22.5       #location of start for the sprite (x,y)
        self.y = 60

    def move_down(self):                                      
        if self.map.structure[self.case_y + 1][self.case_x] != 'W':    #Mac cannot go through walls
            self.case_y += 1                                           #M cursor in .structure[] is moving
            self.y = self.case_y * SPRITE_SIZE                         #Sprite in labyrinth is moving too

    def move_up(self):
        if self.map.structure[self.case_y - 1][self.case_x] != 'W':
            self.case_y -= 1
            self.y = self.case_y * SPRITE_SIZE

    def move_right(self):
        if self.map.structure[self.case_y][self.case_x + 1] != 'W':
            self.case_x += 1
            self.x = self.case_x * SPRITE_SIZE
        
    def move_left(self):    
        if self.map.structure[self.case_y][self.case_x - 1] != 'W':
                self.case_x -= 1
                self.x = self.case_x * SPRITE_SIZE