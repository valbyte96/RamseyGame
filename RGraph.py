''' RGraph.py
AUTHOR: Val McCulloch
DATE: July 2017
DESCRIPTION: A class that creates an edgeless polygon of n points

:param n: number of vertices of polygon
:param r: radius of the circle in which the polygon is inscribed
:param x: x coordinate of the polygon's center
:param y: y coordinate of the polygon's center

'''

from graphics import *
import math
import random


class Node:

    def __init__(self, p, r, i):
        self.p = p
        self.x = p.getX()
        self.y = p.getY()
        self.r = r
        self.id = i  # id number
        self.circle = Circle(p, r)

    def draw(self, win):
        self.circle.setFill('black')
        self.circle.draw(win)

    def getCenter(self):
        return self.p

    def getID(self):
        return self.id

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def color(self, color):
        self.circle.setFill(color)


class RGraph:

    def __init__(self, n, r, x, y):
        self.n = n
        self.r = r
        self.x = x
        self.y = y
        self.d_rads = 6.28319 / n  # change in radians (2pi/n)
        self.verts = []  # stores verts
        self.c = 5  # small circle radius

    def draw(self, win):
        # init
        R = self.r  # radius
        l = self.c
        rad = 0  # angle
        for i in range(self.n):
            x = R * math.cos(rad) + self.x
            y = R * math.sin(rad) + self.y
            p = Point(x, y)
            c = Node(p, l, i)
            self.verts.append(c)  # store point
            c.draw(win)
            rad += self.d_rads  # adjust angle

    def getRand(self):
        r1 = random.randint(0, self.n - 1)
        r2 = random.randint(0, self.n - 1)
        while r1 == r2:
            r2 = random.randint(0, self.n - 1)
        return self.verts[r1], self.verts[r2]

    def isTouched(self, checkPoint):
        x = checkPoint.getX()
        y = checkPoint.getY()
        c = self.c
        for v in self.verts:
            v_x = v.getX()
            v_y = v.getY()
            if x > v_x - c and x < v_x + c and y > v_y - c and y < v_y + c:
                v.color('red')
                return True, v
        return False, None
    def isComplete(self, list1, list2):
        N = self.n #number of verts
        maxE = N*(N-1)/2
        if len(list1)+len(list2)>=maxE:
            return True
        return False
