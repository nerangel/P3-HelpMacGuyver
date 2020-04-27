#! /usr/bin/env python3
# coding: utf-8

import pygame
from class_game import Map, Macgyver

def main():
    map = Map("level.txt") # Establishing variable map from class Map with .txt name
    map.lab()              # Creation of a labyrinth
    map.pos_items()        # Positionning items on labyrinth
    map.display(22.5, 60)    
    macg = Macgyver(map)

    continued = True
    while continued:
        for event in pygame.event.get():    # Checking every events happening while the game is running
            if event.type == pygame.QUIT:
                continued = False           # Loop is stopped and the game windows is close
    
            if event.type == pygame.KEYDOWN:        # IF Keyborad press
                    if event.key == pygame.K_DOWN:  # IF Arrow down pressed
                        macg.move_down()            # Move Macguyver down
                    if event.key == pygame.K_UP:    # IF Arrow up pressed
                        macg.move_up()              # Move Macguyver up
                    if event.key == pygame.K_RIGHT: # IF Arrow right pressed
                        macg.move_right()           # Move Macguyver right
                    if event.key == pygame.K_LEFT:  # IF Arrow left pressed
                        macg.move_left()            # Move Macguyver left
            map.display(macg.x, macg.y)             #RE-Print/Actualize sreen game after an event on keyboard

if __name__ == "__main__":
    main()