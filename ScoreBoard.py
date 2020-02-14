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

    def checkSpecialPoints():
        1  # FIXME
