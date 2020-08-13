#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 08:44:49 2020

@author: Elliot
"""

import random
from abc import ABC, abstractmethod

class AzulAI(ABC):
    
    def __init__(self, game):        
        self.game = game
        
    @abstractmethod
    def chooseTiles(self):
        pass
    
class RandomBot(AzulAI):
    
    def __init__(self, game):
        super().__init__(game)
    
    # randomly choose factory and tile color
    def chooseTiles(self):
        factoryChoice = random.randrange(self.game.numFactories - 1)
        randomIdx = random.randrange(self.game.tilesPerFactory - 1)
        tileColorChoice = self.game.factories[factoryChoice].tiles[randomIdx].color

        return factoryChoice, tileColorChoice
        
    
class AggressiveBot(AzulAI):
    
    def __init__(self, game):
        super().__init__(game)
    
    def chooseTiles(self):
        pass
        
    
class GreedyBot(AzulAI):
    
    def __init__(self, game):
        super().__init__(game)
    
    def chooseTiles(self):
        pass
    
    
class PatientBot(AzulAI):
    
    def __init__(self, game):
        super().__init__(game)
    
    def chooseTiles():
        pass
    
class CautiousBot(AzulAI):
    
    def __init__(self, game):
        super().__init__(game)
    
    def chooseTiles():
        pass