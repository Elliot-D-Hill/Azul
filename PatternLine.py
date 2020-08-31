#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 22:35:37 2020

@author: Elliot
"""

# import queue
import collections


class PatternLine:

    
    def __init__(self, idx):
        self.idx = idx
        self.maxsize = idx + 1
        self.line = collections.deque(maxlen=self.maxsize)
        # self.line = queue.Queue(maxsize=self.maxsize)
        self.tileColors = ["bl", "yl", "rd", "bk", "tl"]

    def placeTiles(self, playerBoard, tiles, game):
    
        colorIdx = self.tileColors.index(tiles['color'])
        if playerBoard.wall.tileWall[self.idx][colorIdx]['tile'] is None:
            
            for tile in tiles:
                if self.line:
                    playerBoard.fillLine.placeTiles(tiles, game)
                    break
                else:                    
                    self.line.append(tiles['tiles'].pop())
        else:
            raise Exception('Invalid tile placement')
    
    def tileToWall(self, player, game):
        
        player.playerBoard.wall.placeTile(self.line.pop(), self.idx)
        
        # all other tiles go to the tile lid
        while not self.line.empty():
            game.tileLid.append(self.line.pop())