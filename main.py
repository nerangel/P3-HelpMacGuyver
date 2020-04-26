#! /usr/bin/env python3
# coding: utf-8
import pygame

def main():
    res = (1080,980)
    windows_game_color = [5, 74, 255]   
    logo_image = pygame.image.load("ressource/MacGyver.png")

    windows_game = pygame.display.set_mode(res, pygame.RESIZABLE)
    pygame.display.set_icon(logo_image)
    pygame.display.set_caption("Aidez MacGyver à s'échapper !")


    windows_game.fill(windows_game_color)
    
    pygame.display.flip()

    continued = True
    while continued:
        for event in pygame.event.get(): #Checking every events happening while the game is running
            if event.type == pygame.QUIT:
                continued = False #Loop is stopped and the game windows is closed



if __name__ == "__main__":
    main()