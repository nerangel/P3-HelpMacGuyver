#! /usr/bin/env python3
# coding: utf-8

import random

import pygame

from constants import ROWS, COLUMNS, SPRITE_SIZE


class Maze:
    """
    Class for display everything

    Everything possess is place define by .struct[]
    load itself from a .txt also in this class.
    """
    def __init__(self, filename: str):
        """
        windows build.
        loading all image with pygame.
        convert() -> optimization.
        convert_alpha() -> transparency.
        two add for the windows icon and title.
        """
        self.filename = filename
        self.load_from_file(filename)

        pygame.init()
        self.window = pygame.display.set_mode(
            (COLUMNS * SPRITE_SIZE, ROWS * SPRITE_SIZE))
        logo_image = pygame.image.load(
            'ressource/MacGyver.jpg')
        self.wall_img = pygame.image.load(
            'ressource/wall.png').convert()
        self.backgr_img = pygame.image.load(
            'ressource/backgr.jpg').convert()
        self.macgyver_img = pygame.image.load(
            'ressource/MacGyver.png').convert_alpha()
        self.guardian_img = pygame.image.load(
            'ressource/Gardien.png').convert_alpha()
        self.stairsway_out_image = pygame.image.load(
            'ressource/stairsway_out.png').convert_alpha()
        self.needle_img = pygame.image.load(
            'ressource/needle.png').convert_alpha()
        self.ether_img = pygame.image.load(
            'ressource/ether.png').convert_alpha()
        self.syringe_img = pygame.image.load(
            'ressource/seringue.png').convert_alpha()
        self.bubble = pygame.image.load(
            'ressource/bubble.png').convert_alpha()

        pygame.display.set_icon(logo_image)
        pygame.display.set_caption("Aidez MacGyver à s'échapper !")

        self.randomize_items()

    def display(self, pos_mac: int, state: str):
        """
        display labyrinth and elements.
        run throught .structure[] to print each sprit
        matching letters in the txt file.
        display wall, macgyver stairsway out and guardian's sprits.
        """
        self.window.fill((0, 70, 250))
        self.window.blit(self.backgr_img, (20, 20))

        for y, col in enumerate(self.structure):
            for x, case in enumerate(col):
                pos_sprite = x * SPRITE_SIZE, y * SPRITE_SIZE
                if case == "W":
                    self.window.blit(self.wall_img, pos_sprite)
                elif case == "M":
                    self.window.blit(self.macgyver_img, (
                        pos_mac[0] * SPRITE_SIZE, pos_mac[1] * SPRITE_SIZE))
                elif case == "O":
                    self.window.blit(self.stairsway_out_image, pos_sprite)
                elif case == "G":
                    self.position_G_sprit = pos_sprite
                    self.window.blit(self.guardian_img, pos_sprite)

        needle, syringe, ether = self.positions_items
        self.window.blit(self.needle_img, (
            needle[0] * SPRITE_SIZE, needle[1] * SPRITE_SIZE))
        self.window.blit(self.syringe_img, (
            syringe[0] * SPRITE_SIZE, syringe[1] * SPRITE_SIZE))
        self.window.blit(self.ether_img, (
            ether[0] * SPRITE_SIZE, ether[1] * SPRITE_SIZE))

        if state == "slopy_guard":
            self.window.blit(self.bubble, self.position_G_sprit)

        pygame.display.flip()

    def load_from_file(self, filename: str):
        """
        create maze structure in list from the txt file
        opening file.txt in reading mode
        reading each line in file.txt and add it in
        structure.
        """
        self.structure = []
        with open(filename, "r") as f:
            self.structure = [list(line) for line in f.readlines()]

    def randomize_items(self):
        """
        define 3 random positions for items.
        run throught .structure[] searching for " "
        and create a random positions.
        positions items throught .structure[].
        append possibilities position on maze.
        create a list of 3 random positions.
        """
        self.items_possibilities = []
        for y, col in enumerate(self.structure):
            for x, case in enumerate(col):
                if case == " ":
                    position_item = [x, y]
                    self.items_possibilities.append(position_item)
        self.positions_items = random.sample(self.items_possibilities, 3)
