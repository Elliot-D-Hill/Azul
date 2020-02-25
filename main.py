#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 13:06:59 2020

@author: Elliot
"""

import Game

# setup game
numPlayers = 2
# AI = ['Angry', 'Greedy', 'Patient', 'Careful']

game = Game.Game(numPlayers)
game.setupGame()
game.fillFactories()

# game.players[0].playerBoard.wall.printWall()
# game.players[0].playerBoard.wall.printLegal()

for i in range(len(game.players[0].getFactoriesState(game))):
    print(game.players[0].getFactoriesState(game)[i])

print('\n')
