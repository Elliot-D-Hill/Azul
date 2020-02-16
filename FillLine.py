#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 22:56:23 2020

@author: Elliot
"""
import queue


class FillLine:

    def __init__(self):
        self.fillLinePenalties = [-1, -1, -2, -2, -2, -3, -3]
        self.fillLine = queue.Queue(maxsize=7)

    def placeTiles(self, tiles):
        leftOverTiles = []
        for tile in tiles:
            if len(self.fillLine) < 8:
                self.fillLine.put(tile)
            else:
                leftOverTiles.append(tile)
        return leftOverTiles
