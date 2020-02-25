#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 22:35:37 2020

@author: Elliot
"""

import queue


class PatternLine:

    def __init__(self, idx):
        self.idx = idx
        self.maxsize = idx + 1
        self.line = queue.Queue(maxsize=self.maxsize)

    def placeTiles(self, tiles, playerBoard):
        if playerBoard.wall.tileWall[self.idx][tiles['color']] is None:
            for tile in tiles:
                if self.line.full():
                    playerBoard.fillLine.placeTiles(tiles)
                    break
                else:
                    self.line.put(tiles.pop())
        else:
            raise Exception('Invalid tile placement')
    
    def tileToWall(self, playerID, game):
        game.players[playerID].playerBoard.wall.placeTile(self.line.pop(), self.idx)
        # all other tiles go to the tile lid
        while not self.line.empty():
            game.tileLid.put(self.line.pop())