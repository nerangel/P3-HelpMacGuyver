#! /usr/bin/env python3
# coding: utf-8

import pygame
from map import Map


def main():
    map = Map("level.txt") # Establishing variable map from class Map with .txt name
    map.lab()              # Creation of a labyrinth
    map.pos_items()        # Positionning items on labyrinth
    map.display(22.5, 60)    

    continued = True
    while continued:
        for event in pygame.event.get():    #Checking every events happening while the game is running
            if event.type == pygame.QUIT:
                continued = False           #Loop is stopped and the game windows is closed



if __name__ == "__main__":
    main()