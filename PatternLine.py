#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 22:35:37 2020

@author: Elliot
"""

import queue


class PatternLine:

    
    def __init__(self, idx, game):
        self.game = game
        self.idx = idx
        self.maxsize = idx + 1
        self.line = queue.Queue(maxsize=self.maxsize)
        self.tileColors = ["bl", "yl", "rd", "bk", "tl"]

    def placeTiles(self, tiles, playerBoard):
    
        colorIdx = self.tileColors.index(tiles['color'])
        if playerBoard.wall.tileWall[self.idx][colorIdx]['tile'] is None:
            
            for tile in tiles:
                
                if self.line.full():
                    playerBoard.fillLine.placeTiles(tiles, self.game)
                    break
                else:
                    
                    print('\n')
                    print(len(tiles['tiles']))
                    print(tiles['tiles'][0].color)
                    
                    self.line.put(tiles['tiles'].pop())
        else:
            raise Exception('Invalid tile placement')
    
    def tileToWall(self, playerID, game):
        
        game.players[playerID].playerBoard.wall.placeTile(self.line.pop(), self.idx)
        
        # all other tiles go to the tile lid
        while not self.line.empty():
            game.tileLid.put(self.line.pop())