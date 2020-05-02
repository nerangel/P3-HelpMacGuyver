#! /usr/bin/env python3
# coding: utf-8

import pygame
from maze import Maze
from macgyver import MacGyver

def main():
    maze = Maze("level.txt") 
    maze.file_into_list()              
    maze.positions_items()        
    maze.display(22.5, 60)    
    macg = MacGyver(maze)

    running = True
    while running:
        for event in pygame.event.get():    # Checking every events happening while the game is running
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.type == pygame.K_ESCAPE):
                running = False           # Loop is stopped and the game windows is close
    
            if event.type == pygame.KEYDOWN:        # IF Keyborad press
                if event.key == pygame.K_DOWN:  # IF Arrow down pressed
                    macg.move_down()            # Move Macguyver down
                
                if event.key == pygame.K_UP:    # IF Arrow up pressed
                    macg.move_up()              # Move Macguyver up
                
                if event.key == pygame.K_RIGHT: # IF Arrow right pressed
                    macg.move_right()           # Move Macguyver right
                
                if event.key == pygame.K_LEFT:  # IF Arrow left pressed
                    macg.move_left()            # Move Macguyver left
                        
            maze.display(macg.x, macg.y)             #RE-Print/Actualize sreen game after an event on keyboard
        

if __name__ == "__main__":
    main()