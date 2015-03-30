__author__ = 'Linus'


drawings = []


class Drawing(object):

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