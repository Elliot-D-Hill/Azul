#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 21:42:49 2020

@author: Elliot
"""

import Wall
import PatternLine
import FillLine
import ScoreBoard


class PlayerBoard:

    def __init__(self):
        self.wall = Wall.Wall()
        self.patternLines = {color : PatternLine.PatternLine(i) 
                             for i, color in enumerate(self.wall.colors)}
        self.fillLine = FillLine.FillLine()
        self.scoreBoard = ScoreBoard.ScoreBoard()
