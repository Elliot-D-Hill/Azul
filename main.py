#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 13:06:59 2020

@author: Elliot
"""

import Game
import Tile

# setup game

numPlayers = 4
# AI = ['Angry', 'Greedy', 'Patient', 'Careful']

game = Game.Game(numPlayers)
game.setupGame()


tile = Tile.Tile('b')
tile2 = Tile.Tile('t')
game.players[0].playerBoard.wall.placeTile(tile, 3, 2)
game.players[0].playerBoard.wall.placeTile(tile2, 2, 4)
game.players[0].playerBoard.wall.printWall()
