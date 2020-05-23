#! /usr/bin/env python3
# coding: utf-8

import pygame

from maze import Maze


class Game:
    """
    Class for the gameplay.

    Hero movement and conditions of winning.
    """
    def __init__(self):
        """
        initialazing of maze and position in the game for all tests
        and interactions between characters and items.
        """
        self.maze = Maze("level.txt")
        self.guardian_pos = self.get_pos("G")
        self.stairsway_out_pos = self.get_pos("O")
        self.pos_mac = self.get_pos("M")
        self.state = "running"
        self.backpack = 0

    def run(self):
        """
        Loop of test for event and win / lose conditions.
        actualize / RE-Print sreen game after an event on keyboard.
        checking every events happening while the game is running.
        when keyborad's press.
        if arrow down pressed.
        move macguyver down.
        check win or lose conditions and guardian on maps.
        change the state of the game.
        """
        while True:
            if self.state == "running" or self.state == "slopy_guard":
                self.maze.display(self.pos_mac, self.state)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and
                        event.key == pygame.K_ESCAPE):
                    self.state = "quit"
                    return

                if event.type == pygame.KEYDOWN:
                    if self.state == "running" or self.state == "slopy_guard":
                        if event.key == pygame.K_DOWN:
                            self.move("down")

                        elif event.key == pygame.K_UP:
                            self.move("up")

                        elif event.key == pygame.K_RIGHT:
                            self.move("right")

                        elif event.key == pygame.K_LEFT:
                            self.move("left")
                        self.state = self.check_status()

                    if self.state != "running" and self.state != "slopy_guard":
                        if event.key == pygame.K_r:
                            self.state = "reset"
                            return

                        elif event.key == pygame.K_q:
                            self.state = "quit"
                            return

    def check_status(self) -> str:
        """
        after each move checking the new case for return a state for the game.
        display the victory screen.
        display the defeat screen.
        """
        if self.pos_mac[0] == self.stairsway_out_pos[0] and \
                self.pos_mac[1] == self.stairsway_out_pos[1]:
            win_img = pygame.image.load('ressource/win.jpg').convert_alpha()
            self.maze.window.blit(win_img, (0, 0))
            pygame.display.flip()
            return "win"

        elif self.pos_mac[0] == self.guardian_pos[0] \
                and self.pos_mac[1] == self.guardian_pos[1]:

            if self.backpack == 3:
                return "slopy_guard"

            else:
                lose_img = pygame.image.load(
                    'ressource/game_over.jpg').convert_alpha()
                self.maze.window.blit(lose_img, (0, 0))
                pygame.display.flip()
                return "lose"

        elif self.state == "slopy_guard":
            return "slopy_guard"

        else:
            return "running"

    def move(self, direction: str):
        """
        with the string direction, we move macguyver in the structure.
        mac cannot go through walls.
        test if we have an object on the case.
        macguyver cursor in .structure[] is moving.
        """
        if direction == "down":
            if self.maze.structure[
                    self.pos_mac[1] + 1][self.pos_mac[0]] != 'W':
                self.pos_mac[1] += 1
                self.grab_items()

        elif direction == "up":
            if self.maze.structure[
                    self.pos_mac[1] - 1][self.pos_mac[0]] != 'W':
                self.pos_mac[1] -= 1
                self.grab_items()

        elif direction == "right":
            if self.maze.structure[
                    self.pos_mac[1]][self.pos_mac[0] + 1] != 'W':
                self.pos_mac[0] += 1
                self.grab_items()

        elif direction == "left":
            if self.maze.structure[
                    self.pos_mac[1]][self.pos_mac[0] - 1] != 'W':
                self.pos_mac[0] -= 1
                self.grab_items()
        return

    def grab_items(self):
        """
        "grab" items, add 1 to backpack and reposition
        sprite under the game.
        """
        if self.pos_mac == self.maze.positions_items[0]:
            self.backpack += 1
            self.maze.positions_items[0] = (5, 16)
        elif self.pos_mac == self.maze.positions_items[1]:
            self.backpack += 1
            self.maze.positions_items[1] = (8, 16)
        elif self.pos_mac == self.maze.positions_items[2]:
            self.backpack += 1
            self.maze.positions_items[2] = (11, 16)

    def get_pos(self, sprite: str) -> int:
        """
        get the position in struct[] of the sprite pass in the fonction.
        """
        for y, col in enumerate(self.maze.structure):
            for x, case in enumerate(col):
                if case == sprite:
                    return [x, y]
