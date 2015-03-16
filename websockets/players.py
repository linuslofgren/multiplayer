__author__ = 'Linus'

import random

players = []


class Player(object):
    xPos = random.uniform(10,100)
    yPos = 10

    def __init__(self, name):
        self.name = name

    def serialize(self):
        return {
            'xPos': self.xPos,
            'yPos': self.yPos,
            'name': self.name
        }


def add():
    players.append(Player(players.__len__()+1))