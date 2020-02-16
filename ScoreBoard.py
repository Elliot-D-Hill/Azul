#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 23:00:44 2020

@author: Elliot
"""


class ScoreBoard:

    def __init__(self):
        self.score = 0

    def applyPenalty(self, penalty):
        self.score = self.score - penalty

    def checkSpecialPoints(self, wall):
        def rowSpecial(wall):
            for i in range(wall.maxIdx):
                count = 0
                for j in range(wall.maxIdx):
                    if wall.tileWall[i,j] is not None:
                        count += 1
                if count == 5:
                    self.score += 2
                        
        def colSpecial(wall):
            for i in range(wall.maxIdx):
                count = 0
                for j in range(wall.maxIdx):
                    if wall.tileWall[j,i] is not None:
                        count += 1
                if count == 5:
                    self.score += 7
                    
        def fiveOfaKind(wall):
            counts = {"blue": 0, "yellow": 0, "red": 0, "black": 0, "teal": 0}
            for i in range(wall.maxIdx):
                for j in range(wall.maxIdx):
                    if wall.tileWall[j,i] is not None:
                        counts[wall.tileWall[j,i].color] += 1
            for count in counts:
                if counts[count] == 5:
                    self.score += 10