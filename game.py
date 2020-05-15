#! /usr/bin/env python3
# coding: utf-8

import pygame
from maze import Maze
from constants import SPRITE_SIZE


class Game:
    def __init__(self):
        self.maze = Maze("level.txt") 
        self.state = ""
        #location of start in structure (x,y)
        self.pos_mac_x = 2     
        self.pos_mac_y = 4
        #location of start for the sprite (x,y)
        self.x = 40       
        self.y = 80
        self.backpack = 0


    def run(self):
        #Loop of test for event and win / lose conditions
        self.state = "running"
        while True:
            if self.state == "running" or self.state == "slopy_guard":
                #actualize / RE-Print sreen game after an event on keyboard       
                self.maze.display(self.x, self.y, self.state)
            #checking every events happening while the game is running
            for event in pygame.event.get():    
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.state = "quit"
                    return         
    
                #when keyborad's press       
                if event.type == pygame.KEYDOWN:
                    if self.state == "running" or self.state == "slopy_guard":   
                        #if arrow down pressed
                        if event.key == pygame.K_DOWN:  
                            #ove macguyver down
                            self.move("down")            
                            
                        elif event.key == pygame.K_UP:    
                            self.move("up")             
                    
                        elif event.key == pygame.K_RIGHT: 
                            self.move("right")           
                    
                        elif event.key == pygame.K_LEFT:  
                            self.move("left")
                        #check win or lose conditions and guardian on maps       
                        self.state = self.check_status()
                        
                    #change the state of the game
                    if self.state != "running" and self.state != "slopy_guard":                
                        if  event.key == pygame.K_r:
                            self.state = "reset"
                            return 
                        
                        elif event.key == pygame.K_q:
                            self.state = "quit"
                            return
              


                                 
    def check_status(self)->str:
        #after each move checking the new case for return a state for the game
        if self.pos_mac_x == self.maze.stairsway_out_pos[0] and self.pos_mac_y == self.maze.stairsway_out_pos[1]:
            #display the victory screen
            win_img = pygame.image.load('ressource/win.jpg').convert_alpha()
            self.maze.window.blit(win_img, (0, 0))
            pygame.display.flip()
            return "win"
        
        elif self.pos_mac_x == self.maze.guardian_pos[0] and self.pos_mac_y == self.maze.guardian_pos[1]:               
            if self.backpack == 3:
                return "slopy_guard"
            else:
                #display the defeat screen
                lose_img = pygame.image.load('ressource/game_over.jpg').convert_alpha()
                self.maze.window.blit(lose_img, (0, 0))
                pygame.display.flip()
                return "lose"     
        
        elif self.state == "slopy_guard":
            return "slopy_guard"
        
        else:
            return "running"
  


    def move(self, direction:str):
        #with the string direction, we move macguyver in the structure with is sprite 
        #and test if we have an object on the case
        if direction == "down":
            #mac cannot go through walls                                      
            if self.maze.structure[self.pos_mac_y + 1][self.pos_mac_x] != 'W': 
                #macguyver cursor in .structure[] is moving   
                self.pos_mac_y += 1      
                #sprite in labyrinth is moving too                                     
                self.y = self.pos_mac_y * SPRITE_SIZE                        
                self.grab_items()

        elif direction == "up":
            if self.maze.structure[self.pos_mac_y - 1][self.pos_mac_x] != 'W':
                self.pos_mac_y -= 1
                self.y = self.pos_mac_y * SPRITE_SIZE
                self.grab_items()

        elif direction == "right":
            if self.maze.structure[self.pos_mac_y][self.pos_mac_x + 1] != 'W':
                self.pos_mac_x += 1
                self.x = self.pos_mac_x * SPRITE_SIZE
                self.grab_items()
        
        elif direction == "left":
            if self.maze.structure[self.pos_mac_y][self.pos_mac_x - 1] != 'W':
                self.pos_mac_x -= 1
                self.x = self.pos_mac_x * SPRITE_SIZE
                self.grab_items()
        return     
                       

    def grab_items(self):
        #"grab" items, add 1 to backpack and reposition sprite under the game 
        if (self.pos_mac_x,self.pos_mac_y) == self.maze.positions_items[0]:
            self.backpack += 1
            self.maze.positions_items[0] = (5,16)
        elif (self.pos_mac_x, self.pos_mac_y) == self.maze.positions_items[1]:
            self.backpack += 1
            self.maze.positions_items[1] = (8, 16)
        elif (self.pos_mac_x, self.pos_mac_y) == self.maze.positions_items[2]:
            self.backpack += 1
            self.maze.positions_items[2] = (11, 16)

