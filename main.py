#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 13:06:59 2020

@author: Elliot
"""

import Game
import Player
import AzulAI

# setup game
numPlayers = 2
# AI = ['Angry', 'Greedy', 'Patient', 'Careful']

game = Game.Game(numPlayers)
game.setupGame()

AI = AzulAI.RandomBot(game)

# fill an array of players
for ID in range(game.numPlayers):
    game.players.append(Player.Player(ID, AI, game))

game.printFactoryState()
print('\n')

game.playRound(game)

game.players[0].playerBoard.wall.printWall()
game.players[0].playerBoard.wall.printLegal()
game.updateFactoriesState()

