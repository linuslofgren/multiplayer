__author__ = 'Linus'

import random

players = []


class Player(object):
    timer = 50

    def __init__(self, name, x_pos, y_pos):
        self.name = name
        self.y_pos = y_pos
        self.x_pos = x_pos

    def serialize(self):
        return {
            'xPos': self.x_pos,
            'yPos': self.y_pos,
            'name': self.name
        }


def add(x, y):
    players.append(Player(players.__len__(),x,y))