#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 22:35:37 2020

@author: Elliot
"""

import queue


class PatternLines:

    def __init__(self):
        self.maxIndex = 5
        self.patternLines = [None for _ in range(self.maxIndex)]

        for i in range(self.maxIndex):
            self.patternLines[i] = queue.Queue(maxsize=i+1)

    def placeTiles(self, tiles, rowIdx, fillLine):
        for tile in tiles:
            if self.patternLines[rowIdx].full():
                fillLine.placeTiles(tiles)
                break
            else:
                self.patternLines[rowIdx].put(tiles.pop())
