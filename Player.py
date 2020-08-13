#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 21:45:06 2020

@author: Elliot
"""

import PlayerBoard


class Player:

    def __init__(self, ID, AI, game):
        self.ID = ID
        self.playerBoard = PlayerBoard.PlayerBoard(game)
        self.AI = AI
        self.game = game

    def takeTurn(self):
        
        factoryChoiceID, tileColorChoice = self.AI.chooseTiles()
        print(tileColorChoice)
        # if a player chooses first from the center factory give them the first player tile
        if factoryChoiceID == 0 and self.game.factories[0].tiles[0].color == "firstPlayer":
            
            self.game.factories[0].hasFirstPlayerTile = False
            
            # place first player tile in player fill line
            firstPlayerTile = self.game.factories[0].tiles.pop()
            self.playerBoard.fillLine.placeTiles(firstPlayerTile)
        
        # get player tile color choice from factory of choice
        factory = [f for f in self.game.factories if f.ID == factoryChoiceID]


        tiles = factory[0].chooseTiles(tileColorChoice)
        tiles = {'color': tiles[0].color, 'tiles': tiles}
        
        # place tiles on pattern line of player choice
        self.playerBoard.patternLines[tileColorChoice].placeTiles(tiles, self.playerBoard) 
    
    # move tiles from pattern lines to the wall
    def tilesToWall(self):
        
        # if pattern line is full, move one tile to the tile wall
        for patternLine in self.playerBoard.patternLines:
            if patternLine.line.full():
                patternLine.tileToWall(self.ID, self.game)
