'''
Ramsey Games

An opportunity to demonstrate well organized OOP

'''

from graphics import *
from RGraph import *
import math

WIDTH = 500
HEIGHT = 500
N = 7
rads = 6.28319 # 2 pi
R = 100
P = [] #list of points 

def main():
    win = GraphWin('Ramsey', WIDTH, HEIGHT)
    test = RGraph(N, R, WIDTH/2, HEIGHT/2)
    test.draw(win)

    while True:
        clickPoint = win.getMouse()
        test.isTouched(clickPoint)

    




main()
