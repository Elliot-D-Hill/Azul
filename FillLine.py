#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 22:56:23 2020

@author: Elliot
"""
import collections


class FillLine:

    def __init__(self):
        self.fillLinePenalties = [-1, -1, -2, -2, -2, -3, -3]
        self.fillLine = collections.deque(maxlen=7)

    def placeTiles(self, tiles, game):
        for tile in tiles:
            if len(self.fillLine) < len(self.fillLinePenalties):
                self.fillLine.append(tile)
            else:
                game.tileLid.append(tile)
