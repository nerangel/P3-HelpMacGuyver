#! /usr/bin/env python3
# coding: utf-8

import pygame
import random
from constants import ROWS, COLUMNS, SPRITE_SIZE


class Maze:
    def __init__(self, filename):
        self.filename = filename
        self.load_from_file(filename)
        
        pygame.init()                         
        """windows build"""
        self.window = pygame.display.set_mode((COLUMNS * SPRITE_SIZE, ROWS * SPRITE_SIZE))

        """loading all image with pygame"""
        logo_image = pygame.image.load("ressource/MacGyver.jpg")
        """convert() -> optimization"""
        self.wall_img = pygame.image.load('ressource/wall.png').convert()            
        self.backgr_img = pygame.image.load('ressource/backgr.jpg').convert()           
        """convert_alpha() -> transparency"""
        self.macgyver_img = pygame.image.load('ressource/MacGyver.png').convert_alpha()  
        self.guardian_img = pygame.image.load('ressource/Gardien.png').convert_alpha()
        self.stairsway_out_image = pygame.image.load('ressource/stairsway_out.png').convert_alpha()
        self.needle_img = pygame.image.load('ressource/needle.png').convert_alpha()
        self.ether_img = pygame.image.load('ressource/ether.png').convert_alpha()
        self.syringe_img = pygame.image.load('ressource/seringue.png').convert_alpha()
        self.bubble = pygame.image.load('ressource/bubble.png').convert_alpha()

        """two add for the windows icon and title"""
        pygame.display.set_icon(logo_image) 
        pygame.display.set_caption("Aidez MacGyver à s'échapper !")

        self.guardian_pos = self.get_sprite_pos("G")
        self.stairsway_out_pos = self.get_sprite_pos("O")
        self.randomize_items()

    """display labyrinth and elements"""
    def display(self, mac__x, mac__y, state):                              
        self.window.fill((0, 70, 250))       
        self.window.blit(self.backgr_img, (20, 20))
    
        """run throught .structure[]"""
        for y, col in enumerate(self.structure): 
            for x, case in enumerate(col):
                pos_x = x * SPRITE_SIZE
                pos_y = y * SPRITE_SIZE
                if case == "W":
                    """display wall sprit"""
                    self.window.blit(self.wall_img, (pos_x, pos_y))       
                elif case == "M":
                    """display Macgyver sprit"""
                    self.window.blit(self.macgyver_img, (mac__x, mac__y)) 
                elif case == "O":
                    """display Stairsway out"""
                    self.window.blit(self.stairsway_out_image, (pos_x, pos_y)) 
                elif case == "G":
                    """display the guardian"""
                    self.position_G_sprit = (pos_x,pos_y)
                    self.window.blit(self.guardian_img, (pos_x, pos_y))   

        needle, syringe, ether = self.positions_items
        self.window.blit(self.needle_img, (needle[0] * SPRITE_SIZE,
                                      needle[1] * SPRITE_SIZE))
        self.window.blit(self.syringe_img, (syringe[0] * SPRITE_SIZE,
                                       syringe[1] * SPRITE_SIZE))
        self.window.blit(self.ether_img, (ether[0] * SPRITE_SIZE,
                                     ether[1] * SPRITE_SIZE))
        if state == "slopy_guard":
            self.window.blit(self.bubble, self.position_G_sprit)

                                     
        pygame.display.flip()

    """create maze structure in list from the txt file"""
    def load_from_file(self,filename): 
        self.structure = []
        """opening file.txt in reading mode"""
        with open(filename, "r") as f: 
            """reading each line in file.txt"""
            self.structure = [list(line) for line in f.readlines()]


    def get_sprite_pos(self, sprite):
        for y, col in enumerate(self.structure):
            for x, case in enumerate(col):
                if case == sprite:
                    return x, y

    """define 3 random positions for items"""
    def randomize_items(self):    
        self.items_possibilities = [] 
        """run throught .structure[] searching for " " """
        for y, col in enumerate(self.structure): 
            for x, case in enumerate(col):
                if case == " ":
                    """tuple positions items throught .structure[]"""
                    position_item = (x, y) 
                    """append possibilities position on maze"""
                    self.items_possibilities.append(position_item) 
                    """create a list of possible random positions"""
        self.positions_items = random.sample(self.items_possibilities, 3)
    


    
