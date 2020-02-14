#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 12:34:18 2020

@author: Elliot
"""


class Factory:

    def __init__(self, ID):
        self.id = ID
        self.tiles = []

    def chooseTiles(self, colorChoice):
        # gets all the tiles of the color that the player chooses
        tilesOfColorChoice = [tile for tile in self.tiles
                              if tile == colorChoice]
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
