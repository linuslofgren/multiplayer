__author__ = 'Linus'

import random

players = []


class Player(object):
    yPos = 10

    def __init__(self, name, x_pos):
        self.name = name
        self.x_pos = x_pos

    def serialize(self):
        return {
            'xPos': self.x_pos,
            'yPos': self.yPos,
            'name': self.name
        }


def add():
    players.append(Player(players.__len__(),random.uniform(10, 100)))