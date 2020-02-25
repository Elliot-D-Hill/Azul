#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 21:45:06 2020

@author: Elliot
"""

import PlayerBoard


class Player:

    def __init__(self, ID, behavior):
        self.ID = ID
        self.playerBoard = PlayerBoard.PlayerBoard()
        self.AI = behavior # FIXME doesn't do anything right now...
    
    # get current state of factories
    def getFactoriesState(self, game):
        factoriesState = [dict.fromkeys(game.tileColors , 0) for f in game.factories]
        for i in range(1, game.numFactories):
            for j in range(game.tilesPerFactory):
                tileColor = game.factories[i].tiles[j].color
                factoriesState[i][tileColor] += 1
        # center factory
        counter = 1
        while counter < len(game.factories[0].tiles):
            tileColor = game.factories[0].tiles[counter].color
            factoriesState[0][tileColor] += 1
            counter += 1
        return factoriesState

    def takeTurn(self, game, factoryChoiceID, tileColorChoice, patternLineIdx):
        # if a player chooses first from the center factory give them the first player tile
        if factoryChoiceID == 0 and game.factories[0].tiles[0].color == "firstPlayer":
            # place first player tile in player fill line
            self.fillLine.placeTiles(game.factories[0].pop(0))
        
        # get player tile color choice from factory of choice
        factory = [f for f in game.factories if f.ID == factoryChoiceID]
        tiles = factory.chooseTiles(tileColorChoice)
        tiles = {'color': tiles[0].color, 'tiles': tiles}
        # place tiles on pattern line of player choice
        self.playerBoard.patternLines[patternLineIdx].placeTiles(tiles, self.playerBoard) 
    
    # move tiles from pattern lines to the wall
    def tilesToWall(self, game):
        # if pattern line is full, move one tile to the tile wall
        for patternLine in self.playerBoard.patternLines:
            if patternLine.line.full():
                patternLine.tileToWall(self.ID, game)
