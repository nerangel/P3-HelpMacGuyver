#! /usr/bin/env python3
# coding: utf-8

import pygame
import random
from constants import ROWS, COLUMNS, SPRITE_SIZE


class Maze:

    def __init__(self, filename):
        pygame.init()                         
        logo_image = pygame.image.load("ressource/MacGyver.jpg")
        self.filename = filename
        # windows build
        self.window = pygame.display.set_mode((COLUMNS * SPRITE_SIZE, ROWS * SPRITE_SIZE)) 
        #two add for the windows icon and title
        pygame.display.set_icon(logo_image) 
        pygame.display.set_caption("Aidez MacGyver à s'échapper !")


    #Create maze structure in list from the txt file
    def file_into_list(self): 
        self.structure = []
        #opening file.txt in reading mode
        with open(self.filename, "r") as f: 
            #reading each line in file.txt
            for line in f:                    
                #line .txt into list
                line_level = list(line)
                #remove "\n" character from line_level list       
                line_level = line_level[:-1]   
                #append line to structure 
                self.structure.append(line_level)   

    def positions_guardian(self):
        for y, col in enumerate(self.structure):
            for x, case in enumerate(col):
                if case == "G":
                    self.positions_guardian = (x, y)
    
    def positions_stairway_out(self):
        for y, col in enumerate(self.structure):
            for x, case in enumerate(col):
                if case == "O":
                    self.positions_stairway_out = (x, y)

    # define 3 random positions for items
    def positions_items(self):    
        self.items_possibilities = [] 
        #run throught .structure[] searching for " "
        for y, col in enumerate(self.structure): 
            for x, case in enumerate(col):
                if case == " ":
                    #tuple positions items throught .structure[]
                    position_item = (x, y) 
                    # Append possibilities position on maze
                    self.items_possibilities.append(position_item) 
                    # Create a list of possible random positions
        self.positions_items = random.sample(self.items_possibilities, 3)
    
    
    #Display labyrinth and elements
    def display(self, hero_x, hero_y):                              
        self.window.fill((0, 70, 250))
        #loading all image with pygame
        #convert() -> optimization
        wall_img = pygame.image.load('ressource/wall.png').convert()            
        backgr_img = pygame.image.load('ressource/backgr.jpg').convert()           
        #convert_alpha() -> transparency
        macgyver_img = pygame.image.load('ressource/MacGyver.png').convert_alpha()  
        guardian_img = pygame.image.load('ressource/Gardien.png').convert_alpha()
        stairsway_out_image = pygame.image.load('ressource/stairsway_out.png').convert_alpha()
        needle_img = pygame.image.load('ressource/needle.png').convert_alpha()
        ether_img = pygame.image.load('ressource/ether.png').convert_alpha()
        syringe_img = pygame.image.load('ressource/seringue.png').convert_alpha()

        self.window.blit(backgr_img, (20, 20))

        #run throught .structure[]
        for y, col in enumerate(self.structure): 
            for x, case in enumerate(col):
                pos_x = x * SPRITE_SIZE
                pos_y = y * SPRITE_SIZE
                if case == "W":
                    #Display wall sprit
                    self.window.blit(wall_img, (pos_x, pos_y))       
                elif case == "M":
                    #Display Macgyver sprit
                    self.window.blit(macgyver_img, (hero_x, hero_y)) 
                elif case == "O":
                    #Display Stairsway out
                    self.window.blit(stairsway_out_image, (pos_x, pos_y)) 
                elif case == "G":
                    #Display the guardian
                    self.possition_G_sprit = (pos_x,pos_y)
                    self.window.blit(guardian_img, (pos_x, pos_y))   


        needle, syringe, ether = self.positions_items
        self.window.blit(needle_img, (needle[0] * SPRITE_SIZE,
                                      needle[1] * SPRITE_SIZE))
        self.window.blit(syringe_img, (syringe[0] * SPRITE_SIZE,
                                       syringe[1] * SPRITE_SIZE))
        self.window.blit(ether_img, (ether[0] * SPRITE_SIZE,
                                     ether[1] * SPRITE_SIZE))


        pygame.display.flip()

    def display_slept_guardian(self):
        #Display the slopy guardian
        bubble = pygame.image.load('ressource/bubble.png').convert_alpha()
        self.window.blit(bubble, self.possition_G_sprit)
        pygame.display.flip()

    def display_win(self):
        #Display the victory screen
        reset = 0
        lose = True
        win_img = pygame.image.load('ressource/win.jpg').convert_alpha()
        self.window.blit(win_img, (0, 0))
        pygame.display.flip()

        while lose:
            for event in pygame.event.get(): 
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    reset = 1
                    lose = False
                    return reset
                            
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    reset = 2
                    lose = False
                    return reset
    
    def display_lose(self):
        #Display the defeat screen
        reset = 0
        lose = True
        lose_img = pygame.image.load('ressource/game_over.jpg').convert_alpha()
        self.window.blit(lose_img, (0, 0))
        pygame.display.flip()

        while lose:
            for event in pygame.event.get(): 
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    reset = 1
                    lose = False
                    return reset
                            
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    reset = 2
                    lose = False
                    return reset