#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 13:06:59 2020

@author: Elliot
"""
import queue
import random
import Factory
import Player

# setup game

numPlayers = 4

if numPlayers == 4:
    numFactories = 9
elif numPlayers == 3:
    numFactories = 7
elif numPlayers == 2:
    numFactories = 5
else:
    print("Not a valid number of players. Choose from: 2-4")

# Tile colors
tiles = ["blue", "yellow", "red", "black", "teal"]

# Initialize and fill array with the tiles
tileArray = [None for i in range(100)]

for i in range(len(tileArray)):
    if i < 20:
        tileArray[i] = tiles[0]
    elif i >= 20 and i < 40:
        tileArray[i] = tiles[1]
    elif i >= 40 and i < 60:
        tileArray[i] = tiles[2]
    elif i >= 60 and i < 80:
        tileArray[i] = tiles[3]
    else:
        tileArray[i] = tiles[4]

random.shuffle(tileArray)

tileBag = queue.Queue(maxsize=100)
tileLid = queue.Queue(maxsize=100)

for i in range(100):
    tileBag.put(tileArray[i])

factories = []
# create center factory
factories.append(Factory.Factory("center"))

# create and fill an array of factories
for ID in range(numFactories):
    factories.append(Factory.Factory(ID + 1))

# create and fill an array of players
players = []
for ID in range(numPlayers):
    players.append(Player.Player(ID))


def isGameOver(playerList):
    for i in range(numPlayers):
        for j in range(5):
            counter = 0
            for k in range(5):
                if playerList[i].playerBoard.wall.tileWall[j][k] is not None:
                    counter += 1
                    if counter == 5:
                        isRowComplete = True
                    else:
                        isRowComplete = False
    return isRowComplete


# Round setup. Operations that are repeated each round
def fillFactories(tileBag):
    for i in range(len(factories)):
        for j in range(4):
            if not tileBag.empty():
                factories[i].tiles.append(tileBag.get())
            else:
                while not tileLid.empty():
                    tileBag.put(tileLid.get())


def playRound():
    # refill factories with tiles
    fillFactories(tileBag)


# begin game
def playGame():
    while isGameOver(players) is False:  # FIXME
        playRound()


# count scores
for i in range(numPlayers):
    players[i].playerBoard.wall.countPoints()
