#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 08:44:49 2020

@author: Elliot
"""

import collections
import random
from abc import ABC, abstractmethod

class AzulAI(ABC):
        
    @abstractmethod
    def chooseTiles(self):
        pass
    
class RandomBot(AzulAI):
    
    # randomly choose factory and tile color
    def chooseTiles(self, game):
        
        fullFactories = collections.deque()
        for i, f in enumerate(game.factories):
            if f.tiles:
                if f.factory_type=='center' and len(f.tiles) > 1:
                    fullFactories.append(i)
                else:
                    fullFactories.append(i)
                
        factoryChoice = random.choice(fullFactories)
        print(factoryChoice)
        factory = game.factories[factoryChoice]
        
        
        if factory.factory_type == 'center' and len(f.tiles) > 1:
            randomIdx = random.randrange(1, len(factory.tiles))
        else:
            randomIdx = random.randrange(game.tilesPerFactory - 1)
            
        tile = factory.tiles[randomIdx]

        tileColorChoice = tile.color

        return factoryChoice, tileColorChoice
        
    
class AggressiveBot(AzulAI):
    
    def chooseTiles(self):
        pass
        
    
class GreedyBot(AzulAI):
    
    def chooseTiles(self):
        pass
    
    
class PatientBot(AzulAI):
    
    def chooseTiles():
        pass
    
class CautiousBot(AzulAI):
    
    def chooseTiles():
        pass