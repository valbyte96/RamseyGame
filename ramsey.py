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
    graph = RGraph(N, R, WIDTH/2, HEIGHT/2)
    graph.draw(win)

    while True: #Game loop
        while True: #user turn 
            clickPoint = win.getMouse()
            ans1, p1 = graph.isTouched(clickPoint)
            if ans1:
                while True:
                    clickPoint = win.getMouse()
                    ans2, p2 = graph.isTouched(clickPoint)
                    if ans2:
                        line = Line(p1,p2)
                        line.draw(win)
                        break
                    
                    
                    
                

        #while True: #computer turn 

    




main()
