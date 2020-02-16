#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 22:39:11 2020

@author: Elliot
"""


class Wall:

    def __init__(self):
        self.maxIdx = 5
        self.tileWall = [[None for _ in range(self.maxIdx)] for _ in range(self.maxIdx)]

    def countPoints(self, tile):
        rowPoints = 0
        colPoints = 0

        counter = tile.colIndex
        while self.tileWall[tile.rowIndex][counter] is not None:
            rowPoints = rowPoints + 1
            counter = counter - 1
            if counter < 0:
                break

        counter = tile.colIndex
        while self.tileWall[tile.rowIndex][counter] is not None:
            rowPoints = rowPoints + 1
            counter = counter + 1
            if counter > 4:
                break

        counter = tile.rowIndex
        while self.tileWall[tile.rowIndex][counter] is not None:
            colPoints = colPoints + 1
            counter = counter - 1
            if counter < 0:
                break

        counter = tile.rowIndex
        while self.tileWall[tile.rowIndex][counter] is not None:
            colPoints = colPoints + 1
            counter = counter + 1
            if counter > 4:
                break

        points = rowPoints + colPoints
        return points

    def placeTile(self, tile, rowIdx, colIdx):
        tile.rowIndex = rowIdx
        tile.colIndex = colIdx
        if 0 < tile.rowIndex and tile.colIndex < 5:
            if self.tileWall[tile.rowIndex][tile.colIndex] is None:
                self.tileWall[tile.rowIndex][tile.colIndex] = tile
            else:
                raise Exception('Invalid tile placement')
        else:
            raise Exception('Invalid tile placement')

        points = self.countPoints(tile)
        return points
        
    def printWall(self):
        for i in range(self.maxIdx):
            for j in range(self.maxIdx):
                if self.tileWall[i][j] == None:
                    print(' |  ', end ='')
                else:
                    print(' | ' + self.tileWall[i][j].color, end='')
                if j == self.maxIdx - 1:
                    print(' |\n')
