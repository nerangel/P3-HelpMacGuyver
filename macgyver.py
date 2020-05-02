#! /usr/bin/env python3
# coding: utf-8

import pygame
from constants import SPRITE_SIZE

class MacGyver:
    def __init__(self, maze):
        self.maze = maze
        self.case_x = 3     #location of start in structure (x,y)
        self.case_y = 5
        self.x = 40       #location of start for the sprite (x,y)
        self.y = 80
        self.backpack = 0

    def move_down(self):                                      
        if self.maze.structure[self.case_y + 1][self.case_x] != 'W':    #Mac cannot go through walls
            self.case_y += 1                                           #M cursor in .structure[] is moving
            self.y = self.case_y * SPRITE_SIZE                         #Sprite in labyrinth is moving too
            self.grab_items()

    def move_up(self):
        if self.maze.structure[self.case_y - 1][self.case_x] != 'W':
            self.case_y -= 1
            self.y = self.case_y * SPRITE_SIZE
            self.grab_items()

    def move_right(self):
        if self.maze.structure[self.case_y][self.case_x + 1] != 'W':
            self.case_x += 1
            self.x = self.case_x * SPRITE_SIZE
            self.grab_items()

    def move_left(self):    
        if self.maze.structure[self.case_y][self.case_x - 1] != 'W':
            self.case_x -= 1
            self.x = self.case_x * SPRITE_SIZE
            self.grab_items()

    def grab_items(self):
        for (x, y) in self.maze.positions_items:
            if (self.case_x,self.case_y) == self.maze.positions_items[0]:
                self.backpack =+ 1
                self.maze.positions_items[0] = (5,16)
            elif (self.case_x, self.case_y) == self.maze.positions_items[1]:
                self.backpack =+ 1
                self.maze.positions_items[1] = (8, 16)
            elif (self.case_x, self.case_y) == self.maze.positions_items[2]:
                self.backpack =+ 1
                self.maze.positions_items[2] = (11, 16)

    def check_win(self):
        for x in self.maze.pos_guardian:
            for y in self.maze.pos_guardian:
                if self.case_x == x and self.case_y == y:
                    if self.backpack == 3:
                        self.maze.display_win()
                    else:
                        self.maze.display_lose()