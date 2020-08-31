#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 12:34:18 2020

@author: Elliot
"""


class Factory:

    def __init__(self, ID):
        self.factory_type = 'factory'
        self.ID = ID
        self.tiles = []

    def chooseTiles(self, colorChoice):
        
        # gets all the tiles of the color that the player chooses                        
        tilesOfColorChoice = [tile for tile in self.tiles
                              if tile.color == colorChoice]
        
        # removes tiles of color choice from the factory
        self.tiles = [tile for tile in self.tiles if tile != colorChoice]
        return tilesOfColorChoice

    def getRemainingTiles(self):
        if len(self.tiles) < 4:
            remainingTiles = self.tiles
            self.tiles = []
            return remainingTiles
        else:
            print("Number of tiles error")

class CenterFactory(Factory):
    
    def __init__(self, ID):
        super().__init__(ID)
        self.factory_type = 'center'
        self.ID = ID
        self.tiles = []
        self.hasFirstPlayerTile = True
        
        
        
        
        
