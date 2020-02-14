#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 22:35:37 2020

@author: Elliot
"""

import queue


class PatternLine:

    def __init__(self):
        self.maxIndex = 5
        self.patternLines = [None for _ in range(self.maxIndex)]

        for i in range(1, self.maxIndex):
            self.patternLines = queue.Queue(maxsize=i)

    def placeTiles(self, rowOrFill, rowIdx, tiles):
        for i in range(len(tiles)):
            self.patternLines[rowIdx].put(tiles.pop())
