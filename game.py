#! /usr/bin/env python3
# coding: utf-8

import pygame
from maze import Maze
from macgyver import MacGyver

class Game:
    def run(self):
        maze = Maze("level.txt") 
        maze.file_into_list()              
        maze.positions_items()
        maze.positions_stairway_out()
        maze.positions_guardian()        
        maze.display(40, 80)    
        macg = MacGyver(maze)

        running = True
        while running:
            for event in pygame.event.get():    
                # Checking every events happening while the game is running
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.type == pygame.K_ESCAPE):
                    running = False
                    break       
    
                if event.type == pygame.KEYDOWN:        
                    # IF Keyborad press
                    if event.key == pygame.K_DOWN:  
                        # IF Arrow down pressed
                        macg.move_down()            
                        # Move Macguyver down
                
                    if event.key == pygame.K_UP:    
                        macg.move_up()             
                
                    if event.key == pygame.K_RIGHT: 
                        macg.move_right()           
                
                    if event.key == pygame.K_LEFT:  
                        macg.move_left()            
                        
                maze.display(macg.x, macg.y)             
                #RE-Print/Actualize sreen game after an event on keyboard
                macg.check_guardian_position()
                running = macg.check_win()