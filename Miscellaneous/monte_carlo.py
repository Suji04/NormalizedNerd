import numpy as np
import random
import copy

org_deck = [
'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS',
'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD',
'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC',
'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH',
]


''' Q1. What is the probability that at least 2 Kings will appear 
    next to each other in the shuffled deck? '''

def KingKing(deck):
    for i in range(len(deck)-1):
        if deck[i][0] == 'K' and deck[i+1][0] == 'K':
            return True

def MonteCarlo1(n):
    res = 0
    for _ in range(n):
        deck = copy.deepcopy(org_deck)
        random.shuffle(deck)
        if KingKing(deck): res += 1
    print(res*100/n)

for i in range(1, 7):
    MonteCarlo(10**i)

'''
    output:
    40.0
    17.0
    20.6
    22.15
    21.645
    21.7206
'''


''' Q2. What is the probability that at least one King and one Queen
    will be next to each other or one card away? '''

def KingQueen(deck):
    n = len(deck)
    for i in range(n-1):
        if deck[i][0] + deck[i+1][0] in ['KQ', 'QK']:
            return True
        if i!=n-2:
            if deck[i][0] + deck[i+2][0] in ['KQ', 'QK']:
                return True

def MonteCarlo2(n):
    res = 0
    for _ in range(n):
        deck = copy.deepcopy(org_deck)
        random.shuffle(deck)
        if KingQueen(deck): res += 1
    print(res*100/n)

for i in range(1, 7):
    MonteCarlo2(10**i)

'''
    output:
    40.0
    73.0
    71.7
    73.35
    73.510
    73.5967
'''
