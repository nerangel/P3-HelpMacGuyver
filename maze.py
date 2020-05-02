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
        self.window = pygame.display.set_mode((COLUMNS * SPRITE_SIZE, ROWS * SPRITE_SIZE)) # windows build
        pygame.display.set_icon(logo_image) #two add for the windows icon and title
        pygame.display.set_caption("Aidez MacGyver à s'échapper !")



    def file_into_list(self): #Create maze structure in list from the txt file
        self.structure = [] #initialization empty list
        with open(self.filename, "r") as f: #opening file.txt in reading mode
            for line in f:                     #reading each line in file.txt
                line_level = list(line)        #line .txt into list
                line_level = line_level[:-1]    #remove "\n" character from line_level list
                self.structure.append(line_level)   #append line to structure

    
    def positions_items(self):    # define 3 random positions for items
        self.items_possibilities = [] #Create an empty list for items positions
        for y, col in enumerate(self.structure): #run throught .structure[]
            for x, case in enumerate(col):
                if case == " ":
                    position_item = (x, y) #tuple positions items throught .structure[]
                    self.items_possibilities.append(position_item) # Append possibilities position on maze
        self.positions_items = random.sample(self.items_possibilities, 3) # Create a list of possible random positions
    
    
    def display(self, hero_x, hero_y):                              #Display labyrinth and elements
        self.window.fill((0, 70, 250))
        wall_img = pygame.image.load('ressource/wall.png').convert()             #loading all image with pygame
        backgr_img = pygame.image.load('ressource/backgr.jpg').convert()           #convert() -> optimization
        macgyver_img = pygame.image.load('ressource/MacGyver.png').convert_alpha()  #convert_alpha() -> transparency
        guardian_img = pygame.image.load('ressource/Gardien.png').convert_alpha()
        stairsway_out_image = pygame.image.load('ressource/stairsway_out.png').convert_alpha()
        needle_img = pygame.image.load('ressource/needle.png').convert_alpha()
        ether_img = pygame.image.load('ressource/ether.png').convert_alpha()
        syringe_img = pygame.image.load('ressource/seringue.png').convert_alpha()

        self.window.blit(backgr_img, (20, 20))

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


        needle, syringe, ether = self.positions_items
        self.window.blit(needle_img, (needle[0] * SPRITE_SIZE,
                                      needle[1] * SPRITE_SIZE))
        self.window.blit(syringe_img, (syringe[0] * SPRITE_SIZE,
                                       syringe[1] * SPRITE_SIZE))
        self.window.blit(ether_img, (ether[0] * SPRITE_SIZE,
                                     ether[1] * SPRITE_SIZE))


        pygame.display.flip()