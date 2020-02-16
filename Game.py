#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 08:20:12 2020

@author: Elliot
"""
import queue
import random
import Factory
import Player
import Tile

class Game:
    
    def __init__(self, numPlayers):
        self.numPlayers = numPlayers
        self.numFactories = None
        self.numTiles = 100
        self.tileArray = [None for i in range(self.numTiles)]
        self.factories = []
        self.players = []
        self.tileBag = queue.Queue(maxsize=self.numTiles)
        self.tileLid = queue.Queue(maxsize=self.numTiles)
        self.tilesPerFactory = 4
        self.winner = None
    
    def setupGame(self):

        if self.numPlayers == 4:
            self.numFactories = 9
        elif self.numPlayers == 3:
            self.numFactories = 7
        elif self.numPlayers == 2:
            self.numFactories = 5
        else:
            raise Exception('Not a valid number of players. Choose from: 2-4')
        
        # Tile colors
        tileColors = ["blue", "yellow", "red", "black", "teal"]
        
        # fill array with the tiles
        for i in range(len(self.tileArray)):
            if i < 20:
                self.tileArray[i] = Tile.Tile(tileColors[0])
            elif i >= 20 and i < 40:
                self.tileArray[i] = Tile.Tile(tileColors[1])
            elif i >= 40 and i < 60:
                self.tileArray[i] = Tile.Tile(tileColors[2])
            elif i >= 60 and i < 80:
                self.tileArray[i] = Tile.Tile(tileColors[3])
            else:
                self.tileArray[i] = Tile.Tile(tileColors[4])
        
        random.shuffle(self.tileArray)
        
        for i in range(self.numTiles):
            self.tileBag.put(self.tileArray[i])
        
        # create center factory
        self.factories.append(Factory.Factory(0))
        # create all other factories
        for ID in range(self.numFactories):
            self.factories.append(Factory.Factory(ID + 1))
        
        # fill an array of players
        for ID in range(self.numPlayers):
            self.players.append(Player.Player(ID))

def roundOver(self):        
    for factory in self.factories:
        if not factory.empty():
            roundIsOver = False
            break
        else:
            roundIsOver = True
    return roundIsOver


def gameOver(self):
    if not self.playerList:
        raise Exception('Player list is empty')
    rowLength = 5
    for i in range(self.numPlayers):
        for j in range(rowLength):
            counter = 0
            for k in range(rowLength):
                if self.playerList[i].playerBoard.wall.tileWall[j][k] is not None:
                    counter += 1
                    if counter == 5:
                        gameIsOver = True
                    else:
                        gameIsOver = False
    return gameIsOver

def theWinnerIs(self):
    scores = []
    for player in self.players:
        scores = player.scoreBoard.score
    # return multiple indices because there may be one or more ties
    winnerIndices = [i for i, score in enumerate(scores) if score == max(scores)]
    winners = [self.players[i] for i in winnerIndices]
    return winners

# Round setup. Operations that are repeated each round
def fillFactories(self):
    for i in range(len(self.factories)):
        for j in range(self.tilesPerFactory):
            if self.tileBag.empty():
                while not self.tileLid.empty():
                    self.tileBag.put(self.tileLid.get())
            else:
                self.factories[i].tiles.append(self.tileBag.get())
                
def playRound(self):
    # refill factories with tiles
    fillFactories(self.tileBag)

def playGame(self):
    while not self.gameOver(self.players):
        self.playRound()