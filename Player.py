#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 21:45:06 2020

@author: Elliot
"""

import PlayerBoard


class Player:

    def __init__(self, ID, AI):
        self.ID = ID
        self.playerBoard = PlayerBoard.PlayerBoard()
        self.AI = AI

    def takeTurn(self, game):
        
        factoryChoiceID, tileColorChoice = self.AI.chooseTiles(game)
        
        # if a player chooses first from the center factory give them the first player tile
        if factoryChoiceID == 0 and game.factories[0].tiles[0].color == 'firstPlayer':            
            # place first player tile in player fill line
            firstPlayerTile = game.factories[0].tiles.leftpop()
            game.factories[0].hasFirstPlayerTile = False
            self.playerBoard.fillLine.placeTiles([firstPlayerTile], game)
        
        # get player tile color choice from factory of choice
        factory = game.factories[factoryChoiceID]
        tiles = factory.chooseTiles(tileColorChoice)
        tiles = {'color': tiles[0].color, 'tiles': tiles}
        
        # move remaining tiles from factory to center factory
        if factory.tiles and factory.factory_type != 'center': 
            for tile in factory.tiles:
                game.factories[0].tiles.append(tile)
        
        # place tiles on pattern line of player choice
        patternLines = self.playerBoard.patternLines[tileColorChoice]
        patternLines.placeTiles(self.playerBoard, tiles, game) 
    
    # move tiles from pattern lines to the wall
    def tilesToWall(self, game):
        
        # if pattern line is full, move one tile to the tile wall
        for patternLine in self.playerBoard.patternLines:
            if patternLine.line.full():
                patternLine.tileToWall(self.ID, game)
