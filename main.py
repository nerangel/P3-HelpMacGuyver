#! /usr/bin/env python3
# coding: utf-8

from game import Game

def main():
    #reset: 0 = running / 1 = reset / 2 = quit
    reset = 0
    while reset != 2:
        level = Game()
        reset = level.run()
        
       
if __name__ == "__main__":
    main()