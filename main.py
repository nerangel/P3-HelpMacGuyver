#! /usr/bin/env python3
# coding: utf-8

from game import Game


def main():
    """
    initializing game and loop while game.state is not "quit"
    and reset it if game.state is "reset"
    """
    game = Game()
    while game.state != "quit":
        game.run()
        if game.state == "reset":
            game = Game()


if __name__ == "__main__":
    main()
