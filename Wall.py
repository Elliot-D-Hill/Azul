#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 22:39:11 2020

@author: Elliot
"""

from collections import deque

class Wall:

    def __init__(self):
        self.maxIdx = 5
        self.tileWall = [[None for _ in range(self.maxIdx)] for _ in range(self.maxIdx)]
        self.colors = deque(["bl", "yl", "rd", "bk", "tl"])
        # fill tile wall with dictionary that holds legal color and player tiles
        for row in range(self.maxIdx):
            for col in range(self.maxIdx):
                self.tileWall[row][col] = {'legalColor': self.colors[col], 'tile': None}
            self.colors.rotate(1)

    def countPoints(self, tile):
        rowPoints = 0
        colPoints = 0

        counter = tile.colIdx
        while self.tileWall[tile.rowIdx][counter].get('tile') is not None:
            rowPoints = rowPoints + 1
            counter = counter - 1
            if counter < 0:
                break

        counter = tile.colIdx
        while self.tileWall[tile.rowIdx][counter].get('tile') is not None:
            rowPoints = rowPoints + 1
            counter = counter + 1
            if counter > 4:
                break

        counter = tile.rowIdx
        while self.tileWall[tile.rowIdx][counter].get('tile') is not None:
            colPoints = colPoints + 1
            counter = counter - 1
            if counter < 0:
                break

        counter = tile.rowIdx
        while self.tileWall[tile.rowIdx][counter].get('tile') is not None:
            colPoints = colPoints + 1
            counter = counter + 1
            if counter > 4:
                break

        points = rowPoints + colPoints
        return points

    def placeTile(self, tile, rowIdx):
        tile.rowIdx = rowIdx
        # need to find column index of legal color
        for i in range(self.maxIdx):
            if self.tileWall[tile.rowIdx][i].get('legalColor') == tile.color:
                tile.colIdx = i
        # place tile in the wall at given row and color
        if 0 < tile.rowIdx and tile.colIdx < 5:
            if self.tileWall[tile.rowIdx][tile.colIdx].get('tile') is None:
                self.tileWall[tile.rowIdx][tile.colIdx]['tile'] = tile
            else:
                raise Exception('Invalid tile placement')
        else:
            raise Exception('Invalid tile placement')

        points = self.countPoints(tile)
        return points
        
    def printWall(self):
        for i in range(self.maxIdx):
            for j in range(self.maxIdx):
                if self.tileWall[i][j]['tile'] == None:
                    print(' |  ', end ='')
                else:
                    print(' | ' + self.tileWall[i][j]['tile'].color, end='')
                if j == self.maxIdx - 1:
                    print(' |\n')
                    
    def printLegal(self):
        for i in range(self.maxIdx):
            for j in range(self.maxIdx):
                print(' | ' + self.tileWall[i][j]['legalColor'], end='')
                if j == self.maxIdx - 1:
                    print(' |\n')
