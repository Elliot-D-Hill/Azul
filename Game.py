#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 08:20:12 2020

@author: Elliot
"""
import queue
import random
import Factory
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
        self.firstPlayerTile = Tile.Tile("firstPlayer")
        self.tileColors = ["bl", "yl", "rd", "bk", "tl"]
        self.factoriesState = []
    
    def setupGame(self):

        # number of factories includes the center factory
        if self.numPlayers == 4:
            self.numFactories = 10
        elif self.numPlayers == 3:
            self.numFactories = 8
        elif self.numPlayers == 2:
            self.numFactories = 6
        else:
            raise Exception('Not a valid number of players. Choose from: 2-4')
        
        # fill array with the tiles
        for i in range(self.numTiles):
            if i < 20:
                self.tileArray[i] = Tile.Tile(self.tileColors[0])
            elif i >= 20 and i < 40:
                self.tileArray[i] = Tile.Tile(self.tileColors[1])
            elif i >= 40 and i < 60:
                self.tileArray[i] = Tile.Tile(self.tileColors[2])
            elif i >= 60 and i < 80:
                self.tileArray[i] = Tile.Tile(self.tileColors[3])
            else:
                self.tileArray[i] = Tile.Tile(self.tileColors[4])
        
        random.shuffle(self.tileArray)
        
        for i in range(self.numTiles):
            self.tileBag.put(self.tileArray[i])
        
        # create center factory
        self.factories.append(Factory.CenterFactory(0))
        
        # create all other factories
        for ID in range(1, self.numFactories):
            self.factories.append(Factory.Factory(ID))
            
        self.factoriesState = [dict.fromkeys(self.tileColors, 0) for f in self.factories]
        self.factoriesState[0].update({'fp' : 1})
            

    def roundIsOver(self):  
        
        for factory in self.factories:
            if not factory.tiles:
                roundIsOver = False
                break
            else:
                roundIsOver = True
                
        return roundIsOver

    # returns a boolean indicating if a row is full which implies the final round
    def gameOver(self):
        
        if not self.players:
            raise Exception('Player list is empty')
            
        rowLength = 5
        for i in range(self.numPlayers):
            for j in range(rowLength):
                counter = 0
                for k in range(rowLength):
                    if self.players[i].playerBoard.wall.tileWall[j][k] is not None:
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

    # fill factories with tiles 
    def fillFactories(self):
        
        # add first player tile to center
        self.factories[0].tiles.append(self.firstPlayerTile)
        self.factories[0].hasFirstPlayerTile = True
        
        # the +1 is because we don't want to fill the center factory
        for i in range(1, self.numFactories):
            for tile in range(self.tilesPerFactory):
                
                if not self.tileBag:
                    while not self.tileLid:
                        self.tileBag.put(self.tileLid.get())
                else:
                    self.factories[i].tiles.append(self.tileBag.get())
    
    # Update current state tiles in each factory
    def updateFactoriesState(self):
        
        if self.factories[0].hasFirstPlayerTile:
            self.factoriesState[0]['fp'] = 1
        else:
            self.factoriesState[0]['fp'] = 0
        
        for i in range(1, self.numFactories):
            for j in range(self.tilesPerFactory):

                tileColor = self.factories[i].tiles[j].color
                self.factoriesState[i][tileColor] += 1
                
        # center factory
        counter = 1
        while counter < len(self.factories[0].tiles):
            
            tileColor = self.factories[0].tiles[counter].color
            self.factoriesState[0][tileColor] += 1
            counter += 1
            
        return self.factoriesState
    
    def printFactoryState(self):
        for i in range(self.numFactories):
            print(self.factoriesState[i])
                
    def playRound(self, game): # FIXME
    
        # refill factories with tiles
        self.fillFactories()
        self.updateFactoriesState()
        self.printFactoryState()
        
        while self.roundIsOver():
            for player in self.players:
                if self.roundIsOver():
                    break
            self.printFactoryState
            player.takeTurn(game)

    def playGame(self):
        while not self.gameOver(self.players):
            self.playRound()
        
        winners = self.theWinnerIs()
        if len(winners) == 1:
            print("The winner is: ")
        else:
            print('The winners are: ')
        
        for winner in winners:
            print(winner)
            
            