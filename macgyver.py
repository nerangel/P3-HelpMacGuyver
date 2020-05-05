#! /usr/bin/env python3
# coding: utf-8

from constants import SPRITE_SIZE

class MacGyver:
    def __init__(self, maze):
        self.maze = maze
        #location of start in structure (x,y)
        self.location_M_x = 2     
        self.location_M_y = 4
        #location of start for the sprite (x,y)
        self.x = 40       
        self.y = 80
        self.backpack = 0

    def move_down(self):
        #Mac cannot go through walls                                      
        if self.maze.structure[self.location_M_y + 1][self.location_M_x] != 'W': 
            #M cursor in .structure[] is moving   
            self.location_M_y += 1      
            #Sprite in labyrinth is moving too                                     
            self.y = self.location_M_y * SPRITE_SIZE                        
            self.grab_items()

    def move_up(self):
        if self.maze.structure[self.location_M_y - 1][self.location_M_x] != 'W':
            self.location_M_y -= 1
            self.y = self.location_M_y * SPRITE_SIZE
            self.grab_items()

    def move_right(self):
        if self.maze.structure[self.location_M_y][self.location_M_x + 1] != 'W':
            self.location_M_x += 1
            self.x = self.location_M_x * SPRITE_SIZE
            self.grab_items()

    def move_left(self):    
        if self.maze.structure[self.location_M_y][self.location_M_x - 1] != 'W':
            self.location_M_x -= 1
            self.x = self.location_M_x * SPRITE_SIZE
            self.grab_items()

    def grab_items(self):
        if (self.location_M_x,self.location_M_y) == self.maze.positions_items[0]:
            self.backpack += 1
            self.maze.positions_items[0] = (5,16)
        elif (self.location_M_x, self.location_M_y) == self.maze.positions_items[1]:
            self.backpack += 1
            self.maze.positions_items[1] = (8, 16)
        elif (self.location_M_x, self.location_M_y) == self.maze.positions_items[2]:
            self.backpack += 1
            self.maze.positions_items[2] = (11, 16)

    def check_guardian_position(self):
        if self.location_M_x == self.maze.positions_guardian[0] and self.location_M_y == self.maze.positions_guardian[1]:               
            if self.backpack == 3:
                self.maze.display_slept_guardian()
            else:
                self.maze.display_lose()

    def check_win(self):
        running = True
        if self.location_M_x == self.maze.positions_stairway_out[0] and self.location_M_y == self.maze.positions_stairway_out[1]:
            self.maze.display_win()
            running = False 
        return running