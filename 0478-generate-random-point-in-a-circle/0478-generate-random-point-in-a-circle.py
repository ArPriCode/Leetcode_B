import random
import math

class Solution(object):

    def __init__(self, radius, x_center, y_center):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self):
        d = self.r * math.sqrt(random.random())
        theta = 2 * math.pi * random.random()
        return [
            self.x + d * math.cos(theta),
            self.y + d * math.sin(theta)
        ]