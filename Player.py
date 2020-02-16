#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 21:45:06 2020

@author: Elliot
"""

import PlayerBoard


class Player:

    def __init__(self, ID):
        self.ID = ID
        self.playerBoard = PlayerBoard.PlayerBoard()
    
    def getFactoryState():
        1 # FIXME

    def takeTurn(self, factories, factoryChoiceID,
                 tileColorChoice, patternLineIdxChoice):
        # get player tile color choice from factory of choice
        factory = [f for f in range(len(factories)) if
                   factories[f].ID == factoryChoiceID]
        tiles = factory.chooseTiles(tileColorChoice)
        self.playerBoard.patternLine.placeTiles(patternLineIdxChoice, tiles)
